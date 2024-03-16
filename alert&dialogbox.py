from playwright.sync_api import sync_playwright
text_alert = []


def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()


def handle_dialog_with_text(dialog):
    message = dialog.type('Aziya Solkar')
    text_alert.append(message)
    dialog.accept()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")
    title = page.title()
    print("Title of the page is: ", title)

    page.wait_for_selector("//div[@id='OKTab']/button").click()
    page.wait_for_timeout(2000)

    page.wait_for_selector("//a[@href='#CancelTab']").click()
    page.wait_for_timeout(2000)
    # Control alert
    # page.on("dialog",lambda dialog: print(dialog.message)) # To print dialog message
    # page.on("dialog",lambda dialog: dialog.accept())
    page.on("dialog", handle_dialog) # We will call our dialog method here
    page.wait_for_selector("//div[@id='CancelTab']/button").click()
    page.wait_for_timeout(2000)
    print(text_alert[0])

    page.wait_for_selector("//a[@href='#Textbox']").click()
    page.wait_for_timeout(2000)
    page.on("dialog", handle_dialog_with_text)
    page.wait_for_selector("//div[@id='Textbox']/button").click()
    page.wait_for_timeout(2000)
    print(text_alert[1])


