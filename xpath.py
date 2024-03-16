from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # xpath - It is use to traverse between webelements
    # Relative xpath
    # Using attribute - //tagname[@attribute="value"]

    page.wait_for_selector('//input[@name="username"]').type('Admin')
    page.wait_for_selector('//input[@placeholder="Password"]').type('admin123')
    # page.wait_for_selector('//button[@type="submit"]').click()
    page.wait_for_timeout(3000)

    # Using text - //tagname[text()="text"]
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    page.wait_for_timeout(3000)

    # using contains
    # attribute - //tagname[contains(@attribute,"value")]
    # //input[contains(@placeholder,'User')]
    # text - //tagname[contains(text(),"")]
    # //label[contains(text(),"Username")]
    page.wait_for_selector('')

    # Using dynamic xpath
    # E.g. aziya12User, aziya22User, aziya638257User
    # starts-with -> //tagname[starts-with(@id,"aziya")]
    # ends-with -> //tagname[ends-with(@id,"User")]

    # Using Family
    # parent - //tagname[@id="xy"]/parent::input[]
    # child - //tagname[@id="xy"]/child::input[]
    # siblings -
    # preceding-siblings -> //td[text()="Argentina"]//preceding-sibling::td[0]
    # following-siblings -> //td[text()="Microsoft"]//following-sibling::td[2]
