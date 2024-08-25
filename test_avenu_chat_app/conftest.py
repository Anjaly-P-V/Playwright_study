import pytest
from playwright.sync_api import Playwright,expect


@pytest.fixture(scope='session')
def context_1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.chat-avenue.com/general/")
    #page.locator('button:has-text(" Login")').click()
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username/Email").click()
    page.get_by_placeholder("Username/Email").fill("AnjuMehul")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Anju@test24")
    with page.expect_navigation():
        page.get_by_role("button", name="Login")

    yield context

@pytest.fixture(scope='session')
def context_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.chat-avenue.com/general/")
    #page.locator('button:has-text(" Login")').click()
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username/Email").click()
    page.get_by_placeholder("Username/Email").fill("AnjuMehul")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Anju@test24")
    with page.expect_navigation():
        page.get_by_role("button", name="Login")

    yield context


    



@pytest.fixture()
def login_set_up_for_chat(context_1, context_2, browser):
    page1 = context_1.new_page()
    page2 = context_2.new_page()
    page1.goto("https://www.chat-avenue.com/general/")
    page2.goto("https://www.chat-avenue.com/general/")
    page1.set_default_timeout(5000)
    page2.set_default_timeout(5000)

    yield page1, page2
    page1.close()
    page2.close()
