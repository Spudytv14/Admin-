import os
from playwright.sync_api import sync_playwright

def verify_updates():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # 1. Screenshot Welcome Page
        page.screenshot(path="verification_welcome.png", full_page=True)
        print("Captured verification_welcome.png")

        # 2. Login Flow
        print("Filling login form...")
        page.fill("#email", "spudytv14@gmail.com")
        page.fill("#password", "muduchwa14")
        page.click("#login-form button[type='submit']")

        # Wait for dashboard to animate in
        page.wait_for_timeout(1000)

        # 3. Navigate to Reports and Screenshot (to verify generic names)
        print("Navigating to Reports...")
        page.click("#nav-reports")
        page.wait_for_timeout(500)
        page.screenshot(path="verification_reports_updated.png", full_page=True)
        print("Captured verification_reports_updated.png")

        browser.close()

if __name__ == "__main__":
    verify_updates()
