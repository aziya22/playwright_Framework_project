from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()
    page1.goto('https://www.saucedemo.com/')
    title = page1.title()
    print('Title of the page is: ', title)

    # CSS Selector usage

    # 1. Using Id
    username = page1.wait_for_selector('#user-name')
    username.type('error_user')
    password = page1.wait_for_selector('#password')
    password.type('secret_sauce')
    page1.wait_for_timeout(3000)
    login_btn = page1.wait_for_selector('#login-button')
    login_btn.click()
    page1.wait_for_timeout(3000)

    page2 = browser.new_page()
    page2.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    title = page2.title()
    print("Title of the page is: ",title)

    #2. Using Attribute
    username1 = page2.wait_for_selector('input[name="username"]')
    username1.type('Admin')
    password1 = page2.wait_for_selector('input[name="password"]')
    password1.type('admin123')
    page1.wait_for_timeout(3000)
    login_btn1 = page2.wait_for_selector('button[type="submit"]')
    login_btn1.click()
    page2.wait_for_timeout(3000)