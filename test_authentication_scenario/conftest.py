import time

from playwright.sync_api import Playwright
import pytest


@pytest.fixture(scope='session')
def context_creation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.set_default_timeout(3000)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin123")
    page.locator('button[type="submit"]').click()

    yield context


@pytest.fixture()
def page_creation(context_creation):
    context = context_creation
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.set_default_timeout(3000)
    #time.sleep(3)
    yield page




