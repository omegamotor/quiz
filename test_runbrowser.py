import unittest
from selenium import webdriver
from django.test import TestCase
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\Robert\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe')

    def test_something(self):
        self.assertEqual(True, True)

    def test_browser(self):
        self.browser.get('http://localhost:8000')

        self.header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('h1', self.header_text)


    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
