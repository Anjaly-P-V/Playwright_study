import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.expedia.co.in/")
    page.get_by_role("button", name="Where to?").click()
    page.get_by_placeholder("Going to").fill("kochi")
    page.get_by_placeholder("Going to").click()
    page.get_by_placeholder("Going to").press("Enter")
    page.get_by_test_id("uitk-date-selector-input1-default").click()
    page.get_by_role("button", name="Friday 13 September").click()
    page.get_by_role("button", name="Sunday 29 September").click()
    page.get_by_role("button", name="Done").click()
    page.get_by_role("button", name="Search").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
   run(playwright)
