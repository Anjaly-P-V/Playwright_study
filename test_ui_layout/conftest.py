import pytest
from playwright.async_api import Playwright

@pytest.fixture
def set_up(page):

    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()


    yield page

    page.close()