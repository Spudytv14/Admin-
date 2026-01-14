import os
from playwright.sync_api import sync_playwright

def verify_premium():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # 1. Screenshot Login Page (Gold Theme)
        page.screenshot(path="verification_01_login_gold.png")
        print("Captured verification_01_login_gold.png")

        # 2. Login Flow
        print("Filling login form...")
        page.fill("#email", "spudytv14@gmail.com")
        page.fill("#password", "muduchwa14")
        page.click("#login-form button[type='submit']")

        # Wait for dashboard to animate in (animation is 0.8s)
        page.wait_for_timeout(2000)

        # 3. Verify Admin Name
        content = page.content()
        if "Admin Matipaishe" in content:
            print("SUCCESS: Found 'Admin Matipaishe' on the dashboard.")
        else:
            print("FAILURE: Could not find 'Admin Matipaishe'.")

        # 4. Screenshot Overview (Hero + Shortcuts)
        page.screenshot(path="verification_02_overview_premium.png", full_page=True)
        print("Captured verification_02_overview_premium.png")

        # 5. Navigate to Reports to check Tables in Gold
        print("Navigating to Reports...")
        page.click("#nav-reports")
        page.wait_for_timeout(1000)
        page.screenshot(path="verification_03_reports_premium.png", full_page=True)
        print("Captured verification_03_reports_premium.png")

        browser.close()

if __name__ == "__main__":
    verify_premium()
