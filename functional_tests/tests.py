from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest


class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def check_for_row_in_list_table(self, row_text):
		self.browser.get(self.live_server_url)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Enter the homepage
		self.browser.get(self.live_server_url)
		
		# Does the page title and header mention to-do lsits?
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		# Eter the To-Do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		# Type in text for the first element
		inputbox.send_keys('Buy peacock feathers')
		
		# After hitting enter the page updates with a new item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		
		# Type in some more text for the second element
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		
		# Assert for two items in a list table
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		
		## Now it's Francis' turn. He revisits site and makes suere  there is no trace of Edith's #
		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		page_text = self.browser.fing_element_by_tag_name('body')
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)
		
		# Francis adds a new item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		
		# Franics gets his own unique URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)
		
		# Again, there is no trace of Edith's list
		page_text = self.browser.find_element._by_tag_name('body')
		self.assertNotIn('Buy milk, page_text')
		
		# Satisfied, they both go back to sleep together
		self.assertFail('Need to implement more tests')
