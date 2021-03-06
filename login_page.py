from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "'login' not in current url"    
          
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login is not presented" 

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register is not presented" 