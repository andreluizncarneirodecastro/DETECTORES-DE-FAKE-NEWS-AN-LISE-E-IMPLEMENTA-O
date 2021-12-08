from selenium import webdriver
import urllib
import time

class Duck:
	def __init__(self):
		pass

	def find(self, browser, search, news):
		# Parâmetros
		params = {'q' : search}
		encoded_params = urllib.parse.urlencode(params)

		# Página
		browser = browser.get()
		browser.get('https://duckduckgo.com/?' + encoded_params)

		# Elementos
		contents = browser.find_elements_by_xpath("//div[@id='links']/div[@class='result results_links_deep highlight_d result--url-above-snippet']")

		for content in contents:
			try:
				title = content.find_element_by_xpath("div/h2/a").text
				text = content.find_element_by_xpath("div/div[@class='result__snippet js-result-snippet']").text

				news.add(title, text)
			except:
				continue