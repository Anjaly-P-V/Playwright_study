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
    # page.wait_for_load_state("networkidle")
    time.sleep(2)
    context.storage_state(path='context_state.json')

    yield context


@pytest.fixture()
def page_creation(context_creation, browser):
    context = browser.new_context(storage_state='context_state.json')
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.set_default_timeout(3000)
    #time.sleep(3)
    yield page
    context.close()




