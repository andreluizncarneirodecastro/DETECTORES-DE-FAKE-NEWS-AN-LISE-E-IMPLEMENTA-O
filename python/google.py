from selenium import webdriver
import urllib
import time

class Google:
	def __init__(self):
		pass

	def find(self, browser, search, news):
		# Parâmetros
		params = {'q' : search}
		encoded_params = urllib.parse.urlencode(params)

		# Página
		browser = browser.get()
		browser.get('https://www.google.com/search?' + encoded_params)

		# Elemetos
		contents = browser.find_elements_by_xpath("//div[@id='rso']/div[@class='g']")


		for content in contents:
			try:
				title = content.find_element_by_xpath("div/div/div/a/h3").text
				text = content.find_element_by_xpath("div/div/div[2]/div").text
				
				news.add(title, text)
			except:
				continue