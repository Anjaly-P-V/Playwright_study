import re
import time

import pytest
from playwright.sync_api import Playwright,  expect


@pytest.mark.xfail(reason="time out")
def test_run(set_up) :
    page = set_up
    page.goto("https://www.amazon.in/")
    # page.get_by_test_id("royal_email").click()
    # page.get_by_test_id("royal_email").fill("anjalyviswambharan@gmail.com")
    # page.get_by_test_id("royal_pass").click()
    # page.get_by_test_id("royal_pass").fill("mehulsuvan")
    # page.get_by_test_id("royal_login_button").click()
    # expect(page.get_by_placeholder("Search Facebook")).to_be_visible(timeout=7000)
    page.click("text='Sell'")
    print("Sucess!")
    # ---------------------
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     test_run(playwright)
