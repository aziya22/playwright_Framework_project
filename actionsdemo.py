from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Selectable.html')

    # Mouse actions
    # Hover a dropdown
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    page.wait_for_timeout(2000)

    # Click on element
    page.wait_for_selector('//a[text()="SwitchTo"]').click()
    page.wait_for_timeout(2000)

    # Double click
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
    page.wait_for_timeout(2000)

    # Right click on element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button="right")
    page.wait_for_timeout(2000)

    # Shift click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["Shift"])
    page.wait_for_timeout(2000)

    # Keyboard actions
    page.wait_for_selector('//a[text()="SwitchTo"]').press('A')
    # press A-Z, 0-9, F1-F12, All Special Characters, ArrowRight, ArrowDown, PageUp, PageDown, Enter, Shift, Control
    page.wait_for_timeout(2000)