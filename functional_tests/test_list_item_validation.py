from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		# Blah blah - long story: Edith tries adding blank items
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# Test error message for imputing blank items
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# Now with text
		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
		self.wait_for_row_in_list_table('1: Buy milk')

		# What a pervert that Edith, she tries empty item again!
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# She receives a similar warning
		self.wait_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# And she can correct it by filling some text in
		self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
		self.wait_for_row_in_list_table('1: Buy milk') 
		self.wait_for_row_in_list_table('2: Make tea')

		self.fail('write me!')

