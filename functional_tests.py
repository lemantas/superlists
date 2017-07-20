from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Enter the homepage
		self.browser.get('http://localhost:8000')
		
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
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		
		# Type in some more text for the second element
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		
		# Check it the table was updated properly
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		
		# check for two items
		self.assertIn('1: Buy peacock feathers', 
			[row.text for row in rows]
		)
		self.assertIn(
			'2: use peacock feathers to make a fly',
			[row.text for row in rows]
		)
		
		# proceed with tests here
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
