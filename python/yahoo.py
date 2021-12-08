from selenium import webdriver
import urllib
import time

class Yahoo:
	def __init__(self):
		pass

	def find(self, browser, search, news):
		# Parâmetros
		params = {'q' : search}
		encoded_params = urllib.parse.urlencode(params)

		# Página
		browser = browser.get()
		browser.get('https://br.search.yahoo.com/search?' + encoded_params)

		# Elemetos
		contents = browser.find_elements_by_xpath("//div[contains(@class, 'dd algo algo-sr relsrch')]")

		for content in contents:
			try:
				title = content.find_element_by_xpath("div/h3").text
				text = content.find_element_by_xpath("div[@class='compText aAbs']/p").text
				news.add(title, text)
			except:
				continue