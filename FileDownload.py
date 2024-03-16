from playwright.sync_api import sync_playwright


def download_handle(download):
    file_location = './files/test.zip'
    download.save_as(file_location)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.imacros.net/Automate/Downloads')

    page.on('download', download_handle)
    page.wait_for_selector('//a[@href="/Content/Download.zip"]').click()
    page.wait_for_timeout(3000)
