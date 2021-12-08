from selenium import webdriver
import sys, os

class Browser:
	browser = None

	def __init__(self):
		pass

	def init(self):
		options = webdriver.ChromeOptions()
		options.add_argument('headless')
       
		pathname = os.path.dirname(sys.argv[0])        

		self.browser = webdriver.Chrome(executable_path = os.path.abspath(pathname) + "\driver\chromedriver.exe", options = options)

	def getPage(self, link):
		self.browser.get(link)

		return self.browser.page_source
	
	def get(self):
		return self.browser

	def quit(self):
		self.browser.quit()