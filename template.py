from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest
import re

class testOne(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get("https://website")

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
