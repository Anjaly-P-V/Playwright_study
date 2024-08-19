import time

import pytest
from playwright.sync_api import Playwright ,expect
from pom.facebook_LogIn import LogIn


@pytest.mark.parametrize("email", [pytest.param("fake@email.com", marks= pytest.mark.xfail),
                                            pytest.param("abcd@gmail.com", marks=pytest.mark.xfail),
                                            "anjudamayanthy@gmail.com"])
@pytest.mark.parametrize("passwrd", [pytest.param( "asdff", marks= pytest.mark.xfail),
                                            pytest.param( "wdvbgt" , marks=pytest.mark.xfail), "Anjudama@test"])
def test_fb(set_up, email, passwrd):
    page = set_up
    page.goto("https://www.facebook.com/")
    login = LogIn(page)
    login.user_name.fill(email)
    login.password.fill(passwrd)
    login.logInButton.click()
    #expect(page.get_by_placeholder("Search Facebook")).to_be_visible(timeout=7000)



@pytest.mark.skip
def test_fb_1(set_up) :
    page = set_up
    page.goto("https://www.facebook.com/")
    login = LogIn(page)
    login.user_name.fill("Anjaly")
    login.password.fill("asdfg")
    login.logInButton.click()
    #time.sleep(15)













# with sync_playwright() as playwright:
#     test_fb(playwright)