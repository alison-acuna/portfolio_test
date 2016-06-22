from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import re

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get('http://www.alisonacuna.com/')

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        # User navigates to the website and notices that Alison is a Full Stack Developer
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Full Stack Web Developer', header_text)
        # User finds the About section and reads about Alison
        title_text = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual('About', title_text)
        # User moves to the work section and looks over Alison's work
        self.browser.get("http://www.alisonacuna.com/work")
        # User navigates back to the home page 
        self.browser.back()


if __name__ == '__main__':
    unittest.main()
    # this allows the tests to run
