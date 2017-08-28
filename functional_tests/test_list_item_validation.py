from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		# Blah blah - long story: Edith tries adding blank items
		self.browser.get(self.server_url)
		inputbox = self.get_item_input_box()
		inputbox.send_keys('\n')
		inputbox.submit()
		import time
		time.sleep(2)

		# Test error message for imputing blank items
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# Now with text
		inputbox = self.get_item_input_box()
		inputbox.send_keys('Buy milk\n')
		inputbox.submit()
		self.wait_for_row_in_list_table('1: Buy milk')

		# What a pervert that Edith, she tries empty item again!
		inputbox = self.get_item_input_box()
		inputbox.send_keys('\n')
		inputbox.submit()

		# She receives a similar warning
		self.wait_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# And she can correct it by filling some text in
		inputbox = self.get_item_input_box()
		inputbox.send_keys('Make tea\n')
		inputbox.submit()
		self.wait_for_row_in_list_table('1: Buy milk') 
		self.wait_for_row_in_list_table('2: Make tea')

	def test_cannot_add_multiple_items(self):
		# Editute goes to home page and starts a new list
		self.browser.get(self.server_url)
		itembox = self.get_item_input_box()
		itembox.send_keys("Buy wellies")
		itembox.submit()
		self.wait_for_row_in_list_table("1: Buy wellies")

		# She accidentally tires to enter a duplicate item
		itembox = self.get_item_input_box()
		itembox.send_keys("Buy wellies")
		itembox.submit()
		
		# She sees a helpful error message
		self.wait_for_row_in_list_table("1: Buy wellies")	
		error = self.browser.find_element_by_css_selector(".has-error")
		self.assertEqual(error.text, "You've already got this in your list")
