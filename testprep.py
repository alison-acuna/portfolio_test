
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest
import re

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get('http://www.beingboss.club/')

    def tearDown(self):
        self.browser.quit()

    def testSubscribe(self):
        first_name = self.browser.find_element_by_id("ck_firstNameField")
        first_name.clear()
        first_name.send_keys("Alison")
        email_box = self.browser.find_element_by_id("ck_emailField")
        email_box.clear()
        email_box.send_keys("aacuna136@gmail.com")
        submit = self.browser.find_element_by_id("ck_subscribe_button")
        submit.click()

if __name__ == '__main__':
    unittest.main()
