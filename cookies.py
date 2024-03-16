from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.redbus.in/')

    # Get all the cookies
    my_cookies = context.cookies()
    print(my_cookies)

    # Clear all the cookies
    context.clear_cookies()

    new_cookies = {
        'name': 'aziya',
        'value': 'sbdfsjfsdlfj',  # Changed 'did' to 'value' to match the correct cookie structure
        'domain': 'www.redbus.in',
        'path': '/',
        'secure': True
    }

    # Add the new cookies to the context
    context.add_cookies([new_cookies])

    # Take a screenshot
    page.screenshot(path='test.png')

    # Take full screenshot
    page.screenshot(path='full.png',full_page=True)

    # Close the browser
    browser.close()
