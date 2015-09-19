from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser= webdriver.Firefox()

#Charles dickson likes lists, he found a list app online
#he checks it out 
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		self.browser.get('http://localhost:8000')

		#he looks at the page title and it mentions to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
		#he sees that the site gives him a prompt to make a todo item immediately

		#he types "buy milk" into a text box (charles likes milk)

		#when he hits enter, the page updates and now the page lists
		#"1" :buy milk as an item in a to-do list

		#there is still a textbox inviting him to add another item
		#charlers enters "drink milk"

		#the page updates and now shows both items on  his list

		#charles wonders if the site will remember the list
		#then he sees that the site has generated a unique url for him
		#there is some text describing the unique url

		#he visits the url and sees his todo list

		#being happy he goes back to sleep

if __name__=='__main__':
	unittest.main(warnings='ignore')

