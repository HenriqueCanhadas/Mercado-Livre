from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from collections import defaultdict
import time
import smtplib
from email.message import EmailMessage
import datetime

# === CONFIGURAÇÕES DE FILTRO E RESULTADOS ===

termos_relevantes = ["1/43", "1:43", "f1", "formula 1"]

exclusoes_titulo = [
    "hot wheels f1 - mc donalds",
    "mclaren f1-mcl36",
]

exclusoes_id_link = [
    "mlb-1929640090",
    "mlb22449590",
]

NUMERO_ITENS_BARATOS = 5

# === PADRÕES PARA CATEGORIZAÇÃO DE MINIATURAS ===

padroes_preto = [
    "apxgp", "preto", "expensity", "cor apx", "cor apxgp", "modelo apxgp"
]

padroes_vermelho = [
    "vermelho", "automac", "app", "automaq", "maisto", "modelo vermelho"
]

# === CONFIGURAR CHROME ===

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
)
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 20)

# === ACESSAR SITE DO MERCADO LIVRE ===

url = "https://lista.mercadolivre.com.br/mc-donalds-f1-1%2F43#D[A:mc%20donalds%20f1%201/43]"
driver.get(url)

# === FUNÇÕES AUXILIARES ===

def extrair_valor_em_reais(preco_str):
    try:
        preco_limpo = preco_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
        return float(preco_limpo)
    except:
        return float('inf')

def rolar_pagina(driver, pause_time=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def extrair_resultados(lista_xpath, total_itens, driver):
    resultados = []
    for i in range(1, total_itens + 1):
        try:
            item_xpath = f'{lista_xpath}/li[{i}]'
            item = driver.find_element(By.XPATH, item_xpath)

            try:
                titulo_elem = item.find_element(By.XPATH, './/h3/a')
                titulo = titulo_elem.text.strip()
                link = titulo_elem.get_attribute('href')
            except:
                continue

            titulo_lower = titulo.lower()
            link_lower = (link or "").lower()

            if any(padrao in titulo_lower for padrao in exclusoes_titulo) or \
               any(padrao in link_lower for padrao in exclusoes_id_link):
                continue

            if not any(term in titulo_lower for term in termos_relevantes):
                continue

            try:
                preco_elem = item.find_element(By.CLASS_NAME, 'andes-money-amount')
            except NoSuchElementException:
                continue

            try:
                symbol = preco_elem.find_element(By.CLASS_NAME, 'andes-money-amount__currency-symbol').text
                fraction = preco_elem.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text
                cents = preco_elem.find_element(By.CLASS_NAME, 'andes-money-amount__cents').text
                preco = f"{symbol} {fraction},{cents}"
            except:
                preco = preco_elem.text.strip()

            # === CATEGORIZAÇÃO REFINADA ===
            if "mc donalds" not in titulo_lower and "mcdonald" not in titulo_lower and "o filme" not in titulo_lower:
                categoria = 'Desconhecido'
            else:
                is_dupla = any(p in titulo_lower for p in [
                    "set 2un", "kit 2x", "kit c/2", "dupla", "2x miniatura", "2x miniaturas", "kit com 2", "2 unidades"
                ])
                is_vermelha = any(p in titulo_lower for p in padroes_vermelho)
                is_preta = any(p in titulo_lower for p in padroes_preto)

                if is_dupla:
                    categoria = '2un'
                elif is_vermelha and is_preta:
                    categoria = 'Vermelha' if "vermelho" in titulo_lower else 'Preta'
                elif is_vermelha:
                    categoria = 'Vermelha'
                elif is_preta:
                    categoria = 'Preta'
                else:
                    categoria = 'Desconhecido'

            resultados.append({
                'Título': titulo,
                'Preço': preco,
                'Link': link,
                'Possui 1/43': '✅',
                'Posição': i,
                'Categoria': categoria
            })

        except StaleElementReferenceException:
            print(f"[Aviso] Item {i} ficou obsoleto, pulando...")
        except Exception as e:
            print(f"[Erro] Falha ao processar item {i}: {e}")
    return resultados

def navegar_por_paginas(driver, wait, lista_xpath):
    todos_resultados = []
    pagina = 1

    while True:
        print(f"\n🌐 Página {pagina}:")
        time.sleep(2)
        rolar_pagina(driver)

        lista_elementos = driver.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")
        total_itens = len(lista_elementos)
        print(f"🔎 Total de itens nesta página: {total_itens}")

        resultados = extrair_resultados(lista_xpath, total_itens, driver)
        todos_resultados.extend(resultados)

        try:
            botao_seguinte = driver.find_element(By.XPATH, "//a[@title='Seguinte']")
            if botao_seguinte.is_enabled() and botao_seguinte.is_displayed():
                driver.execute_script("arguments[0].click();", botao_seguinte)
                pagina += 1
                time.sleep(2)
            else:
                break
        except NoSuchElementException:
            break

    return todos_resultados

def exibir_mais_baratos(resultados, n=1):
    itens_validos = [item for item in resultados if 'R$' in item['Preço']]
    itens_ordenados = sorted(itens_validos, key=lambda x: extrair_valor_em_reais(x['Preço']))
    if itens_ordenados:
        mais_baratos = itens_ordenados[:n]
        print("\n=== PRODUTO(S) MAIS BARATO(S) ===\n")
        for item in mais_baratos:
            print(f"Item original posição: {item['Posição']}")
            print(f"✅ 1/43: {item['Possui 1/43']} | Categoria: {item['Categoria']}")
            print(f"Título: {item['Título']}")
            print(f"Preço:  {item['Preço']}")
            print(f"Link:   {item['Link']}")
            print("-" * 100)
    else:
        print("\nNenhum item com preço válido foi encontrado.")

def exibir_por_categoria(resultados):
    categorias = defaultdict(list)
    for item in resultados:
        categorias[item['Categoria']].append(item)

    for categoria, itens in categorias.items():
        print(f"\n=== Categoria: {categoria} - {len(itens)} Itens ===")
        itens_ordenados = sorted(itens, key=lambda x: extrair_valor_em_reais(x['Preço']))
        for item in itens_ordenados:
            print(f"Posição: {item['Posição']} | Preço: {item['Preço']} | Título: {item['Título']}")
            print(f"Link: {item['Link']}")
            print("-" * 80)

def enviar_email_mais_baratos(resultados, n=5):
    import datetime
    from email.message import EmailMessage
    from collections import defaultdict
    import smtplib

    email_remetente = 'pedrosacanhadas@gmail.com'
    senha_app = 'xwxk tvei frjw lfnl'
    destinatarios = ['pedrosacanhadas@gmail.com']

    categorias_legenda = {
        '2un': '🧩 Ambos',
        'Vermelha': '🟥 Mc Donalds 🟨',
        'Preta': '⬛ ApxGP 🟨',
        'Desconhecido': '❓ Desconhecido'
    }

    estilos_categoria = {
        '2un': {
            'bg': '#eeeeee',
            'color': '#000000',
            'td_color': '#eeeeee',
            'price_color': '#000000',
            'th_bg': '#eeeeee',
            'th_color': '#000000',
        },
        'Preta': {
            'bg': '#1e1e1e',
            'color': '#FFD700',
            'td_color': '#000000',
            'price_color': '#FFD700',
            'th_bg': '#000000',
            'th_color': '#FFD700',
        },
        'Vermelha': {
            'bg': '#FF0000',
            'color': '#FFFF00',
            'td_color': '#FF0000',
            'price_color': '#FFD700',
            'th_bg': '#FF0000',
            'th_color': '#FFFF00',
        },
        'Desconhecido': {
            'bg': '#dddddd',
            'color': '#000000',
            'td_color': '#eeeeee',
            'price_color': '#000000',
            'th_bg': '#f0f0f0',
            'th_color': '#000000',
        }
    }

    def extrair_valor_em_reais(preco_str):
        try:
            return float(preco_str.replace('R$', '').replace('.', '').replace(',', '.').strip())
        except:
            return float('inf')

    ordem_categorias = ['2un', 'Preta', 'Vermelha', 'Desconhecido']
    data_envio = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                background-color: #f9f9f9;
                font-family: Arial, sans-serif;
                color: #333;
                padding: 20px;
            }}
            h2 {{
                color: #444;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 8px;
            }}
            a {{
                color: #1a0dab;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .rodape {{
                font-size: 12px;
                margin-top: 40px;
                color: #888;
            }}
        </style>
    </head>
    <body>
        <h2>✅ Relatório de Miniaturas McDonald's F1 1/43</h2>
        <p><strong>Total de itens relevantes encontrados:</strong> {len(resultados)}</p>
    """

    agrupados = defaultdict(list)
    for item in resultados:
        if 'R$' in item['Preço']:
            agrupados[item['Categoria']].append(item)

    for categoria in ordem_categorias:
        itens = agrupados.get(categoria, [])
        if not itens:
            continue

        estilo = estilos_categoria.get(categoria, {})
        bg_color = estilo.get('bg', '#ffffff')
        text_color = estilo.get('color', '#000000')
        td_color = estilo.get('td_color', '#ffffff')
        price_color = estilo.get('price_color', '#000000')
        th_bg = estilo.get('th_bg', '#f0f0f0')
        th_color = estilo.get('th_color', '#000000')

        titulo_categoria = categorias_legenda.get(categoria, categoria)
        itens_ordenados = sorted(itens, key=lambda x: extrair_valor_em_reais(x['Preço']))[:n]

        html += f"""
        <div class="categoria" style="background-color: {bg_color}; color: {text_color}; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); padding: 15px; margin-bottom: 25px;">
            <h3>{titulo_categoria} - Top {len(itens_ordenados)}</h3>
            <table>
                <thead>
                    <tr style="background-color: {th_bg}; color: {th_color};">
                        <th>Posição</th>
                        <th>1/43</th>
                        <th>Título</th>
                        <th>Preço</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
        """

        for item in itens_ordenados:
            preco_formatado = item['Preço'].replace('\n', ' ')
            html += f"""
                    <tr style="background-color: {td_color}; color: {text_color};">
                        <td style="text-align:center;">{item['Posição']}</td>
                        <td style="text-align:center;">{item['Possui 1/43']}</td>
                        <td>{item['Título']}</td>
                        <td style="color: {price_color};">{preco_formatado}</td>
                        <td><a href="{item['Link']}">🔗 Ver Produto</a></td>
                    </tr>
            """

        html += """
                </tbody>
            </table>
        </div>
        """

    html += f"""
        <div class="rodape">
            Relatório gerado automaticamente em {data_envio}.<br>
            Desenvolvido pelo seu script de monitoramento. 🚀
        </div>
    </body>
    </html>
    """

    msg = EmailMessage()
    msg['Subject'] = '📦 Itens Mais Baratos - Miniaturas McDonald\'s F1 1/43'
    msg['From'] = email_remetente
    msg['To'] = ', '.join(destinatarios)

    msg.set_content("Seu cliente de e-mail não suporta HTML.")
    msg.add_alternative(html, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_remetente, senha_app)
            smtp.send_message(msg)
        print('✅ E-mail HTML com layout personalizado enviado com sucesso!')
    except Exception as e:
        print(f'❌ Erro ao enviar e-mail: {e}')

# === EXECUÇÃO PRINCIPAL ===

wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ui-search-layout__item")))

lista_xpath = '//*[@id="root-app"]/div/div[2]/section/div[5]/ol'
resultados = navegar_por_paginas(driver, wait, lista_xpath)

exibir_por_categoria(resultados)
exibir_mais_baratos(resultados, NUMERO_ITENS_BARATOS)
enviar_email_mais_baratos(resultados, NUMERO_ITENS_BARATOS)
