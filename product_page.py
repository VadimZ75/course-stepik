from .base_page import BasePage
from .locators import PageObjectLocators
from selenium.webdriver.common.by import By

class PageObject (BasePage):
	def product_add_to_basket(self):
		add_to_basket_link =  self.browser.find_element(*PageObjectLocators.add_to_basket)
		add_to_basket_link.click()
	def product_and_massege_present(self):	
		assert self.is_element_present(*PageObjectLocators.PRODUCT_NAME), "PRODUCT_NAME not presented"
		assert self.is_element_present(*PageObjectLocators.MESSAGE_ABOUT_ADDING), "Massage not presented"
		product_name = self.browser.find_element(*PageObjectLocators.PRODUCT_NAME).text
		message = self.browser.find_element(*PageObjectLocators.MESSAGE_ABOUT_ADDING).text
		y = len(message) - len(product_name)
		assert product_name in message, "No product name in the message"
		assert y == 29, "No product"
	def should_be_message_basket_total(self):
	    assert self.is_element_present(*PageObjectLocators.BASKET_VOLUME), "Basket volume is not presented"
	    assert self.is_element_present(*PageObjectLocators.PRODUCT_PRICE), "Product price is not presented"
	    basket_volume = self.browser.find_element(*PageObjectLocators.BASKET_VOLUME).text
	    product_price = self.browser.find_element(*PageObjectLocators.PRODUCT_PRICE).text
	    assert product_price in basket_volume, "No product price in the basket"
	def should_not_be_message(self):
	    assert self.is_not_element_present(*PageObjectLocators.MESSAGE_ABOUT_ADDING), "Success message is presented, but should not be"       