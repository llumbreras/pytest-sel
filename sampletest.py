from selenium import webdriver
import unittest
import sys

class SampleTestCase(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(desired_capabilities={
			"browserName": "firefox",
			"platform": "Ubuntu"
			})

	def test_sample(self):
		self.driver.get("http://www.google.com")
		self.assertEqual(self.driver.title, "Google")

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()

