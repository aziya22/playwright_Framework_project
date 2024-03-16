from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Selectable.html")

        # Storing multiple elements using list
        elements = page.query_selector_all('b')
        # Providing wrong path to check Try except
        page.query_selector('d//[@shf="efhu"]').click()
        print(f'size of the string: {len(elements)}')
        for i in elements:
            print(i.text_content())
            # text_content() is use to read the text of web element
        page.wait_for_timeout(1500)

        elementss = page.query_selector_all('a')
        print(f'size of the string: {len(elementss)}')
        for i in elementss:
            print(i.get_attribute('href'))
            # text_content() is use to get the attribute of a web element
        page.wait_for_timeout(1500)
    except Exception as e:
        print(str(e))
    finally:
        print("Execute")
