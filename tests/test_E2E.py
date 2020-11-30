from page_objects import Page
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basic(self):
        self.open("https://www.saucedemo.com/")
        self.type(Page.username, "standard_user")
        self.type(Page.password, "secret_sauce")
        self.click(Page.loginButton)
        self.click(Page.css_4)
        self.click(Page.css_5)
        self.click(Page.css_6)
        self.click(Page.checkOutButton)
        self.type(Page.firstName, "Ulises")
        self.type(Page.lastName, "Ibarguren")
        self.type(Page.zipCode, "1706")
        self.click(Page.css_11)
        self.click(Page.css_12)
        self.assert_exact_text("THANK YOU FOR YOUR ORDER", Page.css_13)
