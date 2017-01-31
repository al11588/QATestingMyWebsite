import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

        # navigate to my website: https://al11588.github.io/ 
        self.browser.get('https://al11588.github.io/')

        #1. testing Linkedin button.
    def testNumber1(self):
    	#clicks linked button
        linkedIn = self.browser.find_element_by_css_selector("a.fa-linkedin").click()


        #searchfield return
    def tearDown(self):
        self.browser.close()





if __name__ == '__main__':
    unittest.main() 