# Unreleased

# 6.23.0 - 2025-06-24

- Clean up logic for deprecated pref keys.
- Add encoded cohorts to uninstall and IPM URLs. (EXT-979)
- Exposed experiment assignments in the Public API. (EXT-991)

# 6.22.0 - 2025-06-10

- Update non-partner detection check
- Updated snippets to 2.2.0
- Add semver operator to be used in cohorts. (EXT-960)

# 6.21.2 - 2025-06-03

This release contains bugfixes and under-the-hood changes.

- Fixed a typo in the AdBlock debug data related to the total ping count.
- Fixed an issue with the display of text on the Customize tab of the AdBlock Option page with the dark theme enabled. (EXT-835)
- Fix Public API Main World script initialization.
- Store installation date in prefs. (EXT-959)
- Updated `EWE.start()` parameters to enable the cohorts engine. (EXT-946)

# 6.21.1 - 2025-05-27

This release contains only minor updates and under-the-hood changes.

# 6.21.0 - 2025-05-20

- Collect additional pageview metrics for specific requests. (EXT-951)
- Detect and collect if a user has ubo installed. (EXT-942)
- Introduce 'cookie banner' OPD. (GROW-58)

# 6.20.1 - 2025-05-13

This release contains some bugfixes and under-the-hood changes.

- Fixed a bug where previously-disabled filters that are readded would be still
  be considered disabled by the DNR rules subsystem but not by other parts of
  the engine, leading to inconsistent behaviour. (EXT-926)
- Detect and collect if a user has our ad blocking extensions installed (EXT-923)
- Enabled public api in the trusted iframe.
- Consider data collection opt-out when initializing Sentry

# 6.20.0 - 2025-04-29

This release removes the I don't care about cookies recommendation and also
contains some bugfixes and under-the-hood changes.

- Remove I don't care about cookies recommended list. (EXT-843)
- Fixed an issue with the block count being shown after a user allowlists a site (EXT-904)
- Updated snippets to 2.1.0
- Collect pageview metrics from specific domains. (EXT-921)
- Added the `EWE.experiments.getFlags()` in Content and UI APIs. (EXT-880)
- Fixed haven autoplay behaviour. (noissue)

# 6.19.0 - 2025-04-15

This release contains improvements to ongoing haven experiment as well as various bug fixes and under-the-hood improvements.

- Fixed various UI breakages that could occur if too many tabs are open.
- Updated the minimum supported version of Node to 22. Node 22 is the current
  LTS version of Node. This only affects code that runs in Node, such as build
  scripts. This does not affect extension code running in the browser. (EXT-778)
- Added privacy as premium, under an experiment flag (EXT-859)
- Fixed empty responses being forwarded to Main World by the Public API. (EXT-872)
- Added Sentry exception handling to the icon popup. (EXT-902)
- Fixed: Free distraction control filter list was no longer considered recommended.
- Phase 2 of haven experiment with info box (EXT-899)

# 6.18.0 - 2025-04-01

- Added experiment flag data to the information injected into our websites. (EXT-867)
- Added the `use_dynamic_url` property to entries under the `web_accessible_resources` key in AdBlock's manifest file (MV3 only). (EXT-871)
- Added a new event log message to the popup menu when a user subscribes to a filter list (EXT-878)
- Added split experiment data to event log requests. (EXT-865)
- Added the ability to retrieve an experiment flag from content/ui scripts. (EXT-877)
- Added experiment information to debug data. (no-issue)

# 6.17.0 - 2025-03-17

- Fixed branding on Firefox for the modal variant
- Fixed Haven experiment is active check
- Extend allowlisting public API to allow for any TLD+(x > 0) of the current hostname (EXT-770)

# 6.16.0 - 2025-03-12

- Fixed an issue with the Premium Sync feature
- Add Haven experiment with 3 variants (EXT-794)
- Remove leftover OPDs on pages that perform synthetic navigation (IM-216)

# 6.15.1 - 2025-03-04

This release contains bugfixes and under-the-hood changes.

- Fixed an issue with the Premium Sync feature
- Fixed an issue with attempting to remove a filter list subscription when the user wasn't subscribed
- Fixed an null response issue with the IPM server response
- Fixed an issue when an incognito tab isn't found
- Added Sentry exception handling to the options UI page (EXT-755)

# 6.15.0 - 2025-02-18

This release contains bugfixes and under-the-hood changes.

- Attempt to fix IPM initialization issue with split experiment (IM-175)
- Updated snippets to 2.0.0
- Fixed license check to run every 24h (EXT-746)
- Fixed an issue with the Pause on all tabs feature (EXT-782)
- Added support for Sentry logging (EXT-754)

# 6.14.2 - 2025-02-03

This release contains minor UI update and under-the-hood changes.

- Saving of downloaded filters to IndexedDB can now continue if the database was
  previously corrupted. (EXT-679)
- Removed unused code from the extension (EXT-668)
- Turn on Acceptable Ads by default on Firefox (EXT-750)

# 6.14.1 - 2025-01-21

This release contains minor UI update and under-the-hood changes.

- Fixed loading bug for the new free basic distraction control filter list

# 6.14.0 - 2025-01-20 (internal)

This release contains minor UI update and under-the-hood changes.

- Added new free basic distraction control filter list
- Removed machine learning snippets from extension (refs EXT-710)
- Updated webext-ad-filtering-solution to 1.23.1
- Updated minimum Chrome version to 79 for MV2 extensions
- Updated minimum Opera version to 66 for MV2 extensions
- Moved SDK types into the webext-ad-filtering-solution repo (EXT-662)

# 6.13.1 - 2025-01-07

This release contains only minor updates and under-the-hood changes.

# 6.13.0 - 2024-12-10

- Removed "Always allow ads on this site" from kebab menu (EXT-595)
- Added skeleton for public API inside custom iframe; the API is currently inactive (EXT-567)
- Remove the "console log test" split experiment. (EXT-612)
- Telemetry fetch errors are now sent to the production log server.
- Updated webext-ad-filtering-solution to 1.22.0
- Pass premium status and aa active in uninstall link (EXT-607)
- Updated snippets to 1.7.1
- Attached split experiments assignments data to uninstall URL (EXT-541).

# 6.12.0 - 2024-11-25

This release contains mostly under-the-hood changes.

- Refactored the telemetry fetch processing
- Updated webext-ad-filtering-solution to 1.19.0
- Add the "console log test" split experiment. This is to verify the integration
  of our new split experiments framework. (EXT-612)

# 6.11.1 - 2024-11-18

This release contains only minor updates and under-the-hood changes.

- Updated webext-ad-filtering-solution to 1.17.1
- Removed PubNub integration (EXT-544)

# 6.11.0 - 2024-10-30

This release contains only minor updates and under-the-hood changes.

- Updated webext-ad-filtering-solution to 1.17.0

# 6.10.0 - 2024-10-16

This update should reduce disk usage and contains minor updates.

- Updated the link to the source code on the support tab
- Added allowlisting events centered on privacy to help us improve the user experience
- Updated snippets to 1.7.0
- Updated webext-ad-filtering-solution to 1.16.0

# 6.9.3 - 2024-10-02

This release contains minor updates and attempts to fix an issue when no subscriptions are enabled (due to corrupted data).

- Updated webext-ad-filtering-solution to 1.15.0
- Attempt to fix issue when no subscriptions are enabled (due to corrupted data), restoring to default subscriptions (EXT-373)
- Allows querying the extension for basic information about the state of adblocker settings, by trusted partners using the correct credentials. (RL-110)
- Better ad wall is detected (EXT-333)
- Fixed outdated Help Center links (EXT-354)
- Updated snippets to 1.6.0

# 6.9.2 - 2024-09-25

This release contains only minor updates and under-the-hood changes.

- We no longer test the MV2 build of our extensions on Chrome 129 and later,
  since it disables MV2 extensions by defaults.

# 6.9.1 - 2024-09-18

- Updated snippets to 1.5.0, now AdBlock supports: `hide-if-canvas-contains`
- Added fallback mechanism for telemetry request
- Included sourcemaps in Manifest v3 Chromium builds

# 6.9.0 - 2024-08-28

- Updated webext-ad-filtering-solution to 1.12.0
- Fixed an issue with the metadata on allow listed rules created via the popup menu
- Fixed an issue with the YouTube Channel allow listing feature
- Continued the YouTube Ad Wall vs. Allowlist Uninstall User Test (Phase 2 & 3)

# 6.8.0 - 2024-08-14

- Changed the pause button to do 7-day smart allowlisting.
- Fix premium push notification prevention.
- Update webext-ad-filtering-solution to 1.11.0.
- Update snippets to 1.4.1.
- Fixed the 'received' event recording for IPM.

# 6.7.0 - 2024-07-31

- Update webext-ad-filtering-solution to 1.10.0
- Make messaging API usable in standalone JavaScript files

# 6.6.0 - 2024-07-17

- Updated AdBlock's name and description
- Moved the update of the kebob URL
- Updated isSelectorFilter function to ignore comment filers
- Removed VPN waitlist CTA
- Refactored initial telemetry logic
- Removed a check for the warning_removal subscription on MV3
- Updated the premium licensing server URL
- Added extension install timestamp to debug data
- Added new entries to locale files

# 6.5.0 - 2024-07-03

- Added new IPM deletion command
- Support user counting functionality
- Update @eyeo/snippets dependency to 1.4.0
- Fixed: Telemetry wasn't being sent due to Chrome bug
- Fixed: Filter lists weren't being updated on Manifest v3

# 6.4.0 - 2024-06-25

- “Learn More” button in new pop up menu does not append user ID to Premium page redirect
- Show number of ads blocked on AdBlock menu also hides Premium Filterlists
- YouTube Ad Wall vs. Allowlist Uninstall User Test
- Updated the extension engine dependency to 1.8.0
- Support CDP functionality
- Add special handling to allowlisting API for Softonic domains

# 6.3.0 - 2024-06-04

- Fixed an issue with the premium filter lists being turned off after migrating to MV3

# 6.2.0 - 2024-05-21

- Changed the default pause button functionality in the popup.
- Fixed premium filters tab not showing the updated subscription status
- Update @eyeo/snippets dependency to 1.3.0
- Add extension info before DOMContentLoaded
- Redesigned the popup menu

# 6.1.1 - 2024-05-17

- Updated the extension engine dependency to 1.6.1

# 6.1.0 - 2024-05-08

- Updated the extension engine dependency to 1.6.0
- Updated AdBlock's description in the English locale files

# 6.0.2 - 2024-04-30

- Show the /update page to let Firefox users know about AdBlock Premium

# 6.0.1 - 2024-04-24

- Modified the minimum chrome version to "124.0"

# 6.0.0 - 2024-04-23

- Fixed an issue in the beta_manifest.base.json file that caused the AdBlock extension to fail to load
- Improved the log message for command version mismatch error
- Initial release of a MV3 version of AdBlock

# 5.22.2 - 2024-04-09

- Updated minimum Chrome version to 124 for MV3 extensions
- AdBlock will no longer log an error when the tab ID isn’t found when closing a tab
- Fixed an issue with the YT Allow listing feature on Firefox
- Fixed an issue when saving excluded filters (an advanced user feature)
- Fixed Twitch channel allow listing in MV3 extensions
- Updated MV3 translations
- QA testers can now invoke some utlitilty functions on the background & SW scripts from the AdBlock Options page
- Updated the snippet dependency to 1.2.2

# 5.21.1 - 2024-04-04

- Show the /update page to let Firefox users know about AdBlock Premium

# 5.21.0 - 2024-03-19

- Open a new tab to inform Firefox users about AdBlock Premium
- Updated the URL opened when the 'create_tab' command is executed.  It now includes the block count.
- Updated the domains that the AdBlock information is injected into the DOM.
- Updated the AdBlock information that is injected to now include the:
    - block count
    - isPremium user indicator
    - extension version
    - the AdBlock device GUID

# 5.20.0 - 2024-03-12

- Disable all telemetry by default for all Firefox users
- Fixed an issue with the editing of custom rules while AdBlock is paused
- For MV3 users with custom subscriptions, we added a message on the Filter Lists tab that they are temporarily unavailable
- Removed duplicated calls to sendResponse
- Added additional subdomain command parameter for the create OPD command

# 5.19.3 - 2024-03-06

- Updated the rules dependency

# 5.19.2 - 2024-02-28

- Updated the rules dependency
- Updated the extension engine dependency to 1.2.4

# 5.19.1 - 2024-02-22

- Created an MV3 build for beta users
- Updated the rules dependency

# 5.19.0 - 2024-02-20

- Removed a duplicate message in the locale Swedish message file
- Removed unnecessary code that opens the first run page
- In preparation for migrating to manifest version 3, the following changes were made to AdBlock:
  - added migration error counts to the telemetry data
  - fixed an issue with the "Manage AdBlock settings from YouTube subscriptions page"
  - fixed the premium event messages listeners in an MV3 environment
- Updated the @eyeo/snippets dependency to 1.0.0

# 5.18.0 - 2024-01-31

- Added an option to opt out of the sending of telemetry
- AdBlock's premium filter lists can now use snippets
- Added two new language filter lists (Hungarian, and Global - Greek, Thai, Philippines, Malaysia, Croatian, Serbian, Slovenian, Bosnian)
- Updated EyeO webext-ad-filtering-solution dependency to 1.2.3 This update addresses the following issues:
  - Fixed an issue with the $document filters in iFrames
  - Added domain wildcard support for element hiding emulation filters.
  - Replaced subscriptions.getDownloadable() with subscriptions.getSubscriptions()
  - Replaced "Subscription.downloadable" property with "Subscription.updatable".
- Fixed an issue during extension initialization for browser languages without recommended filter lists
- Added logging of extension engine migration errors to the console
- Fixed an issue with the debug data when the Premium sync feature is not enabled
- Improved the YouTube channel allow listing feature; it now works in a MV3 / service worker environment
- Added platform+extension metadata to the query string when showing the `/install` page
- Added a new parameter to control the IPM "create_tab" command

# 5.17.2 - 2024-01-19

- Updated EyeO webext-ad-filtering-solution to version 1.1.3. This update addresses two issues:
  - Removed internal adblockpluscore dependency
  - Incorrect handling of first-party requests in third-party frames
- Show the /update page to let users know about AdBlock Premium

# 5.17.1 - 2024-01-15

- This release fixes a major performance problem that was introduced in AdBlock 5.17.0

# 5.17.0 - 2024-01-10

- Fixed an issue when trying to subscribe to the Premium filter lists in the manifest version 3 build of AdBlock
- Fixed an issue with the collection of the debug data when the Premium sync feature was enabled
- Fixed an issue with incorrect data in the Telemetry request
- Fixed an issue with the "Don't show me this message again" option on the AdBlock "hide an element" wizard
- Fixed an issue with element hide filter hits not being displayed in the AdBlock devtools tab
- In preparation for migrating AdBlock to manifest version 3, the following changes were made:
    - the Local CDN feature has been removed
    - the Premium Sync feature will now periodically check for setting updates
    - removed the Adblock Warning Removal filter list
- Improved the Premium image swap feature
- Added translations for the Premium Cookie Consent Cutter filter list
- To help with the automated testing process, a new message handler was added to get the ready state of the extension
- Users with the browser language set to either Uzbek or Kazakh will now automatically be subscribed to the Russian & Ukrainian filter list
- Updated EyeO webext-ad-filtering-solution to version 1.1.1
- Updated the test URLs and docker image version in the CI script for AdBlock
- Moved several aliased files into adblockplusui directory
- Reverted the changes to the license text file

# 5.16.0 - 2023-12-11

- Show the /update page to let users know about AdBlock Premium
- In preparation for manifest V3, and to help us better understand how our users use AdBlock, we've added custom filter metadata counts to the ping data
- Added the Cookie Consent Cutter premium filter list
- Added two new language-specific filter lists - Japanese and Turkish
- Added temporary debug IPM event messages for the create_tab command

# 5.15.0 - 2023-11-26

- Show the /update page to let users know about AdBlock Premium
- Added telemetry (with an option to opt-out) data to gauge how many of our users are affected by the YouTube ad wall
- Removed temporary IPM code that ignores certain commands for certain users
- Updated the Node dependency to 18.17
- Updated the GitLab code owners file
- Added a lint step to the GitLab CI/CD script

# 5.14.0 - 2023-11-13

- Show the /update page to let users know about AdBlock Premium
- Fixed an issue with the block count parameter in the IPM request

# 5.13.0 - 2023-10-30

- Show the /update page to let users know about AdBlock Premium
- Updated the Snippet dependency to 0.10.0
- Fixed an issue with the premium sync feature not synchronizing custom rules
- Removed the temporary code that removed the IPM 'create tab' commands
- Removed the unused `custom-subscriptions.json` file
- Fixed an issue with IPM command statistics being reset on extension start-up

# 5.12.0 - 2023-10-16

- Show the /update page to let users know about AdBlock Premium
- Fixed an issue with the Premium Image Swap feature
- Fixed an issue with the AdBlock toolbar icon incorrectly showing as allowlisted when ad blocking is active
- Fixed an issue with on-page dialog in the Opera search results page
- Fixed an issue on the AdBlock Options page incorrectly showing advanced options when the page is manually reloaded
- Added the 'license' parameter to the IPM request, and now include it when processing IPM commands

# 5.11.0 - 2023-10-08

- Fixed a race condition that could occur with tab-session storage
- Added temporary debug IPM event messages
- Updated the Snippet dependency to 0.9.0
- Updated the eyeo's Web Extension Ad Blocking Toolkit to version 0.10.1
- Added a new machine learning dependency
- Removed the September 2023 campaign code
- Added a webpack alias
- Added the IPM data to the debug data

# 5.10.1 - 2023-09-18

- Show the /update page to let users know about AdBlock Premium
- Added code to remove any un-processed In Product Messages (IPMs)
- Fixed an issue with AdBlock Premium on a MV3 build
- Added an alias to the build script

# 5.10.0 - 2023-09-06

- Updated the eyeo's Web Extension Ad Blocking Toolkit to version 0.9.0
- Replaced the vendor/webext-sdk git submodule with @eyeo/webext-sdk npm package
- Updated the eyeo snippets dependency to 0.8.1
- Updated the create_on_page_dialog command; added a `domain_list` parameter
- Added the command name and version to IPM event object request
- Changed the IPM versioning from command library level to command level
- Removed the adblockplusui git dependency; added a copy of the required adblockplusui files in their own directory
- Fixed an issue with the contact link in the AdBlock help flow
- Fixed an issue with the allowlist and hiding wizards showing multiple a CTA times
- Updated the AdBlock configuration files to remove an unnecessary steps

# 5.9.0 - 2023-08-02

- Added a new IPM command to open a new tab
- Updated the Distraction Control options page tab
- Added the new, combined Distraction Control filter list
- Fixed an error that occurred during the sending of the telemetry request
- Added support for a Manifest V3 (MV3) compliant build of AdBlock
  - Fixed the MV3 beta build process
  - Updated the AdBlock popup menu work in an MV3 environment
  - Integrated static filter lists for MV3
  - Fixed the AdBlock icon block counter
  - Updated the trigger mechanism that opens the first run page
  - Added support for the new, MV3 specific execute script API
  - Fixed context menus in an MV3 environment
  - Added a new `isPinned` parameter to the telemetry request
  - Removed the obsolete AdBlock custom filter list
- Upgraded the adblockpluscore dependency to 0.11.0
- Upgraded the webext-SDK dependency to 0.8.1
- Updated the CI script to run tests on the Edge browser
- Added the missing variables in the CI script
- Updated the CI script to run tests on the MV3 builds in the CI scrip

# 5.8.1 - 2023-07-20

- Updated the bundled Snippets library to 0.7.0

# 5.8.0 - 2023-06-29

- Fixed an issue with the initialization of the uninstal URL
- Updated the telemetry data that is sent to the in-product messaging (IPM) server
- Added support for a new on page dialog
- Continue to show the /update page to let users know about AdBlock Premium

# 5.7.0 - 2023-06-09

- Updated the bundled Snippets library to 0.6.2
- Fixed an issue with the AdBlock toolbar icon incorrectly showing "NEW"
- Updated the extension for Premium users so that web based allow listed rules are removed

# 5.6.0 - 2023-05-01

- Continue to show the /update page to let users know about AdBlock Premium
- Provide experimental Flattr API to some websites
- Expanded partner access to experimental allowlisting API

# 5.5.0 - 2023-04-14

- Show the /update page to let users know about AdBlock Premium
- Added sending telemetry data to a new in-product messaging (IPM) server
- Added a new query string parameter to the un-install page which will provide information on whether the user has used the experimental allowlisting feature

# 5.4.2 - 2023-02-21

- Added a consent dialog when a user enables the AdBlock Premium Sync feature (only for Firefox users)

# 5.4.1 - 2023-02-12

- Fixed the on click event handler for the "Upgrade your AdBlock" CTA in the AdBlock popup menu
- Show the /update page to let users know about AdBlock Premium

# 5.4.0 - 2023-02-02

- Modified or updated several JavaScript modules to work in a service worker environment in preparation for migration to manifest V3.
  The modified modules include:
  - survey & on page icon
  - telemetry
  - anonymous filter list data collection
  - ad blocking statistics ('Stats')
- We also updated the following in preparation for migration to manifest V3
  - the AdBlock Options page to use message passing
  - created a new common utilies module for use within a service worker
- Updated several dependencies used within AdBlock:

  - snippets to 0.6.0
  - adblockplusui to 3.16
  - web ext SDK to 0.7.2

# 5.3.3 - 2022-12-19

- Stop opening the /update page to let users know about AdBlock Premium
- Added the Crotian locale to update an old Chrome web store Crotian listing

# 5.3.2 - 2022-11-18

- Show the /update page to let users know about AdBlock Premium

# 5.3.1 - 2022-11-16

- Fixed an issue with the sending of telemetry
- Fixed an issue with the format of data being sent to the backup log server
- Stop showing the /update page to let users know about recent changes to AdBlock
- Updated the License information, git configuration, and README files

# 5.3.0 - 2022-10-21

- Fixed an issue with the Premium Sync feature
- Added a backup IP address telemetry process that will be used in case of a network issue
- Updated the eyeo web ext SDK to version 0.5.0
- In preparation for Manifest V3, the following changes where made:

  - converted modules that use the setTimeout & setInterval function to use the Alarm API
  - removed references to local storage, and instead use the extension storage API
  - removed any reference to jQuery in background scripts
  - converted AJAX requests to use the Fetch API
  - removed ability to subscribe to custom filter lists

# 5.2.0 - 2022-10-10

- Show the /update page to let users know about recent changes to AdBlock

# 5.1.3 - 2022-10-07

- Stop showing the /update page to let users know about the new AdBlock VPN

# 5.1.2 - 2022-09-06

- Show the /update page to let users know about the new AdBlock VPN

# 5.1.1 - 2022-08-29

- Replaced the abp-snippets git submodule with the @eyeo/snippets npm package and upgraded it to 0.5.2
- Cleaned up and fixed a couple of issues with the AdBlock package.json file

# 5.1.0 - 2022-08-22

- Removed the 'social media' links on the AdBlock Options page when the user is subscribed to the Anti Social Filter list
- Fixed an issue on the AdBlock Bug Report page with the 'steps' field not highlighted when left blank
- Fixed an issue with a missing error message when a user would edit their custom filters on the Customize tab of the AdBlock Options page
- Fixed an issue with anonymous filter list usage data incorrectly determining the filter list subscriptions for a filter list rule
- Updated the AdBlock On Page icon

# 5.0.5 - 2022-08-16

- Fixed an issue with telemetry possibly being sent prior to initialization being complete
- Updated the Snippets library to version 0.4.1

# 5.0.4 - 2022-07-15

- Fixed an issue with a missing entry in the locale messages file

# 5.0.3 - 2022-07-15

- Fixed a performance issue in the anonymous data collection, and image swap feature

# 5.0.2 - 2022-06-28

- Fixed an issue in the release build script
- Updated to the new eyeo ad blocking SDK.
- Updated translations

# 4.46.2 - 2022-05-15

- Continue to show /update page for those users that haven't seen the Spring 2022 update

# 4.46.1 - 2022-05-02

- Continue to show /update page for those users that haven't seen the Spring 2022 update

# 4.46.0 - 2022-04-18

- Added a AdBlock popup menu message about the AdBlock VPN
- Show the /update page to let users know what features have been updated in the last 6 months.
- Added checks to enhance content script messages security

# 4.44.0 - 2022-03-07

- Removed the logic to show the "New" badge text on extension update
- In preparation for manifest V3, and to help us better understand how our users use AdBlock, we've added

  - AdBlock Options Page Telemetry
  - filter list subscription information to the ping data

# 4.43.0 - 2022-01-25

- Fixed several issues on the AdBlock popup menu
- Removed the CryptoCurrency BitCoin Mining Protection filter list from the list of subscriptions added for new users
- Continue to show the message about Distraction Control on the AdBlock popup menu

# 4.42.0 - 2022-01-03

- Added a AdBlock popup menu message about Distraction Control
- Improved the Distraction Control help flow
- Made some minor improvements to the Distraction Control tab on the AdBlock options page
- Removed the functionality to open the /update page

# 4.41.0 - 2021-12-10

- Continue to show /update page for those users that haven't seen the Fall 2021 update
- Added a CTA to notify our users about the AdBlock VPN
- Updated the bundled Snippets library to 0.3.2

# 4.40.0 - 2021-11-11

- Continue to show /update page for those users that haven't seen the Fall 2021 update
- For our AdBlock Premium users, the extension will now add an flag to our website to let the website know the visitor is a premium user
- Updated the URL that's opened for the VPN CTA on the AdBlock Options page
- In preparation for manifest V3, and to help us better understand how our users use AdBlock, we've added custom rule counts to the telemetry (ping) data
- Added an Email CTA to the AdBlock Options page
- Added host permissions information to the "debug" data available on the Support tab of the AdBlock Option page

# 4.39.1 - 2021-10-25

- Show the /update page to let users know what features have been updated in the last 6 months.

# 4.38.0 - 2021-10-11

- Added Distraction Control for AdBlock Premium users

# 4.37.0 - 2021-09-27

- Fixed an issue when printing in Chrome with AdBlock enabled
- Fixed an issue with the Premium Sync feature
- Fixed an issue with the 'Submit Feedback' button
- Fixed an issue with the 'New' Badge text showing on blank or empty tabs
- Updated the minimum Chrome version to 60
- Fixed an issue with Nordic language filter list incorrectly in the language dropdown on the Filter list tab of the AdBlock Options page
- Fixed an issue with AdBlock double counting some blocked items

# 4.36.0 - 2021-09-08

- Updated the bundled Snippets library

# 4.35.0 - 2021-08-11

- Fixed an issue with the advanced mode of the hiding wizard
- Updated the bundled Snippets library

# 4.34.0 - 2021-06-21

- Updated translations
- Fixed an issue with anonymous data collection sending data URLs
- Fixed an issue with the edit mode of the hiding wizard
- Removed the functionality to open the /update page
- Updated to ABP Core 3.11

# 4.33.0 - 2021-04-30

- Updated Translations
- Improved the layout of the AdBlock menu and options pages for right to left languages such as Arabic and Hebrew
- Fixed the color of hyperlinks on the AdBlock menu
- Continue to show /update page for those users that haven't seen the Spring 2021 update

# 4.32.0 - 2021-04-04

- Show the /update page to let users know what features have been updated in the last 6 months.

# 4.31.0 - 2021-03-31

- Updated Translations
- Fixed and improved the hiding wizard
- Fixed an issue with the YT Manage Subscription page
- Fixed an issue with YT Channel allowlisting feature interfering with snippets
- Updated the FanBoy Annoyances filter list URL

# 4.30.0 - 2021-03-17

- Updated Translations
- For AdBlock Premium users, we've added the ability to delete any synchronized devices
- For AdBlock Premium users, we've improved the performance of the image swap feature
- Fixed an issue with new the Gulp build process
- Enhanced the ability of AdBlock to be tested via automation

# 4.29.2 - 2021-02-26

- Improved a content script related to the manipulation of browser requests

# 4.29.1 - 2021-02-25

- Fixed an issue with minimum Firefox version in the manifest file

# 4.29.0 - 2021-02-24

- Added a link to the AdBlock ProductBoard page to the AdBlock Options page on the Support tab
- Fixed an issue when importing rotated images into the custom Image Swap feature
- Updated the Twitch specific content script so that streaming ads should no longer shown
- Removed the Malware Protection filter list from the AdBlock Options page since it is no longer available
- Removed the legacy AdBlock Premium extension migration functionality
- Updated the minimum version of Firefox to 63
- Updated the bundled 3rd party libraries within AdBlock
  - jQuery is now 3.5.1
  - DOM Purify is now 2.2.6
  - Chart JS is now 2.9.4
- Fixed an issue when the extension was notified that a premium user's license expired and left the sync feature partially enabled
-
- Fixed an issue with filter list data collection process sending data URLs (very long strings of data)

# 4.28.6 - 2021-02-23

- Fixed a performance issue with the Stats and data collection functions

# 4.28.5 - 2021-02-10

- Added missing entries to the 'no' locale message file

# 4.28.4 - 2021-02-10

- Fixed an issue with the new build process

# 4.28.3 - 2021-02-08

- Updated to ABP Core 3.10.2

# 4.27.0 - 2021-01-14

- Updated the Support tab on the AdBlock Options page
- Fixed an issue with our email address in the popup menu help flow

# 4.26.0 - 2021-01-05

- Updated the AdBlock popup menu

# 4.25.1 - 2020-12-16

- Fixed an issue with missing messages in the locale files

# 4.25.0 - 2020-12-14

- Fixed an issue in the data collection content script
- Removed the functionality to open the /update page

# 4.24.1 - 2020-11-19

- Continue to show the /update page to users that have not seen it. The /update page lets users know what features have been updated in the last 6 months.
- Fixed an issue with the Stats / charting feature in AdBlock incorrectly processing blank hostnames.

# 4.24.0 - 2020-10-28

- Added 4 new image categories to the Premium Image Swap feature
- Continue to show the /update page to users that have not seen it. The /update page lets users know what features have been updated in the last 6 months.
- Fixed an issue with the buttons on the AdBlock Options page not set to the correct font family
- Removed code that was associated with the AdBlock Protect extension
- Refactored the code so that it now we following the standard naming convention
- Refactored the code to remove the warning for synchronous AJAX requests

# 4.23.0 - 2020-10-09

- Show the /update page to let users know what features have been updated in the last 6 months.

# 4.22.1 - 2020-10-06

- Improved streaming ad blocking on Twitch

# 4.22.0 - 2020-09-24

- Updated translations
- Updated / fixed a few of the themes colors
- Updated DOM Purify to version 2.0.15
- Updated to ABP Core 3.9.5
- Removed the 'onUpdate' logic added for the YouTube Subscribed Channel Allowlist feature
- Added a AdBlock Premium status indicator to the AdBlock popup menu and options page
- Fixed an issue with the YouTube Channel Allowlist feature

# 4.21.0 - 2020-09-17

- Fixed an issue when subscribing to a filter list via a subscription link
- Updated the Hungarian filter list URL
- Updated to ABP Core 3.9.4
- Fixed an issue when showing status messages on the AdBlock Options page
- Added the "I don't care about cookies" filter list to the Filter List tab of the AdBlock Options page
- Fixed an issue with Local CDN feature
- Removed the Local CDN feature from our Firefox extension

# 4.20.0 - 2020-09-02

- Added a new feature which allows users to easily add or remove their YouTube subscribed channels to the AdBlock allowlist

# 4.19.0 - 2020-08-10

- Fixed an issue with 'hide an ad' wizard when trying to hide certain ads with very long text
- The AdBlock popup menu has been enhanced to allow a tab id to be provided in a query string. This will allow us to improve our automated testing.
- Added Twitch 'channel' allow listing and improved ad hiding on Twitch on channels which are not allow listed.

# 4.18.0 - 2020-07-28

- Updated to ABP Core 3.9.3

# 4.17.0 - 2020-07-22

- Added processing to migrate legacy AdBlock Premium users data to the new data structures

# 4.16.0 - 2020-07-18

- Updated to ABP Core 3.9.1

# 4.15.0 - 2020-06-29

- Updated translations
- Removed the functionality to open the /update page
- Improved the hiding wizard. It now allows a user to restart the 'hide an element' flow.
- Fixed an issue with the YouTube channel allow ads feature. The AdBlock toolbar icon correctly displays the ad blocking status.
- For Edge users, a "Rate Us" link has been on the AdBlock Options page
- The extension now correctly identifies the stable Edge version in the AdBlock debug data
- Added aria labels and roles to the social media icons on the AdBlock Options page
- Added the AdBlock development servers to the bandaid code
- Removed unused code and references to a 'getadblock question'

# 4.14.0 - 2020-06-10

- Added Aria labels to the social media icons on the AdBlock Options page
- Added two new 'getadblock.com' development hostnames to the 'bandaids' content script
- Added the stable MS Edge, and Firefox extension ids so that the debug data logic correctly identifies the extensions as 'stable'
- Removed unused code from the 'bandaids' content script

# 4.13.0 - 2020-06-04

- Added the AdBlock "on page" icon
- Removed the unused 'notification' and 'overlay' survey types
- Added a 'referrer-policy' of 'no-referrer' to the image tag used for the Premium image replacement / swap
- Continue to show the /update page to users that have not seen it. The /update page lets users know what features have been updated in the last 6 months.
- Fixed an issue with the 'Add Filter List Subscription' via link click functionality
- Fixed an issue with the element highlighter in the 'Block an ad on this page' wizard
- Removed the Romanian filter list
- Updated translations

# 4.12.0 - 2020-05-18

- For Premium users, we've added functionality to allow you to import your own images / photos into AdBlock to be used for image swap.
- Added a debug message when an error is detected from the PubNub library
- Fixed two issues which occur on older versions of Chrome (version 65)
- Fixed an issue that was introduced in the new managed storage option (AdBlock version 4.11.0)
- Continue to show the /update page to users that have not seen it. The /update page lets users know what features have been updated in the last 6 months.

# 4.11.0 - 2020-04-15

- Added new managed storage / group policy options

# 4.10.0 - 2020-04-06

- Updated translations
- Show the /update page to let users know what features have been updated in the last 6 months.

# 4.9.0 - 2020-03-31

- Added ad blocking statistics to the AdBlock Options page

# 4.8.0 - 2020-03-16

- Updated to ABP Core 3.8

# 4.7.4 - 2020-03-06

- Fixed an issue in the MS Edge user data migration code

# 4.7.3 - 2020-03-04

- Removed debug statements in the MS Edge user data migration code
- Fixed a bug in the survey logic

# 4.7.2 - 2020-03-03

- Added debug statements to the MS Edge user data migration

# 4.7.1 - 2020-02-28

- Fixed an issue with Firefox user data migration

# 4.7.0 - 2020-02-27

- Updated the PubNub bundled library to version 4.27.2
- Added logic migrate Firefox users data from the legacy data structures to new data structures (Firefox Only)
- Updated the DOMPurify bundled library with the binary compatible version
- Improved the Twitch hiding bandaid

# 4.6.0 - 2020-02-19

- Updated translations
- Fixed an issue with the whitelist filter that's created on the 'Don't run on this page' AdBlock menu option
- Removed references to the background page on the popup menu
- Fixed an issue in the help flow
- Fixed an issue when subscribing to a new filter lists with multiple AdBlock Option pages opened
- Added support for Mozilla / Firefox to the wizards, and telemetry data
- Added a new parameter to the telemetry data to indicate if Chrome users have modified the default hosts that AdBlock runs on
- Fixed an issue with users unable to de-select the 'Advanced' option on the General tab of the AdBlock Options page
- Updated the URLs used for Premium feedback
- Added tooling to help us maintain our current level of accessibility
- Modified the AdBlock logo / icon in the AdBlock menu to now open the AdBlock homepage
- Added a 'Rate Us' link to the AdBlock options page

# 4.5.0 - 2020-01-31

- Updated translations
- Consistently use 'browser._' instead of 'chrome._' for extension APIs
- Updated the bundled version of jQuery to 3.4.1
- Corrected the 'report an ad' link in the help flow
- Converted all CSS url links to use the absolute path, instead of a relative path
- All dynamically created HTML is now sanitized using DOMPurify

# 4.4.0 - 2020-01-16

- Updated translations
- Fixed an issue with blank AdBlock notifications
- Fixed errors that would be shown when the browser was started or AdBlock was installed
- Fixed an error related to the user opt in data collection processing
- Fixed an issue with the URL missing in the AdBlock tab of the Chrome developer tools
- Added functionality to update the AdBlock badge text to "New" 7 days after installation

# 4.3.1 - 2019-12-30

- Updated translations
- Added processing to migrate legacy Edge users data to the new data structures
- Fixed an issue with viewing debug data on the AdBlock Options page
- Modified the ping parameter 'flavor' for Edge users

# 4.2.0 - 2019-12-18

- Updated translations
- Fixed a couple of issues with the Solarized Dark theme
- Improved the accessibility on the recently added help flow
- Fixed an issue with the AdBlock logo on the AdBlock Options page in Chromium Edge
- Updated to ABP Core 3.7

# 4.1.0 - 2019-12-11

- Updated translations
- Fixed an issue with an empty 'alt' attribute on a image on the AdBlock Options page
- Fixed an issue when sending the AdBlock popup help flow log message
- Fixed an issue with enabling the YouTube channel whitelisting feature on the AdBlock Options page
- Updated the 'Learn More' link on Sync tab of the AdBlock Options page
- Added several users messages regarding the new AdBlock Premium feature
- Fixed an issue with the Acceptable Ads Privacy setting not being in sync between the General and Filter Lists tabs on the AdBlock Options page
- Removed unused translation messages and message files

# 4.0.2 - 2019-12-05

- Updated translations
- Updated the Twitch pre-roll ad muting and hiding logic in bandaids

# 4.0.1 - 2019-11-26

- Updated translations
- In the 'bandaid' logic for getadblock.com, the addition of the message handler listener was modified to not be dependent on the load event.
- Added a log message when the extension is updated

# 4.0.0 - 2019-11-24

- Updated translations
- Added logic to enroll all (new and existing) users in AdBlock Premium
- Added a limit of 2 to the image replacements attempted on Facebook, as is done on other sites
- Removed AdBlock Premium test code
- Minor style modifications the AdBlock popup menu and the AdBlock Options pages
- Added preventative logic to the translation framework

# 3.62.0 - 2019-11-19

- Updated translations
- Changed all references from MyAdBlock to Premium
- Updated references to deprecated extension APIs
- Fixed an issue with the 'Update' button on the Filter List tab of the AdBlock Options page
- Fixed an error with `isNaN` usage when processing ping server responses
- Added meta tags to all extension HTML documents
- Fixed an issue when un-subscribing to EasyList on the Filter List tab of the AdBlock Options page
- Updated the Premium Sync options page
- Fixed the YouTube channel whitelisting feature
- Removed the 'MyAdBlock' options menu item in the AdBlock popup menu

# 3.61.1 - 2019-11-08

- Updated translations
- Updated the extension name and short description

# 3.61.0 - 2019-11-06

- Updated translations
- Updated the extension name and short description
- Updated the Image Swap and Theme options pages
- Removed the obsolete Danish filter list
- Fixed an issue on the Customize tab with error messages
- Removed the unused MyAdBlock call to actions to the AdBlock popup menu

# 3.60.0 - 2019-10-20

- Updated translations
- Show the /update page to let users know what features have been updated in the last 6 months.

# 3.59.0 - 2019-10-17

- Updated translations
- Added a new help feature to the AdBlock popup menu
- Updated the 'should show tab' survey logic. There is now a check to see if the user should be enrolled in MyAdBlock.
- Fixed a typo in a comment (jspeed-meyers)
- Fixed three small bugs on the Filter List tab of the AdBlock Options page

# 3.58.0 - 2019-10-11

- Updated translations
- Improved the accessibility of the AdBlock pop-up menu and option pages.

# 3.57.0 - 2019-10-02

- Updated translations
- Fixed an error in the popup menu error handling process
- Removed old, unnecessary code for older versions of Chrome (less than Chrome version 53)
- Fixed an issue when saving the "disabled" filters on the Customize tab
- Improved the error handling process for the MyAdBlock Sync feature
- Fixed an error when saving Sync'd themes
- Added element hiding exception rules to user opt in data collection processing
- Formatted two CSS files that were initially missed

# 3.56.0 - 2019-09-30

- Updated translations
- Updated the MyAdBlock dashboard page and the related popup menu item

# 3.55.1 - 2019-09-17

- Fixed an issue with the initial 'ping' not occurring for 55 minutes

# 3.55.0 - 2019-09-17

- Updated Translations
- Linted and formatted the JavaScript, HTML and CSS files.

# 3.54.0 - 2019-08-28

- Added new MyAdBlock call to action to the AdBlock popup menu
- Improved the keyboard accessibility of the AdBlock popup menu
- Fixed an issue with the AdBlock popup menu taking users to the incorrect MyAdBlock options page
- Added a request for feedback on the AdBlock Options page for MyAdBlock users
- Update Translations

# 3.53.0 - 2019-08-23

- Updated to ABP Core 3.6.3

# 3.52.1 - 2019-08-14

- Updated Translations
- Added the Acceptable Ads Privacy filter list
- Fixed a security issue in the 'bandaid' processing on getadblock.com
- Fixed an issue on the Customize tab of the AdBlock Options page
- Further improvements to the 'MyAdBlock' image replacement functionality

# 3.51.1 - 2019-08-07

- Fixed a few issues in the 'MyAdBlock' image replacement functionality
- Fixed an issue on the AdBlock Option page not showing the translation credits widget
- Added a new data sync feature for MyAdBlock users
- Updated translations

# 3.50.1 - 2019-07-30

- Improved the 'MyAdBlock' image replacement functionality
- Refactored the call to the `getSettings` function
- Added a new option to hide ads on Twitch
- Improved / refactored the blacklist / hiding wizard to show correctly on all web sites, removed jQuery UI
- Updated translations

# 3.49.1 - 2019-07-05

- Improved / modified the AdBlock options page
- Added new themes for the AdBlock menu

# 3.49.0 - 2019-07-05

- Updated translations
- Removed the functionality to open the /update page
- Updated the Norwegian filter list URL
- Improved (Refactored) the whitelist wizard to show correctly on all web sites

# 3.48.0 - 2019-05-28

- Updated translations
- Fixed an issue with the AdBlock tab in the Chrome developer tools
- Added Edge detection logic to the telemetry data
- Updated the icons, including the inclusion of the material design icons
- Changed the tab functionality on the AdBlock Options page to a menu style layout
- Fixed a JavaScript error in the user enabled filter list data collection processing

# 3.47.0 - 2019-05-20

- Removed unused files from the build
- Updated the ping processing to include parameters as to which Theme the user has enabled
- Removed duplicate log server messages
- Updated the 'MyAdBlock' message in the popup menu
- Update translations

# 3.46.0 - 2019-04-22

- Show the /update page to let users know what features have been updated in the last 6 months.

# 3.45.0 - 2019-04-22

- Updated to ABP Core 3.5.1
- Updated translations

# 3.44.0 - 2019-04-12

- Added white or dark theme to option page and/or pop-up menu. Theme selection can be found on the AdBlock Option page.
- Updated the ping processing to include an indicator if the user has YouTube whitelisting enabled or disabled.
- Added the AdBlock version number to log messages.

# 3.43.0 - 2019-04-08

- Updated to ABP Core 3.5.1

# 3.42.0 - 2019-03-21

- Updated the look and layout of the AdBlock Options page
- Added a channel name cache to reduce the of number YT API calls
- Cleaned up, and removed old, unused Safari logic
- Added the Lato font files to the extension, and changed the AdBlock popup menu, and Options pages to use the new font

# 3.41.0 - 2019-02-22

- Added error handling to the popup menu

# 3.40.1 - 2019-02-14

- Change the default values for MyAdBlock so that only a cat is initially selected

# 3.40.0 - 2019-02-12

- Updated the look and layout of popup menu
- Moved the MyAdBlock options page to a new tab on Options page

# 3.39.1 - 2019-02-06

- Updated translations
- Added logic to show a message about the new AdBlock Protect extension to some users

# 3.38.1 - 2019-01-29

- Fixed a typo in the extension description

# 3.38.0 - 2019-01-28

- Updated to ABP Core 3.4.3
- Fixed an issue when starting AdBlock and AdBlock had been paused when the browser was closed.

# 3.37.0 - 2019-01-15

- Updated translations
- Updated YouTube Channel whitelisting feature so that the content script no longer make direct requests to the YT API as described here:
  https://sites.google.com/a/chromium.org/dev/Home/chromium-security/extension-content-script-fetches

# 3.36.0 - 2018-12-10

- Updated translations
- Updated 'bandaids' processing to help block ads on certain web sites.

# 3.35.0 - 2018-12-03

- Updated translations
- Updated & improved the look of the AdBlock popup menu
- Changed the AdBlock menu item - "Report an ad on this page" to "Troubleshoot an ad". This menu item now opens a KB article.
- Updated the AdBlock bug report page to use V2 of the FreshDesk API.
- Updated the AdBlock logging API to V2
- The missed local CDN statistics are now only sent when there is something to send
- Fixed the vertical position of the social links in header on the AdBlock options page
- Added the Norwegian language filter list
- Updated the help links of the Swedish and Korean filter lists
- Changed the URLs of the Finnish, Danish, Romanian and Icelandic language filter lists from HTTP to HTTPS

# 3.34.0 - 2018-10-09

- Updated translations
- Added a keyboard shortcut for toggling the pause feature. (#323)
- Added pause / unpause to the AdBlock context menu. (#326)
- Show the /update page to let users know what features have been updated in the last 6 months. (#325)

# 3.33.1 - 2018-09-17

- Updated translations
- Updated to ABP Core 3.3.1 (#320)

# 3.32.1 - 2018-07-25

- Updated translations
- Updated to the full release of ABP Core 3.2 (#320)

# 3.32.0 - 2018-07-18

- Updated translations
- Updated to ABP Core 3.2 (#317)

# 3.31.2 - 2018-06-13

- Updated translations
- Updated to ABP Core 3.1+ (#308)

# 3.30.1

- Updated translations
- Made minor changes to the style and layout of the AdBlock popup menu. (#310)
- Removed the /update logic. (#309)

# 3.29.3

- Updated the logic for passing messages between AdBlock and getadblock.com. (#307)

# 3.29.2

- Removed the externally_connectable entries from the manifest to reduce the number required permissions for AdBlock. (#306)

# 3.29.1

- Updated translations
- Added the 'MyAdBlock' image replacement feature. (#285)

# 3.28.0

- Updated translations
- Added 'Help and Feedback' and remove the 'what's this' link on the AdBlock pop up menu. (#301)
- Updated the /update logic to only open the new tab for users upgrading from AdBlock versions less than 3.27.0. (#302)

# 3.27.1

- Updated translations
- Fixed an issue with the local CDN feature. (#300)

# 3.27.0

- Updated translations
- Show the /update page to let users know what features have been updated in the last 6 months. (#296)

# 3.26.1

- Updated translations
- Fixed an issue with missing separators on the AdBlock popup menu. (#298)

# 3.26.0

- Updated translations
- Added a new 'Pause on this site' menu item on the AdBlock popup menu. (#293)
- Updated the Cryptocurrency (Bitcoin) Mining Protection List URL. (#295)
- Removed obsolete AdBlock popup menu items. (#294)

# 3.25.3

- Updated translations
- Added the local CDN feature. (#290)
- Improved the performance of a common URL parsing function. (#291)

# 3.24.0

- Updated translations
- Updated the tab survey logic to check the 'state' of the computer prior to opening a tab. (#289)
- Updated the ping data to include an indicator that is set to true if the user has opted in to filter list data collection. (#288)

# 3.23.0

- Updated translations
- Updated 'bandaids' processing to help block ads on certain web sites. (#286)
- Updated to ABP Core 1.13.5 (#287)

# 3.22.1

- Added the logging of the opening of AdBlock options page. (#283)

# 3.22.0

- Updated translations
- Updated the logging of user selections in the AdBlock popup menu. (#282)
- Updated the CSS style entry for the text elements that are italicized in the white-list and black-list wizards to avoid style issues. (#281)

# 3.21.0

- Removed the menu option for a user survey. (#280)
- Updated the logic for the optional filter list data collection to include hiding filters. (#279)
- Updated translations

# 3.20.0

- Updated 'bandaids' processing to help block ads on certain web sites. (#278)
- Updated translations

# 3.19.1

- Fixed an issue with the 'Enable AdBlock on this page' AdBlock menu item. (#277)

# 3.19.0

- Updated translations
- Updated to ABP Core 1.13.4 (#275)
- Added a menu option for a user survey. (#276)

# 3.18.0

- Updated translations
- Removed /update logic. (#272)
- Fixed an issue with the pause feature. (#269)
- Added a new filter list that blocks Crypto-currency mining scripts. (#273)
- Updated 'bandaids' processing to help block ads on certain web sites. (#274)

# 3.17.0

- Updated translations
- Show the /update page to non-English users that did not see the 3.16 update. (#265)
- Fixed a typo in the unsubscribe warning cookie on the Filter Lists tab of the AdBlock options page. (#267)

# 3.16.0

- Fixed an issue with the 'pause' feature. (#262)
- Updated translations
- Updated the success message on the the Bug Report page. (#242)
- Removed Safari specific messages that are no longer used. (#236)
- Fixed an issue with some of the language filter list subscriptions that do not use the combined EasyList lists. (#188)
- Fixed an is use with the "undo my blocks on this domain" menu refreshing the wrong tab. (#243)
- Updated 'bandaids' processing to help block ads on certain web sites. (#250)
- Fixed an issue with the YouTube white-list channel feature (#244)
- Removed unnecessary code on the Customize tab. (#184)
- Removed the language specific filter list - Liste AR & EasyList, and will use Liste AR + Liste FR + EasyList instead. (#196)
- Added the locale to the /installed query string to help show the page in the correct language. (#260)
- Added a warning message to the Filter Lists tab on the Options page when the user un-subscribes to EasyList and / or all filter lists. (#259)
- Fixed the warning message on the Filter Lists tab on the Options page when the user subscribes to several filter lists. (#259)
- Changed all hard coded links in AdBlock from HTTP to HTTPS (SSL) (when possible). (#261)
- Show the /update page to non-English users. (#264)

# 3.15.0

- Updated Translations.
- Updated 'bandaids' processing to help block ads on certain web sites. (#235)
- Updated to ABP Core 1.13.3 (#235)
- Fixed the link to our documentation about block counts. (#235)
- Removed an obsolete test module. (#235)
- Removed obsolete code related to version check. (#235)
- Fixed an issue with the updated localized messages on the 'Report an Ad' page. (#235)

# 3.14.0

- Updated Translations.
- Updated 'bandaids' processing to help block ads on certain web sites. (#237)
- Added the injection of the AdBlock unique id into JavaScript memory space on getadblock.com sites. (#237)

# 3.13.0

- Updated Translations.
- Removed HTML tags from all locale files. (#233)

# 3.12.0

- Modified the data collection process to not collect data when AdBlock is paused.
- Modified the data collection process to only collect data from HTTP(S) URLs.
- Modified the data collection to include an indicator that the user has custom filters.
- Updated the opt in data collection process to version 3.

# 3.11.2

- Moved the new 'data collection' option up on the Options page. (#231)

# 3.11.1

- Changed the method of sending the filter list data to a post. (#230)

# 3.11.0

- Fixed an issue on the 'Report an Ad' page when AdBlock attempts to automatically reload the page.
- Updated the opt in data collection process to version 2. (##229)

# 3.10.0

- Updated to ABP Core 1.13.2 (#221)

# 3.9.3

- Fixed a bug in user surveys. (#225)

# 3.9.2

- Re-added code to enable user surveys. (#224)
- Updated Translations.

# 3.9.1

- Updated 'bandaids' processing to help block ads on certain web sites. (#217)

# 3.9.0

- Updated translations.
- Updated to ABP Core 1.12.4 (#192)

# 3.8.8

- Updated translations.
- Updated 'bandaids' processing to help block ads on certain web sites. (#216)

# 3.8.7

- Updated translations.
- Updated 'bandaids' processing to help block ads on certain web sites. (#215)
- Added pause state information to debug data. (#214)

# 3.8.6

- Updated translations.
- Updated 'bandaids' processing to help block ads on certain web sites. (#210)

# 3.8.5

- Updated translations.
- Fixed text display issue on AdBlock menu. (#209)

# 3.8.4

- Updated translations.
- Updated 'bandaids' processing to help block ads on certain web sites. (#205)

# 3.8.2

- Updated the donate to us link on the AdBlock menu. (#204)

# 3.8.1

- Added a check for the browser state to the user surveys. (#202)

# 3.8.0

- Updated translations.
- Fixed an issue with passing of custom filters to our support site on the 'Report an Ad' page, and the 'Report a Bug' page. (# 198)
- Added rich notifications as a user survey type. (# 195)

# 3.7.0

- Updated translations.

# 3.6.0

- Changed the 'Spread the word' link on the AdBlock menu to 'Donate to help support AdBlock!', and added message logging when the AdBlock popup menu is opened. (#190)
- Updated Translations.

# 3.5.0

- Fixed an issue with the YouTube channel white-list feature. AdBlock now correctly handles YouTube channel names with special characters such as '#". (#179)
- Fixed an issue on the black list wizard. The black list wizard now shows an error message when a user creates invalid filter list rule. (#183)
- Updated the 'stats' processing to store and retrieve the next ping time, ping count, and unique identifier to two different persisted storage areas. (#182)

# 3.4.0

- Fixed an issue with the lower section of the AdBlock Options page being hidden behind the footer. (#167)
- Improved the security for the 'bandaids' processing on the getadblock.com/installed page by improving the host name check, and adding a check to click event for isTrusted. (#170)
- Updated the 'stats' processing to store the next ping time, ping count, and unique identifier to two different persisted storage areas. (#174)

# 3.3.2

- Removed all debug logging from the ping process. (#168)

# 3.3.1

- Removed debug logging from the ping process. (#168)

# 3.3.0

- Added all unique messages in the locale message files from the three variations of AdBlock (Chrome, Safari, Edge), so the locale files can be shared, and re-used by all of the various versions of AdBlock. (#145)
- Fixed the text description for the "Show All Request" AdBlock menu item. (#137)
- Added logic to create and save the 'blockage_stats' object during installation. (#141)
- Removed extra 'descriptions' in the locale message. (#148)
- The extension will now recognize and process multiple links on our site (getadblock.com/installed) that can be used to disable Acceptable Ads. (#159)
- Added debug logic to the ping process to help diagnosis issues with the ping processing. (#150)
- A GNU version 3 license file is included with the extension. (#140)
- Added an option on the General tab of AdBlock options to enable / disable the AdBlock devtools panel. (#142)

# 3.2.1

- Fixed issue with AdBlock icon display. (#160)

# 3.2.0

- Updated ABP Core 1.12.2 (#149)

# 3.1.1

- Added a link to the Privacy Policy on the Options page. (#147)

# 3.1

- Updated to ABP Core 1.12.1

# 3.0.8

- Fixed a bug on the 'Options' page, 'Filter List' tab. All of the checkboxes would be inadvertently checked when a user clicked the 'Update Now' button, or other similar actions. (#129)
- Added any remaining localStorage keys to the debug data, to help resolve any data migration issues. (#132).
- Fixed a bug with the ping processing incorrectly sending the wrong value for the aa parameter. (#134).

# 3.0.7

- Fixed a bug on the 'Options' page. Under certain circumstances the "Allow some non-intrusive advertising" option on the General tab was not being saved. (#123)
- Added a check for data on the error object in the Error Reporting logic. (#126)

# 3.0.4

- Fixed a bug on 'Options' page when the page was opened prior to the background page being initialized. (#112)
- Fixed a bug when the AdBlock context menu option was enabled / disabled on the Options page. (#111)
- Fixed a bug on 'Report an Ad' page for non-English users reporting an ad on English site. (#108)
- Updated the descriptions for certain language specific filter lists to include 'EasyList'. (#107)

# 3.0.3

- Fixed a bug in the data migration logic. (#114)

# 3.0.2

- Fixed the 'bug report' link on the Support tab for non-English users. (#105)

# 3.0.1

- Added missing message entries, and removed obsolete entries. (#102)

# 3.0

- Migrated AdBlock to use Adblock Plus (ABP)'s open-source core.

# 2.50

- Updated Translations.
- Fixed incorrect URLs / links on the Support tab of the Options page (#683).
- Changed the Malware filter list URL to download from ABP URL. Also added Malware blocked count to the ping data (#680).
- Refactored the YouTube Channel whitelist feature (#599).

# 2.49

- Updated Translations.
- Removed old code that is no longer needed with migration to the new AdBlock help / support site (#684).
- Fixed the AdBlock logo image on the "Show all requests" page (#678).
- Added a check for the tab 'id' property in the AdBlock popup (#674).
- Refactored the logic on the AdBlock Options page. Also, for Safari users, added a message that Acceptable Ads and Content blocking are mutual exclusive (#682).

# 2.48

- Updated Translations.
- Updated the placeholder text in the "Show ads on web page or domain" example URL (#669).
- Removed duplicate logic on the General tab of the AdBlock Options page (#671).
- Migrated links to the new AdBlock help site (#632).
- Updated the "Report an Ad" and "Bug Report" pages to use the new AdBlock help site (#632).

# 2.47

- Updated Translations
- Removed duplicate strings from the translation (message) files (#666).
- Added a timestamp query string to the Malware URL to prevent caching by the browser (#668).
- For Safari users, content blocking will not be enabled by default (#665).
- Updated the Polish filter list URL (#651).
- Updated the Acceptable Ads un-subscribe message on Options page, General tab (#657).
- Updated the AdBlock image files (#654).

# 2.46

- Fixed a typo in the description of the AdBlock Warning Removal list, it should be a lowercased 'b' (#658).
- Added a new parameter to the ping data to indicate if the advance setting is enabled (#660).
- Fixed an issue with the blocking assistant on some sites (#644).
- For Chrome users, modified the "/installed" logic to use the Chrome specific chrome.runtime.onInstalled API (#656).
- For Safari users, AdBlock will now use the WebKit content blocking feature on new installations. (#619).
- For Safari users, fix a bug with the "Undo my blocks on this domain" feature (#570).

# 2.45

- Added a new, advanced feature to view all HTTP Requests for a tab (#653).

# 2.44

- Updated the URL of filter lists hosted on AdBlock's servers. (#652)
- Updated translations.

# 2.43

- Removed Michael's message. (#645)
- Added logic to the 'Report an Ad' page to check if Acceptable Ads is enabled. (#646).
- Added language specific filter lists for Arabic, Estonian, Icelandic and Lithuanian. (#647)

# 2.42.1

- Modified the block image logic to not redirect any images, but rather cancel the request. (#642)

# 2.42

- Modified the block image logic to not redirect certain images, but rather cancel the request. (#638)
- Added logic to log a message when user clicks the disable acceptable ads link on the '/installed'. (#639)

# 2.41.3

- Added required property for Safari 9 to info.plist file. (#636)

# 2.41.2

- Updated the style attributes of the Acceptable Ads message to better fit the page / tab. (#635)
- Updated the ping data to send a 'u' when the Acceptable Ads is undefined. (#635)

# 2.41.1

- Added missing image file for Safari.

# 2.41

- Added Acceptable Ads filter list. (#627)

# 2.40.1

- Remove the timestamp query string from the Malware filter list URL

# 2.40

- Updated Translations
- Updated Malware filter list URL
- For Safari users, the 'Author' field was changed from Michael Gundlach to BetaFish, Inc

# 2.39.1

- Removed the cache parameter for AdBlock CDN AJAX requests. (#626)

# 2.39

- Updated the AdBlock custom filter list URL. (#623)
- Update translations, remove unused entries. (#624)

# 2.38

- Made a runtime performance improvement for users subscribed to the Malware filter list. (#597)
- Removed some temporary, cleanup code related to old filter lists. (#594)
- Added the total block count and the AdBlock custom filter list update timestamp to the un-install URL to help determine why users are un-installing after just a few minutes of use. (621)
- Added the ping count to the ping data. (#618)
- Removed the 'View the Resource' page. (#614)
- Added formatting lines for the debug information for Tender support tickets. (#613)
- Removed a site specific 'bandaid' for 'thepiratebay'. (#593)

# 2.37.3

- Updated the Safari description and website information.

# 2.37.2

- Reverted the change that replaced 'Help Spread the Word' link in the AdBlock popup with an Amazon affiliate link. (#612)

# 2.37.1

- To help with debugging AdBlock, the length of the error string sent to the getadblock.com server has been increased. (#611)

# 2.37

- Added an user enabled option to anonymously send filter list usage metrics to us to help improvement the functionality and performance of AdBlock. (#610)
- For new installation, users will be subscribed to the malware filter list. (#606)
- For users that have a locale of 'en-us', the 'Help Spread the Word' link in the AdBlock popup has been replace with an Amazon affiliate link. (#604)
- Updated the malware notification text. (#598)
- Removed old log messages. (#589)
- Fixed a bug - Unicode domains in filter lists are now correctly processed. (#588)
- Changed the CSS rules from 'visibility: none' to 'visibility: hidden'. (#585)
- Fixed an issue with the AdBlock white-list and black-list wizards not appearing on certain sites. (#582)

# 2.36.2

- Removed debug logging messages for Safari users. (#591)

# 2.36.1

- Added debug logging messages for Safari users. (#590)

# 2.36

- Added an if check to verify that domain is not undefined when processing URLs. (#579)
- Changed the order of evaluation in the Survey processing. (#576)
- Update the JavaScript error processing to include the stack trace information if it does not include an HTTP URL. (#575)
- Updated the white-list filters for showing ads on Google Search when the 'show Google ads' option is enabled. (#573)
- Removed Disconnect search code from AdBlock. (#568)
- Update the height of the Subscribe popup. (#491)

# 2.35.2

- Removed debug logging messages for Safari users. (#578)
- Updated translations.

# 2.35.1

- Added debug logging messages for Safari users. (#577)

# 2.35

- For Safari users, AdBlock will now block popups on Safari. (#547)
- For Safari users, the deleting of cached resource data when a tab or window is closed has been simplified and improved. (#546)
- For Chrome users, AdBlock will ping upon browser startup when the installation type is 'admin'. (#566)
- For Chrome users, AdBlock will retry to open the 'getadblock.com/installed' page when it fails to open initially. (#564)
- Modified the translation of the DropBox error message to be easier for the translation team. (#562)

# 2.34

- On the 'Report an Ad' page, the support / forum URLs for three filter lists (Korean, Sweden, Turkish) were updated. (#560)
- In Chrome, removed the normalizing of the type on URL requests for fonts since it is not needed. (#553)
- In Safari, improved the removal of pre-roll ads on YouTube. (#552)
- On the Custom tab, under AdBlock options, added the display of error messages when an invalid filter is found during a save of custom filters. (#545)
- Added the ability to whitelist frames. (#521 & #518)
- Improved the YouTube channel whitelist feature, so that a YouTube page is only reloaded when required. (#504)
- In Chrome, the 'number of ads blocked' counter is incremented when a popup is blocked. (#497)
- In Chrome, on the 'Report an Ad' page, an option was added to enable and disable other extensions to help find the source of an ad. Also, The debug information from the 'Report an Ad' page, and the Support tab, will include other extension information (if allowed by the user) to help us better resolve issues. (#462)

# 2.33

- Removed the retry logic when the "/installed" page open on getadblock.com. (#551)

# 2.32

- Fixed a bug in the retry logic when trying to open the "/installed" page on getadblock.com. (#548)
- Added retry logic when the user is the "/question" page on getadblock.com. (#543)
- Added the filter text to the JavaScript exception message when an invalid option is found in a filter. (#537)
- Fixed the logic for creating a YouTube whitelist channel filter to avoid white-listing other channels. (#534)
- Fixed an issue with the whitelist / blacklist wizards not being displayed correctly on certain sites. (#527)
- Added support for Internationalized domains (IDN) throughout AdBlock. (#495)
- Updated Translations

# 2.31

- New language: Gujarati

# 2.30

- Name change to back to "AdBlock"
- Updated Translations

# 2.29

- Name change to "BetaFish Adblocker" (temporary)

# 2.28

- For Chrome, added installation type to the ping data. (#530)

# 2.27

- For Chrome, added retry logic when the '/installed' page fails to open. (#525)
- For Chrome, added a message to include installation type, when AdBlock is installed. (#526)

# 2.26

- Added the extension Id to the data included with the JavaScript error message. (#523)
- For Chrome only, improved / fixed the logic that is checking if the '/installed' page is opened correctly. (#522)
- For Chrome only, added the approximate installation duration to the uninstall URL. (#522)

# 2.25

- Fixed an issue with the DropBox sync processing duplicating filters during browser start. (#442)
- Added a message to the options page when the DropBox sync processing failed due to a large number of custom filters. (#474)
- Updated Translations

# 2.24

- Fixed JavaScript stack exception processing. (#515)
- Modified the new install check logic to only send a message when first run is true. (#513)
- Modified the survey acknowledgement processing to log the 'message' property of chrome.runtime.lastError (if it exists). (#516)

# 2.23

- Added browser and os version information to ping data (#510)
- Added validation logic to help detect an invalid installation state (#510)
- Added acknowledgement processing from overlay surveys (#510)
- Added 'stringify' to the AdBlock settings in the debug data (#512)
- Added a style tag of 'display:none' to Beta div tag in the AdBlock pop up menu. (#508)

# 2.22

- Enhanced survey processing (#453)

# 2.21.1

- For Safari users, added a user confirmation prompt when subscribing to a new filter lists using the ABP syntax. (#502)

# 2.21

- Removed the Norwegian filter list since it is no longer active. (#489)
- For each subscribe filter list, added the last update timestamp to debug data. (#482)
- Added the malware notification setting to debug data. (#458)
- Added additional CSS to whitelist/blacklist dialogs to avoid display issues on some websites. (#460)
- Removed an unnecessary call to sendResponse. (#484)
- For Chrome users, added a user confirmation prompt when subscribing to a new filter lists using the ABP syntax. (#486)
- Fixed an issue when the request URL does not contain a '.' (#500)
- Updated the Chrome web store description.(#501)

# 2.20.1

- Updated Translations
- In Chrome, added an uninstall URL (#493)

# 2.19

- Updated Translations
- In Safari, logic was added to dispatch an event when the extension blocked content (#478)
- Fixed a small memory leak (#456)
- Added the extension installation Date to ping data (#448)
- Fixed a JavaScript error in Chrome when updating badge text (#446)
- Updated the workaround logic to Chrome's reporting fonts as "other" types (#439)

# 2.18.1

- Updated Translations
- Remove unnecessary code from ping processing.

# 2.18

- Fixed an issue when syncing custom filters using DropBox. (#413)
- Fixed an issue with the number of blocked ads on single page sites. (#414)
- Fixed an issue with the URL of Malware filter lists on the AdBlock Options page - Filter List tab. (#436)
- Added an new Malware Notification option when users are subscribed to the Malware filter list. (#435)

# 2.17

- Added a new option for Safari users - "ClickToFlash compatibility mode". (#421)
- Updated the Israel/Hebrew filter list forum link on 'Report an Ad'. (#423)
- Updated the style of the AdBlock popup menu for Chrome Beta users. (#422)
- Added the list of hiding rules to the AdBlock 'Show the Resources list' page for Safari users. (#408)

# 2.16.3

- Added the saving of the malware filter list (same as other filter lists), so that the extension does not need to do a request when the browser starts up.(#432)

# 2.16.2

- Added control logic to the getting of the malware filter lists (#430)

# 2.16.1

- Fixed a bug in the Safari extension when a windows was closed (#428)

# 2.16

- AdBlock now uses the YouTube API to retrieve the channel name when users have the Whitelist a YouTube Channel feature enabled. (#392)
- The 'Filter syntax tutorial' link on the AdBlock options / Customize tab now checks if the generated URL is valid. (#394)
- Added a check for chrome.runtime.onMessage API, since it isn't available in Chrome 25 and older versions. (#395)
- Added an option to the General options tab to not display the ads block counter on the AdBlock popup menu.
  The option to display the # of ads block was moved from the AdBlock popup menu to the General tab as well. (#401)
- Added logic to set focus on new tabs open by AdBlock (for example, the options pages), when the Chrome is running in incognito mode. (#405)
- On the 'Report an Ad' page, all of the questions are now bolded. (#416)
- Reformatted the text and fixed typos in the change log. (#418)
- Modified several JavaScript throws statements to now use an Error object. (#420)

# 2.15

- Improved performance of extension when using the Malware filter list (#384)
- Added the 'show the resource list' page to the Safari version of the extension (#385)
- Added a timestamp to the JavaScript error text that is saved in local storage (#390)
- Added logic to determine the correct URL for the Filter list syntax link on the Custom tab based on the user's language (#387)
- Updated the Japanese filter list URL (#386)

# 2.14.4

Removed unnecessary backup directory that was included in the zip and extz files.

# 2.14.1

Removed invalid character from the French message.json file

# 2.14

- Removed the Spanish filter list from the options since it is no longer being supported (#366)
- Updated translation texts
- Updated the version numbers (added 39 and 40) for a Chrome bug workaround (see crbug.com/410382) (#380)

# 2.13.2

- Modified the YouTube specific logic to use ABP approach (#372)
- Corrected the logging of JavaScript errors in the Chrome Beta version (#367)

# 2.13

- Added the ability to exclude / disable filter list entries (#241)
- Fixed an issue with a missing click handler on the popup menu (#359)
- Removed confusing message on popup menu (#360)
- Fixed a JavaScript error on the background page in Safari when several tabs are closed while still being rendered. (#357)
- Added a user message that is displayed when the whitelist and blacklist wizard can't run on older sites with framesets. (#352)
- Added a 'reload page' option to the white list wizard. (#349)

# 2.12.1

Fixed an issue with the back button in Safari & YouTube. (#350)

# 2.12

- Fixed an issue in the Chrome Beta version in the 'report an issue' link in the popup menu. (#347)
- In Chrome, improved the cleanup of old data when tabs are closed. (#345)
- Fixed an issue with the whitelist wizard not being displayed on certain sites. (#341)
- Fixed an issue with the AdBlock icon in Safari 5.0 (#342)
- On the AdBlock options page, Filter Lists tab, add the title of custom filters lists the users is subscribed to (if there is a title for the filter list). (#336)

# 2.11

In the 'Report an Ad' feature, the extension will now perform a check for known malware
domains in the list of resources. If resources from a known malware site are found, the
user is notified, and a link with more information is provided. If no malware resources
are found, the page continues to work as before. (#315)

# 2.10.3

- Added a work around to a Chrome bug which incorrectly sets the element type (#339) - see http://crbug.com/410382
- Added the column number to the information sent when a JavaScript exception is caught

# 2.10.2

Fixed JavaScript error on YouTube in Safari

# 2.10

- Improved the Safari AdBlock menu (#291)
- Fixed JavaScript error and ads showing on YouTube.com (#332)
- Removed retry logic on ping failures (#331)
- Modified text in buttons to black (#329)
- Added logic to determine the AdBlock version to help with support tickets (#328)
- Removed survey opt out option (#326)

# 2.9.4

Updated Translations

# 2.9.3

- Fixed an issue with DropBox sync process (#325)
- Fixed an memory leak issue in Chrome where pre-rendered tab information was not removed when the tab id was changed (#324)
- Modified the 'Help Spread the Word' link in the popup menu to open a new tab instead of being loaded in the menu (#318)
- Fixed an issue in Safari with un-whitelisting a site (blacklisting it) (#317)
- Improved the string processing of debug information when users report an issue or ad to the AdBlock support site (#307)

# 2.9.2

- Fixed a JavaScript error in DropBox sync logic
- Added the new option 'show survey' to the options that are synced using Dropbox

# 2.9.1

Fixed a style issue on the whitelist and blacklist wizards

# 2.9

- Added a feature to allow users to synchronize their settings using DropBox
- Added an option to allow users to opt out of AdBlock user surveys
- Added logic to not log JavaScript error if they contain URL information
- Updated the version of jQuery and jQuery UI (2.1.1 and 1.10.3)
- Fixed an issue when AdBlock was paused but still blocked popup windows

# 2.8.2

Reverted translation because the line length exceeded the 132 character limit

# 2.8.1

Removed externally_connectable permission from manifest.json file to avoid additional permissions needed for Beta version.

# 2.8

Added logic for Chrome beta users only; opening a /beta tab on updates.

# 2.7.13

- Added 'AdBlock Warning Removal' Filter list as an option on the Filter Lists option page. (#296)
- Removed the logic to see if a user should be given a 'golden ticket'. (#298)

# 2.7.12

- Fixed an issue with Safari and the new translation process (#292)
- Added retry logic to the ping process, and enhanced survey processing (#290)

# 2.7.11

- Updated translations, and added translation credit file (#272)
- Default ad reports to private on the support web site, to avoid spam bot issues (#281)
- Added a link / option to the support page to show users how to report ads (#282)
- Corrected an issue in Safari with YouTube ads (@284)
- Removed 'beta' label from the Whitelist YouTube channels option (#288)

# 2.7.10

Corrected issue with 2.7.9 and the Safari / YouTube fix

# 2.7.9

- Updated logic to correctly block video ads with the HTML 5 player on Safari, on youtube.com (#276)
- Improved the detection of getadblock.com website to ensure any injected extension information only occurs on the correct website (#274)
- Include the total number of ads blocked in the weekly ping statistics (#274)

# 2.7.8

- Added setting information to bug reports (#267)
- Updated Finnish filter list URL (#270)
- Updated hiding style sheet configuration (#266)

# 2.7.7

- Added support information to bug reports (#265, #263, #231)
- Filter unnecessary whitelist rules (#264)

# 2.7.6

- Updated Translations
- Fixed font display issues in Chrome on certain OS'es (#255)

# 2.7.5

- Fixed JavaScript error in search (#251)
- Performance improvement (#248)
- Fixed changelog I18N placeholder issue (#253)

# 2.7.4

- Added Options to view the changelog on the support page (#244)
- Corrected issue with Chrome badge counter not being incremented for hidden content (#237)
- Fix JavaScript error in search (#249)

# 2.7.3

- Added Extension version number to Ad Reports
- Added font support for some specific characters
- Improved Blacklist support on custom filters
- Fixed JavaScript error on Chrome popup menu

# 2.7.2

Issues #228, #220, #216, #219, #221, #227, #229

# 2.7.1

Updated Translations

# 2.7

New design for Options pages and popup menu

# 2.6.33-37

Bug fixes

# 2.6.32

Bug fixes, and URL updates

# 2.6.31

Bug fixes, and YouTube Channel Whitelisting

# 2.6.30

Removed unnecessary files

# 2.6.29

Bug fixes, remove Safari experimental feature, updated French filter URL

# 2.6.28

Small bugfixes (Safari YT Bug) and updated Chinese filter URL

2.6.19-27: Beta tests for survey

# 2.6.18

Minor fixes

# 2.6.17

Version bump.

# 2.6.16

Migrate from chromeadblock.com to getadblock.com

# 2.6.15

- Add Fanboy's annoyances list to the Filter Lists page.
- Fix Safari bug showing ads on Top Sites websites.

# 2.6.14

Settings measurement

# 2.6.13

Small bugfix for UI and updated Israeli filter URL

# 2.6.12

Beta test for survey

# 2.6.11

- New language: Catalan
- Ability to survey small numbers of users about possible developments in AdBlock

# 2.6.10

- Bugfix for slow initial filter subscription.

  2.6.9 (beta channel only):

- Added and updated filter lists based on user's localization, added Malware and Antisocial filter list
- Added RTL function for Arabic and Hebrew users
- Added language: Norwegian
- Bugfix: blocked ad count does not carry over into new, blank tabs

# 2.6.8

Removed crowdfunding message from AdBlock button

# 2.6.7

Update method call that otherwise breaks in Chrome Canary

# 2.6.6

Fix small bug in CrowdTilt notification code

# 2.6.5

- Help and ad reporting links now go to new support site
- Notification about a CrowdTilt campaign
- Blocked ad count is darker color to avoid looking like a notification

# 2.6.4

Undo one of the minor bugfixes in 2.6.3 because it itself had a bug breaking AdBlock if you reloaded a page too quickly

# 2.6.3

Minor bugfixes

# 2.6.2

Don't forget user's badge view setting when AdBlock is paused (Pao), style change of block counts in popup (tomasko)

# 2.6.1

Help link explaining new block counts section in popup

# 2.6.0

Simplify Filter Lists options tab (Pao), show blocking stats in toolbar button and popup (Pao)

# 2.5.65

Blacklist wizard never gets hidden by page content (wormboy.d); updated Russian filter URL (tomasko)

# 2.5.64

Ad report wizard makes user disable other extensions (Marcus Jackson); 'Report an ad' available to non-advanced users (tomasko), Follow button added to Share page (tomasko), minor bugfixes

# 2.5.63

Pressing enter clicks default button in blacklist and whitelist wizards (Pao), lock icon in install URL.

# 2.5.62

Put sharing link in Chrome toolbar button menu (tomasko), stop using deprecated API (Pao), test lock icon in URL upon install

# 2.5.61

Filter list fetch improvements

# 2.5.60

Point to working EasyList and German URLs

# 2.5.59

Replace outdated Czech list with Czechoslovak list (tomasko)

# 2.5.58

Small UI change, and change French list URL (famlam); survey for Safari 6 users

# 2.5.57

Blacklister UI bugfix (John), corner-case Safari background image bugfix (famlam), new Russian+Ukrainian URL

# 2.5.56

Minor Resource List bugfix (famlam), other minor bugfixes

# 2.5.55

Add Retina support in Chrome on Macs (John), minor bugfix (famlam), let Safari users opt in to experimental faster method of hiding ads

# 2.5.54

Disable caching of blockcounts

# 2.5.53

Stop pointing to Amazon S3. Support block counts app.

# 2.5.52

Point to Amazon S3 for a moment

# 2.5.51

onMessageExternal not supported

# 2.5.50

Add block count statistics

# 2.5.49

Fix Hulu ad blocking again, plus minor bugfix

# 2.5.48

Minor bugfixes and UI changes

# 2.5.47

Update Finnish and French filter list URLs (john). Block video ads at Hulu.com again in Chrome.

# 2.5.46

Correct toolbar button text in Safari (crazyskeggy). Resource List shows source filter list; filter validation bugfixes; and memory and speed improvements (famlam). Fix broken buttons in Hotmail.

# 2.5.45

Test users delaying payment decision for an hour

# 2.5.44

Fix filter validation bug, compress install package some (famlam)

# 2.5.43

Fix conflict with other extensions, remove dead Polish list, minor changes (famlam)

# 2.5.42

minor changes, bugfixes on NFL.com and hotmail.com (famlam), Undo of blacklist wizard rules available in button and context menus

# 2.5.41

Fix 'Show Google text ads' for Google Instant

# 2.5.40

Add support for selector exception syntax, code refactoring (famlam)

# 2.5.39

Small bugfixes (famlam) and a Retina display icon in Safari (John)

# 2.5.38

Fix context menus in Safari 5.0.6, log error line numbers to server, several other bug fixes (all famlam)

# 2.5.37

Add a search box to the Resource List (famlam), blacklist wizard improvement

# 2.5.36

Update to manifest version 2 (famlam) and turn back on CSP

# 2.5.35

Add warning to ad report page, stop using deprecated Chrome APIs (famlam). Minimum Chrome version required is now 18.

# 2.5.34

Improvements to the Options page (famlam), the Resource List (famlam), the Ad Reporter (john, famlam), the Blacklister (wormboy, famlam), and the Whitelister. Decrease the chance of showing an ad at startup or when AdBlock is updated (famlam).

# 2.5.33

Delete Chrome 16-style blocking code.

# 2.5.32

Get rid of occasional 'error: blocked by 3rd party' iframes in Chrome

# 2.5.31

various parsing bug fixes (famlam)

# 2.5.30

Popup blocking in Chrome (famlam)

# 2.5.29

Small domain parsing change (famlam), stop using beforeload in Chrome 17+, get rid of 'blocked by third party extension' iframes

# 2.5.28

Button popup was not showing for Chrome 16 users who had not set any settings (jaysoffian)

# 2.5.27

Fix some websites broken by injecting a LINK tag

# 2.5.26

Don't warn RockMelt users of impending upgrade. Work around Japanese filters issue (famlam).

# 2.5.25

Help explain CatBlock to users who missed it on April Fools or who want to know how to get it after 4/4

# 2.5.24

Don't let websites open AdBlock pages; warn Chrome 16 users of impending breakage (famlam); don't ask Safari 5.0 users to upgrade if they can't (zee)

# 2.5.23

Delete unmaintained translations. Want to see yours back again? Please visit the HowToTranslate wikipage.

# 2.5.22

Stop honoring bogus Cache-Control headers, parse custom URLs better (famlam)

# 2.5.21

Minor bugfixes, use https for Dutch filters (famlam)

# 2.5.20

Address a few broken websites (famlam)

# 2.5.19

Handle FB change that caused ads to show

# 2.5.18

Minor changes

# 2.5.17

Minor bugfixes

# 2.5.16

Revert popup blocking, as it disables AdBlock for Chrome 16 users. Will add again when Chrome 16 is dead.

# 2.5.15

Apply Content Security Policy. Re-add popup blocking (famlam). Bug hunting.

# 2.5.14

Minor bug fixes

# 2.5.13

Fix Safari toolbar button menu bug (zee) and blacklist wizard UI bug

# 2.5.12

Refactoring, and work around a bug in Chrome 18 that breaks AdBlock (famlam)

# 2.5.11

Typo

# 2.5.10

Show a menu when Safari toolbar button is pressed (Alexey Ermakov)

# 2.5.9

Turn on new webRequest code for all Chrome 17 users

# 2.5.8

Oops, disable popup blocking as adding it disables AdBlock. Fix broken youtube ad blocking in Safari.

# 2.5.7

Popup blocking (famlam), speed improvement (famlam), remove dead Ukrainian list (John)

# 2.5.6

Remove instrumentation

# 2.5.5

More bug hunting

# 2.5.4

Instrumentation to hunt down issue chromium:106913

# 2.5.3

Include stack trace in logs

# 2.5.2

Measure opt-in rate to new-style blocking, so we know when it's been tested enough to enable for everyone

# 2.5.1

Quieter logging

# 2.5.0

All in-video and in-Flash ads are blocked in Chrome if you turn it on under AdBlock Options

# 2.4.34

Don't break the toolbar button

# 2.4.33

Store data in Safari settings instead of localStorage, so Safari does not wipe it out after Private Browsing

# 2.4.32

Fix critical bug breaking Safari after Private Browsing, remove dead Norwegian list (famlam), new jQuery version (famlam)

# 2.4.31

Small changes (famlam), fix bug in waiting for idle

# 2.4.30

Fix Gmail bug in Safari, wait for idle before fetching filters (famlam), fix filter normalization bug (famlam)

# 2.4.29

Add greek filters (drewish), disable pause on close (Famlam), and sent last-modified and other headers to filter lists (Famlam)

# 2.4.28

Clicking 'Update Now' on Safari Filter Lists page now correctly shows elapsed time

# 2.4.27

{{{[style]}}} change again, this time with workaround for GMail and Yahoo

# 2.4.26

Revert {{{[style]}}} rules change, as it breaks GMail in Chrome

# 2.4.25

Several small changes, plus {{{[style]}}} rules are supported again, and some pages that spiked the CPU were fixed (famlam)

# 2.4.24

Small bugfixes, rework filter list manager (famlam), and add links to project homepage on Options page (John).

# 2.4.23

Small bugfix, and support resourceblock.html in Safari (famlam)

# 2.4.22

Added background image blocking in Safari (famlam), a +1 button in the Chrome browser action, and a small bugfix in the blacklist wizard

# 2.4.21

Minor Safari bugfixes

# 2.4.20

Minor speedup, graduate "new way to block ads" beta option and make it the only way, and don't refresh the page after blacklisting if you can help it (famlam)

# 2.4.19

Minor bug fixes, improvement to unsubscribing oversubscribed users (famlam)

# 2.4.18

Retire the app version (famlam)

# 2.4.17

Warn users who oversubscribe to filter lists, and unsubscribe (one time) users who oversubscribed.

# 2.4.16

Axe vietnamese filters; small bug fixes; helper wizard on Customize tab to run AdBlock on only a few sites (famlam)

# 2.4.15

A pile of bugfixes by Famlam (Issues 5679 5380 699 5726), plus we added a Ukrainian translation.

# 2.4.14

Minor bugfixes (Famlam)

# 2.4.13

Small UI changes and bugfixes (famlam)

# 2.4.12

avoid collision due to not-very-random seeds

# 2.4.11

AB test on install page

# 2.4.10

Minor bugfixes or edits for a couple websites.

# 2.4.9

Bugfixes by wormboy, Drewish, and famlam. Make the whitelisting wizard more powerful (famlam).

# 2.4.8

l10n typo

# 2.4.7

i18n of the installation page. Switch to pay-what-you-want instead of donations.

# 2.4.6

Typo

# 2.4.5

Hide advanced features behind advanced checkbox (famlam)

# 2.4.4

Finish roll out of new install page

# 2.4.3

Prettier new-install page, hopefully clearer to non-technical users as well

# 2.4.2

Bugfix in resourceblock; thanks to Juho again for the report. Remove reference to dead file.

# 2.4.1

Translators get credit under AdBlock Options (Drewish). Minor bug fixes and cleanup (famlam). Lazy-load black and whitelisting code only when it's needed, to reduce memory in tabs.

# 2.4.0

Restructuring of a few parts of the filtering engine, resulting in (on my fast laptop) a savings of 150-180ms per tab load(!), plus 3ms per resource on the page. E.g. cnn.com with 150 resources saves about 650ms.

# 2.3.32

Fix bug related to clicking malformed filter list subscription links. Thanks to Juho Nurminen for the report and most of the fix. Also fix a leaking variable (famlam).

# 2.3.31

Fix blacklister bug for Chinese users (famlam)

# 2.3.30

AdBlock Options in Safari now accessible through Extensions|Preferences. Subscribe legacy users to language-specific filter lists if they've never set up their own lists.

# 2.3.29

Don't run bandaids on most pages (famlam)

# 2.3.28

Fix incognito app behavior. Fix manual filters paste bug (famlam). Blacklist wizard bugfix (wormboy).

# 2.3.27

Test a new way to remove ads, which keeps some websites from breaking (famlam)

# 2.3.26

Change app shipping

# 2.3.25

Remove dead log message (Drew)

# 2.3.24

Fix blacklisting wizard manual editing bug (famlam)

# 2.3.23

Text change

# 2.3.22

Fix blank install page in Safari

# 2.3.21

Fix Safari bug breaking AdBlock after restart. Thanks to conundrum on Freenode, plus the many users on the issue tracker (Issue 5384) who helped diagnose the problem!

# 2.3.20

Fix app description in manifest

# 2.3.19

Show install page to Safari users, and create app version of AdBlock

# 2.3.18

Fix broken signup for subscriptions

# 2.3.17

Internal code shuffling

# 2.3.16

Fix opt-in to Google search ads when using Google Instant

# 2.3.15

Speed and code improvements, and don't let the blacklist and whitelist wizards be open at the same time (famlam, wormboy.d)

# 2.3.14

General cleanup and refactoring of helper functions

# 2.3.13

Make toolbar button tab-specific, so it looks right when multiple windows are open (Famlam)

# 2.3.12

Fix "Block an ad on this page" from toolbar immediately after right clicking page (Naesten)

# 2.3.11

Filter updates

# 2.3.10

Don't show context menu in Chrome Extension Gallery

# 2.3.9

Some resourceblock.html improvements and minor bugfixes (famlam, wormboy.d)

# 2.3.8

Highlight the element you're about to click in the blacklist wizard (wormboy.d)

# 2.3.7

jQuery and jQuery UI refresh

# 2.3.6

New advanced url-blocking wizard linked off of existing hiding wizard (famlam)

# 2.3.5

Try yet again to get the mac-specific Hide Button message correct

# 2.3.4

Fix a bug: whitelisting a page was not updating the toolbar icon immediately (famlam)

# 2.3.3

Show hide button message on install page too

# 2.3.2

Fix positioning of blacklist wizard (wormboy.d). Fix hide button message bug on mac.

# 2.3.1

Tell Mac users workaround for hiding button, since Chrome 9 failed to ship Hide Button on Mac (famlam)

# 2.3.0

Add a toolbar button (again), retiring the Browser Button For AdBlock extension.

# 2.2.32

Bugfix: new installation page was showing checked 'Show a toolbar button' checkbox

# 2.2.31

Bugfix on ad report page (john) and more thorough validation of custom blacklist entries (famlam)

# 2.2.30

Support opt-in to Google ads when not subscribed to EasyList (famlam)

# 2.2.29

Localization updates, correct a URL scheme bug, and remove dead code

# 2.2.28

Support $document filter syntax, allowing individual pages to be whitelisted. Also added $elemhide support. (Famlam)

# 2.2.27

Ignore filters if they contain unknown options (famlam)

# 2.2.26

Support requiresLocation in abp:subscribe links (famlam)

# 2.2.25

Handle new EasyPrivacy filter that was breaking many websites

# 2.2.24

See which filter lists should be added to or removed from the options page.

# 2.2.23

In Chrome, reduce overall browser RAM usage by up to 30%, and decrease AdBlock run time by about 50% :D

# 2.2.22

Validate filters on download instead of when inputting into filter engine, because we input into filter engine on every page load. Saves 50ms per frame. Goooo famlam! Also fix the parsing of `@@||$domain=domain.com` filters

# 2.2.21

New and improved Youtube ad blocking (famlam)

# 2.2.20

L10n typo

# 2.2.19

Change donation request to mention that this is now my full time job.

# 2.2.18

Bugfix for new frame blocking code

# 2.2.17

Keep youtube user-channel videos from autoplaying incorrectly (drewish). Support frame,audio,video, and input type=image blocking (famlam).

# 2.2.16

typo...

# 2.2.15

Updated text description for web store launch

# 2.2.14

Fix broken Spanish translation. jQuery-1.4.4 for speed improvements. Small bugfixes and improvements.

# 2.2.13

Subscribe non-English-speakers to an appropriate Easylist sublist (Famlam)

# 2.2.12

Roll back chrome.tabs.insertCSS() work while we figure out how to make it run earlier and how to be specific for different iframes on a page.

# 2.2.11

Fix tagging typo

# 2.2.10

Use Chrome API for CSS hiding which should improve RAM and speed in Chrome.

# 2.2.9

Work around Chrome bugs related to chrome.tabs and SVG images. 'background' type now deprecated in filter lists. Special cases for hotmail.com and hk-pub.com. Add note to ad reporter about video ads not being blockable yet except in Youtube. Speed up ad blocking in Chrome by removing a redundant regex parse. (All by Famlam!)

# 2.2.8

Use less memory in Chrome (famlam)

# 2.2.7

Vastly simplified mechanism for dealing with ads in Chrome that load before the filter engine is in place (famlam). Also, we are now at 18 languages -- see http://bit.ly/AdBlockTranslations for the list and for credits!

# 2.2.6

Memory and speed improvements (famlam)

# 2.2.5

Do not let users try to block the BODY tag

# 2.2.4

typo

# 2.2.3

Move the browser button back into a separate extension until Chrome supports fully hiding browser buttons.

# 2.2.2

Make the Chrome right click menu disappear properly when requested or paused or whitelisted

# 2.2.1

Typo fix

# 2.2.0

Add a browser button to AdBlock (integrating the Browser Button For AdBlock extension.) Also add support for pausing Chrome AdBlock via the browser button.

# 2.1.15

Add Indonesian translation, and improve memory usage in Safari.

# 2.1.14

Block background images even when they are specified in stylesheets (famlam). Touchups to the UI for manual blacklist editing. Fix typos in last release.

# 2.1.13

Warning popup to Chrome users that next week AdBlock will be disabled as a necessary part of an upgrade, with instructions for re-enabling it.

# 2.1.12

Localized right-click menu text (famlam)

# 2.1.11

Memory savings in Chrome and probably some in Safari (famlam)

# 2.1.10

Revert to old Easylist and Easylist German URLs, per Wladimir Palant's (author of Adblock Plus) request

# 2.1.9

Safari users also lose the context menus if they choose to via the Options page

# 2.1.8

Quick patch to allow optional right click menus and to force Chrome 6 or higher, to get rid of permission error messages for Chrome 5 users.

# 2.1.7

Optimize Chrome RAM usage when 'Block most ads...' beta option is disabled

# 2.1.6

Replace keyboard shortcuts with right click menu items

# 2.1.5

Add or update German, French, Italian, Korean, Macedonian, Dutch, Polish, and Chinese translations.

# 2.1.4

Found a workaround for Safari crashes

# 2.1.3

Roll back to 2.0.25, because Safari is crashing something fierce. Probably due to 2.1.0, but just in case 2.0.0.26 is the culprit (which was only released for an hour before 2.1.0) I'm rolling to .25. This version will only be released to Safari.

# 2.1.2

A few remaining l10n tasks

# 2.1.1

Work around Gallery bug causing extension not to install...

# 2.1.0

Added internationalization support, and English Dutch and German translations (Famlam, plus John Rey providing German translation)

# 2.0.26

Remove whitespace in hotmail, update some filter list links, fix a bug in ad reporting page, and support filter list redirects -- all done by Famlam

# 2.0.25

Fix broken ad reporting link in Safari

# 2.0.24

Support object-subrequest a little better. Ask for fewer ad reports to hopefully improve the signal to noise ratio.

# 2.0.23

Ignore certain filters that Webkit does not parse properly

# 2.0.22

Fix some Safari issues causing ads to slip through, and improve Chrome and Safari memory usage.

# 2.0.21

Many bugfixes and small improvements by Famlam; read the full list at adblockforchrome.googlecode.com under Source -> Changes

# 2.0.20

Chrome should not emulate true blocking in subframes because each one costs a fixed amount of RAM and some pages have _lots_ of subframes.

# 2.0.19

Revert messed up grayscale icon for Safari toolbar

# 2.0.18

Work around Chrome bug causing Google Calendar to render incorrectly in some cases

# 2.0.17

Bandaid to fix collapse-blocked-elements hanging on some websites

# 2.0.16

Correct third-party and first-party and match-case support (famlam)

# 2.0.15

Respect filter subscription expiration dates (famlam)

# 2.0.14

Give icons a new look (thanks tgines!), and do not lose the current tab when reloading the Options page

# 2.0.13

Fix bug with "Collapse Blocked Elements" beta feature

# 2.0.12

Blacklist UI shows full effect of proposed rule. (famlam)

# 2.0.11

Support collapsing empty ad holding elements, and auto-subscribe
EasyList if you subscribe to an EasyList additional list (famlam)

# 2.0.10

Fix some filter rule parsing bugs and a small UI bug (famlam)

# 2.0.9

Grr, turns out Gmail needs a special case to work around a bug in Chrome that makes CC and BCC fields disappear on-click. Put the special case back in.

# 2.0.8

Remove an old facebook layout hack that may be affecting safari

# 2.0.7

Before a user reports an ad via the blacklist wizard, point him to a helper that makes sure he's got up to date subscriptions, and that the ad does not appear in Firefox (if he has Firefox.) (Famlam)

# 2.0.6

Remove an old gmail special case

# 2.0.5

A few blacklist UI fixes (famlam)

# 2.0.4

Subscribe to filter lists when you click on abp:subscribe links on the web. I _still_ do not understand how Famlam pulled this off. Only works in Chrome.

# 2.0.3

Remove a workaround no longer needed

# 2.0.2

Add EasyPrivacy (now that we mostly block resources from downloading) and remove Germany (an out of date filter that EasyList+additional German filters replaces)

# 2.0.1

Resource blocking works in Chrome Stable after all, so get Stable users in on the goodness too.

# 2.0.0

True blocking of resources in Chrome 6. Most resources can be blocked before they are even downloaded. Because Chrome does not fully support resource blocking yet, a few resources will load so quickly that the resource blocker will miss them, and they'll be removed after the fact as usual.

# 1.4.36

Workaround #2 for Safari crashes

# 1.4.35

Custom blacklist editing in Options, now supporting arbitrarily-complex URL-based or CSS-based blacklist and whitelist rules, while still keeping a simple interface for people who aren't comfortable with filter syntax. (famlam)

# 1.4.34

Workaround to avoid safari crashes until safari team fixes safari

# 1.4.33

Prevent empty element flashup in Safari

# 1.4.32

New filter list options (drewish), better element clicking in blacklist wizard (famlam), fix some issues with removing unsubscribed custom filter lists.

# 1.4.31

Fix bug in .30 keeping Safari users from seeing Options page

# 1.4.30

Now supported in Safari as well -- see safariadblock.com

# 1.4.29

Add caching to making CPU usage even better when many DOM nodes are inserted.

# 1.4.28

Fix high CPU usage on sites that insert lots of DOM nodes after loading.

# 1.4.27

Lots of changes:

- Edit support in blacklist UI (by Famlam)
- 'Remove' labels by custom filter lists (by Famlam)
- New filter subscriptions available (by Drewish)
- You can press enter in textboxes on the Options pages to submit data (by Famlam)
- Make blacklist and whitelist more robust against page CSS (by Famlam)

# 1.4.26

5 filter list additions and corrections (by Drewish). A slider on the whitelister, an edit button on the whitelist options page, support for IP whitelisting (by Famlam).

# 1.4.25

Fix regression: we stopped working around a Chrome 4 bug; blacklister can now also create 'href' and 'data' filters.

# 1.4.24

Provide links to filter subscriptions from options page (by famlam).

# 1.4.23

Corrected a couple filter parsing bugs.

# 1.4.22

Workaround Chrome bug regarding removing SCRIPT elements.

# 1.4.21

Theme tweaks

# 1.4.20

Support the $third-party filter directive.

# 1.4.19

Correctly block OBJECTs with multiple < param > tags

# 1.4.18

Point to new options page from youtube

# 1.4.17

Tabbed Options page (by drewish).

# 1.4.16

Fix Google Reader ads, which regressed somewhere at or before v1.4 release; added 'Edit' label after a custom blacklist entry (by famlam).

# 1.4.15

Added changelog link to Options page; improved CSS for blacklister (by drewish and famlam).

# 1.4.14

Add Italian filters.

# 1.4.13

Move custom rules to chromeadblock.com.

# 1.4.12

EasyList+Corset has become just Corset (Korean filters.)

# 1.4.11

Detect and handle bad selector syntax that broke ChinaList.

# 1.4.10

Improved CSS for blacklister.

# 1.4.9

Small fix for when a user manually subscribes to a well-known filterlist.

# 1.4.8

Correct the error message upon internet failure during subscribing to a filter.

# 1.4.7

Add support for type directives in filters, so if they only want to apply to $images and $stylesheets, we don't apply them to $objects.

# 1.4.5-1.4.6

Pointing to the new location of Korean filterlist.

# 1.4.0-1.4.4

Improved and simplified filtering system under the hood.

# 1.3.49

Allow user to close (and never see again) the youtube help message.

# 1.3.48

Revert 1.3.46; it slowed down most websites. Working on a correct solution.

# 1.3.47

Band-aid over badly parsed RuAd filter until a correct solution can be written.

# 1.3.46

Remove, do not just hide, Flash ads, to save CPU.

# 1.3.45

Add X icon to blacklister and whitelister dialogs.

# 1.3.44

Switch back to RuAd Russian filter list.

# 1.3.43

Auto-complete the description field as well.

# 1.3.42

Auto-complete the summary on ad reports from the "Frustrated?" link.

# 1.3.41

Alphabetize filter list (only new users will see the change.)

# 1.3.40

Fix bug that broke the "Update Now" button.

# 1.3.39

Fix slashdot effect from .37, and adhere to 5-day updates per EasyList maintainers' request.

# 1.3.38

Log only successful manual filter subscriptions, to determine which should be added to the standard list.

# 1.3.37

Get latest versions of all filters upon Chrome startup.

# 1.3.36

Improved the beta YouTube ad blocking feature; plus a message telling users how to work around problems or disable the feature if they're having trouble.

# 1.3.35

Handle uppercased blacklist or whitelist manual entries correctly.

# 1.3.34

Standardize whitelist and blacklist UIs more, and do not let CSS from underlying page bleed through.

# 1.3.33

No more alert on acid3 test -- Chrome gets to 100/100 even with AdBlock.

# 1.3.32

Working around a webkit bug in a very general way, so hopefully this is the last changelog entry of this type!

# 1.3.31

Handle ksplice.com

# 1.3.30

Retire "Prevent ad flashup" as an option -- now it is always true.

# 1.3.29

Disallow z-indexes higher than the blacklist wizard's, upon wizard opening. This keeps websites from hiding the wizard behind their ads or other content.

# 1.3.28

Working around a webkit bug.

# 1.3.27

Working around a webkit bug.

# 1.3.26

Working around a webkit bug.

# 1.3.25

Now blocking background image ads.

# 1.3.24

Now handling the '(Adblock' case when importing filters. Working around a webkit bug that has not merged into Chrome stable yet.

# 1.3.22

Working around a webkit bug that has not merged into Chrome stable yet.

# 1.3.21

Tooltip on filter list names showing the URL you are subscribing to.

# 1.3.20

Fixes hole in Options page where a script tag in blacklist would run the script.

# 1.3.19

The adp:subscribe syntax is converted to the proper url. URLs that do not point to filter subscriptions are not supported.

# 1.3.18

Working around a webkit bug that has not merged into Chrome stable yet.

# 1.3.17

Added helpful buttons for contributors.

# 1.3.16

Added a Donate button to the Options page.

# 1.3.15

Remove two experiments from the Contributors section that did not pan out.

# 1.3.14

Possibly fixes bug that makes AdBlock stop working when leaving Chrome open overnight.

# 1.3.13

Fixes bug that let whitelister open multiple dialog boxes.

# 1.3.12

Working around a webkit bug that has not merged into Chrome stable yet.

# 1.3.11

Added YouTube in-video ad blocking. Based heavily on AdThwart's code.

# 1.3.10

Allow blacklist entries in easylist syntax.

# 1.3.9

Created an initial CHANGELOG file.

# 1.3.8

Fixed a problem with converting to the new Russian list.

# 1.3.7

Added Danish filter subscription.

# 1.3.6

Working around a webkit bug that has not merged into Chrome stable yet.

# 1.3.5

Point to a new Russian subscription list.

# 1.3.4

HTML updates to Options page.

# 1.3.3

Point users to bug tracker on the Options page.

# 1.3.2

Working around a webkit bug that has not merged into Chrome stable yet.

# 1.3.1

Attempt to point to a new Russian subscription list.

# 1.3.0

Initial import.
