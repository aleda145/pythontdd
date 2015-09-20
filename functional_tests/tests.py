from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser= webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table=self.browser.find_element_by_id('id_list_table')
		rows= table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Charles dickson likes lists, he found a list app online
		#he checks it out 
		self.browser.get(self.live_server_url)

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
		self.check_for_row_in_list_table('1: buy milk')
		#there is still a textbox inviting him to add another item
		#charlers enters "drink milk"
		inputbox=self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('drink milk')
		inputbox.send_keys(Keys.ENTER)

		#the page updates and now shows both items on  his list
		self.check_for_row_in_list_table('1: buy milk')
		self.check_for_row_in_list_table('2: drink milk')
		#charles wonders if the site will remember the list
		#then he sees that the site has generated a unique url for him
		#there is some text describing the unique url
		self.fail('Finish the test')
		#he visits the url and sees his todo list

		#being happy he goes back to sleep
