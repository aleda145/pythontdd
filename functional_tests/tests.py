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
		charles_list_url=self.browser.current_url
		self.assertRegex(charles_list_url,'/lists/.+')
		self.check_for_row_in_list_table('1: buy milk')
		#there is still a textbox inviting him to add another item
		#charlers enters "drink milk"
		inputbox=self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('drink milk')
		inputbox.send_keys(Keys.ENTER)

		#the page updates and now shows both items on  his list
		self.check_for_row_in_list_table('1: buy milk')
		self.check_for_row_in_list_table('2: drink milk')

		#now a new user Francis, comes along to the sit.

		## we use a new browser session to make sure that no information
		## from charles' session is coming through cookies

		self.browser.quit()
		self.browser=webdriver.Firefox()

		#francis vsists the home page There is no sign of charles' list

		self.browser.get(self.live_server_url)
		page_text=self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy milk', page_text)
		self.assertNotIn('make a fly', page_text)

		#francis starts a new list by entering a new item
		# He is less interesting then Charles
		inputbox=self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock')
		inputbox.send_keys(Keys.ENTER)

		#Francis gets his own unique URL
		francis_list_url=self.browser.current_url
		self.assertRegex(francis_list_url,'/lists/+')
		self.assertNotEqual(francis_list_url, charles_list_url)

		#again there is not trace of charles' url
		page_text=self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy milk',page_text)
		self.assertIn('Buy peacock', page_text)


	def test_layout_and_styling(self):
		#Charles visits the home page
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)
		#the input box is nicely centered
		#charles is pleased
		inputbox=self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta=5)

		#charles inputs an item and sees that it is nicely centered
		#charles is pleased
		inputbox.send_keys('testing\n')
		inputbox=self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta=5)

		self.fail('Finish the test')
		#he visits the url and sees his todo list

		#being happy he goes back to sleep

