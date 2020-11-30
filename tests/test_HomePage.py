from seleniumbase import BaseCase
from page_objects import Page


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open("https://www.saucedemo.com/")
        self.type(Page.username, "standard_user")
        self.type(Page.password, "secret_sauce")
        self.click(Page.loginButton)
        self.assert_title("Swag Labs")
        self.is_element_visible('#inventory_filter_container > div')


