from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

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

NUMERO_ITENS_BARATOS = 3

# === CONFIGURAR CHROME COM PERFIL ===

#PROFILE_PATH = r"user-data-dir=C:\Users\c0ntr\Documents\Github\Mercado-Livre\ChromeProfile"
#chrome_options = Options()
#chrome_options.add_argument(PROFILE_PATH)
#chrome_options.add_argument("--headless=new")
#chrome_options.add_experimental_option("prefs", {
#    "download.prompt_for_download": False,
#    "download.directory_upgrade": True,
#    "safebrowsing.enabled": True
#})
#driver = webdriver.Chrome(options=chrome_options)

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
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

            resultados.append({
                'Título': titulo,
                'Preço': preco,
                'Link': link,
                'Possui 1/43': '✅',
                'Posição': i
            })

        except StaleElementReferenceException:
            print(f"[Aviso] Item {i} ficou obsoleto, pulando...")
        except Exception as e:
            print(f"[Erro] Falha ao processar item {i}: {e}")
    return resultados

def exibir_resultados(resultados):
    print("\n=== RESULTADOS DOS ITENS RELEVANTES ===\n")
    for item in resultados:
        print(f"Item original posição: {item['Posição']}")
        print(f"✅ 1/43: {item['Possui 1/43']}")
        print(f"Título: {item['Título']}")
        print(f"Preço:  {item['Preço']}")
        print(f"Link:   {item['Link']}")
        print("-" * 100)
    print(f"\nTotal de itens com termos relevantes (1/43): {len(resultados)}")

def exibir_mais_baratos(resultados, n=1):
    itens_validos = [item for item in resultados if 'R$' in item['Preço']]
    itens_ordenados = sorted(itens_validos, key=lambda x: extrair_valor_em_reais(x['Preço']))
    if itens_ordenados:
        mais_baratos = itens_ordenados[:n]
        print("\n=== PRODUTO(S) MAIS BARATO(S) ===\n")
        for item in mais_baratos:
            print(f"Item original posição: {item['Posição']}")
            print(f"✅ 1/43: {item['Possui 1/43']}")
            print(f"Título: {item['Título']}")
            print(f"Preço:  {item['Preço']}")
            print(f"Link:   {item['Link']}")
            print("-" * 100)
    else:
        print("\nNenhum item com preço válido foi encontrado.")

def enviar_email_mais_baratos(resultados, n=3):
    import smtplib
    from email.message import EmailMessage

    email_remetente = 'pedrosacanhadas@gmail.com'
    senha_app = os.getenv('EMAIL_SENHA_APP')
    destinatarios = ['pedrosacanhadas@gmail.com']

    itens_validos = [item for item in resultados if 'R$' in item['Preço']]
    itens_ordenados = sorted(itens_validos, key=lambda x: extrair_valor_em_reais(x['Preço']))
    mais_baratos = itens_ordenados[:n]

    # Monta o corpo do e-mail em HTML
    html = f"""
    <html>
    <body>
        <h2>✅ Miniaturas McDonald's F1 1/43 - Itens Mais Baratos</h2>
        <p><strong>Total de itens com termos relevantes (1/43):</strong> {len(resultados)}</p>
        <table border="1" cellspacing="0" cellpadding="6" style="border-collapse: collapse; font-family: Arial; font-size: 14px;">
            <thead>
                <tr style="background-color: #f2f2f2;">
                    <th>Posição</th>
                    <th>1/43</th>
                    <th>Título</th>
                    <th>Preço</th>
                    <th>Link</th>
                </tr>
            </thead>
            <tbody>
    """

    for item in mais_baratos:
        preco_formatado = item['Preço'].replace('\n', ' ')
    
        html += f"""
        <tr>
            <td style="text-align: center;">{item['Posição']}</td>
            <td style="text-align: center;">{item['Possui 1/43']}</td>
            <td>{item['Título']}</td>
            <td>{preco_formatado}</td>
            <td><a href="{item['Link']}">🔗 Ver Produto</a></td>
        </tr>
        """

    html += """
            </tbody>
        </table>
        <p style="margin-top:20px;">Enviado automaticamente por seu script de monitoramento. 🚀</p>
    </body>
    </html>
    """

    msg = EmailMessage()
    msg['Subject'] = 'Miniaturas McDonald\'s F1 1/43 - Itens Mais Baratos'
    msg['From'] = email_remetente
    msg['To'] = ', '.join(destinatarios)

    msg.set_content("Seu cliente de e-mail não suporta HTML.")
    msg.add_alternative(html, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_remetente, senha_app)
            smtp.send_message(msg)
        print('✅ E-mail HTML com os itens mais baratos enviado com sucesso!')
    except Exception as e:
        print(f'❌ Erro ao enviar e-mail: {e}')

# === AGUARDAR LISTA DE PRODUTOS ===

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[5]/ol')))

# === ROLAR A PÁGINA PARA CARREGAR TODOS OS ITENS ===

rolar_pagina(driver)

# === COLETAR E FILTRAR ITENS ===

time.sleep(2)
lista_xpath = '//*[@id="root-app"]/div/div[2]/section/div[5]/ol'
lista_elementos = driver.find_elements(By.XPATH, f"{lista_xpath}/li")
total_itens = len(lista_elementos)

resultados = extrair_resultados(lista_xpath, total_itens, driver)

# === EXIBIR RESULTADOS FILTRADOS E MAIS BARATOS ===

exibir_resultados(resultados)
exibir_mais_baratos(resultados, NUMERO_ITENS_BARATOS)
enviar_email_mais_baratos(resultados, NUMERO_ITENS_BARATOS)
