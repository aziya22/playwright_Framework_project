from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) #Here I put headless=false because i wanna see what is happening other wise the playwright scripts are headless=true
    page = browser.new_page()
    page.goto('https://www.google.co.in/')
    title = page.title()
    print("Title of the page is: ",title)
    page.wait_for_timeout(3000) #3000 milli seconds
    browser.close()