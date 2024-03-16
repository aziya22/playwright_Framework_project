from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    title = page.title()
    print("The title of the page is: ", title)

    # Select Dropdown
    # 1. Find the select dropdown
    # select_dropdown = page.query_selector('//select[@id="Skills"]')
    # 2. Select the option
    # select_dropdown.select_option(label='Android')
    # page.wait_for_timeout(5000)

    # In playwright you don't need to store the dropdown you can directly use select_option
    page.select_option('//select[@id="Skills"]',label='APIs')
    page.wait_for_timeout(5000)
