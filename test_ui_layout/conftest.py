import time

import pytest
from playwright.async_api import Playwright


@pytest.fixture
def set_up(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    yield page

    page.close()

@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.set_default_timeout(3000)
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill("anjudamayanthy@gmail.com")
    page.get_by_test_id("royal_pass").click()
    page.get_by_test_id("royal_pass").fill("Anjudama@test")
    page.get_by_test_id("royal_login_button").click()
    time.sleep(2)
    context.storage_state(path='state.json')
    yield context
    time.sleep(5)
@pytest.fixture()
def login_set_up(context_creation, browser):
    #context = context_creation
    context = browser.new_context(storage_state='state.jason')
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.set_default_timeout(3000)
    yield page
    time.sleep(3)
    context.close()

    time.sleep(3)
    page.close()


