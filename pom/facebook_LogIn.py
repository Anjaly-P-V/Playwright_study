

class LogIn:
    def __init__(self, page):
        self.user_name = page.get_by_test_id("royal_email")
        self.password = page.get_by_test_id("royal_pass")
        self.logInButton = page.get_by_test_id("royal_login_button")