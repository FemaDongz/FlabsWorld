
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get the absolute path to the HTML file
        html_file_path = os.path.abspath('test 1.html')

        # Open the local HTML file
        await page.goto(f'file://{html_file_path}')

        # Take a screenshot of the main view
        await page.screenshot(path='jules-scratch/screenshot_main_view.png')

        # Click the sidebar toggle button to open the sidebar
        await page.click('#sidebar-toggle-btn')

        # Wait for the sidebar to be visible (optional, but good practice)
        await page.wait_for_selector('.sidebar.visible')

        # Take a screenshot of the view with the sidebar open
        await page.screenshot(path='jules-scratch/screenshot_sidebar_view.png')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
