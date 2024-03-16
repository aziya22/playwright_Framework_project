from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    title = page.title()
    print("Title of the page is, ", title)

    click_btn = page.wait_for_selector("//button[contains(text(),'    click   ')]")
    click_btn.click()
    page.wait_for_timeout(3000)

    # How to find  the total pages
    total_pages = context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)

    new_page = total_pages[1]
    # How to switch to new page
    new_page.bring_to_front()
    print(new_page.title())
    new_page.wait_for_timeout(5000)
    new_page.close()

    page.bring_to_front()
    page.wait_for_timeout(3000)
    browser.close()
