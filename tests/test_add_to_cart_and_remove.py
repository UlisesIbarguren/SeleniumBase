from seleniumbase import BaseCase
from page_objects import Page


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open("https://www.saucedemo.com/")
        self.type(Page.username, "standard_user")
        self.type(Page.password, "secret_sauce")
        self.click(Page.loginButton)
        self.click("#inventory_container > div > div:nth-child(3) > div.pricebar > button")
        self.click("#shopping_cart_container > a > svg > path")
        self.is_element_visible('#contents_wrapper > div.subheader')
        self.click("#cart_contents_container > div > div.cart_list > div.cart_item > div.cart_item_label > div.item_pricebar > button")
        self.click("#cart_contents_container > div > div.cart_footer > a.btn_secondary")
        self.assert_title("Swag Labs")
        self.is_element_visible("#inventory_filter_container > div")
