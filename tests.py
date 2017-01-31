import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WebsiteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

        # navigate to my website: https://al11588.github.io/ 
        self.browser.get('https://al11588.github.io/')

        #1. testing Github button.
    def testNumber1(self):
    	#clicks GitHub button
        github = self.browser.find_element_by_css_selector("a.fa-github").click()
        #clicks on repository text
        repositories = self.browser.find_element_by_css_selector("a.underline-nav-item").click()
        #clicks on python worshop text
        pythonworkshop = self.browser.find_element_by_link_text("PythonWorkshopDay1").click()
        #clicks on add number comparison text
        addnumbercomparison = self.browser.find_element_by_link_text("Add Number Comparison").click()
        #refreshes page
        self.browser.refresh()
        
        #cleans up actions 
    def tearDown(self):
        self.browser.close()





if __name__ == '__main__':
    unittest.main() 