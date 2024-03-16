from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    # Radio button
    radiobtn = page.query_selector('//input[@value="FeMale"]')
    # click and check
    # radiobtn.click()
    radiobtn.check()
    page.wait_for_timeout(3000)
    # validation
    if radiobtn.is_checked():
        print("Passed")
    else:
        print("Failed")

    # Checkbox
    checkbox = page.query_selector('//input[@value="Cricket"]')
    checkbox.check()
    page.wait_for_timeout(3000)
    # validation
    if checkbox.is_checked():
        print("Passed")
    else:
        print("Failed")
