from playwright.sync_api import sync_playwright
import time

FACEBOOK_URL = "https://www.facebook.com/your.page.or.profile.url"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open Facebook
    page.goto(FACEBOOK_URL, timeout=0)

    print("➡️ Log in manually, apply the 2025 filter, then press ENTER here")
    input()

    # Auto-scroll to load all posts
    last_height = 0
    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Save to PDF
    page.pdf(
        path="facebook_posts_2025.pdf",
        format="A4",
        print_background=True
    )

    browser.close()
    print("✅ PDF saved as facebook_posts_2025.pdf")