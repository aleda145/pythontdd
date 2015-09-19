from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser= webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Charles dickson likes lists, he found a list app online
		#he checks it out 
		self.browser.get('http://localhost:8000')

		#he looks at the page title and it mentions to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text=self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		#he sees that the site gives him a prompt to make a todo item immediately
		inputbox=self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)
		#he types "buy milk" into a text box (charles likes milk)
		inputbox.send_keys('buy milk')
		#when he hits enter, the page updates and now the page lists
		#"1" :buy milk as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		table=self.browser.find_element_by_id('id_list_table')
		rows=table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text== '1: buy milk' for row in rows),
			"new to-do item did not appear in table"
			)
		#there is still a textbox inviting him to add another item
		#charlers enters "drink milk"
		self.fail('Finish the test')
		#the page updates and now shows both items on  his list

		#charles wonders if the site will remember the list
		#then he sees that the site has generated a unique url for him
		#there is some text describing the unique url

		#he visits the url and sees his todo list

		#being happy he goes back to sleep

if __name__=='__main__':
	unittest.main(warnings='ignore')

