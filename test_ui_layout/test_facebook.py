import os

import pytest

from pom.facebook_LogIn import LogIn

PASSWORD = os.environ['PASSWORD']
# try:
#     PASSWORD = os.environ['PASSWORD']
# except KeyError:
#     import utils.secret_config
#     PASSWORD = utils.secret_config.PASSWORD


@pytest.mark.parametrize("email", [pytest.param("fake@email.com", marks= pytest.mark.xfail),
                                             pytest.param("abcd@gmail.com", marks=pytest.mark.xfail),
                                             "anjudamayanthy@gmail.com"])
@pytest.mark.parametrizpyte("passwrd", [pytest.param( "asdff", marks= pytest.mark.xfail),

                                       pytest.param( "wdvbgt" , marks=pytest.mark.xfail),PASSWORD ])

def test_fb_12(login_set_up, email, passwrd) -> None:
    page=login_set_up



@pytest.mark.skip
def test_fb(login_set_up, email, passwrd):
    page = login_set_up
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