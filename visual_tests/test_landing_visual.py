import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_visual_landing(page, assert_snapshot) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    locator = page.get_by_role("heading", name="Logged In Successfully")
    # #expect(locator).to_be_visible()
    assert_snapshot(page.screenshot(full_page=True))

