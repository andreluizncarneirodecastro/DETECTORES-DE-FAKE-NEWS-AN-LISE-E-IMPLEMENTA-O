from selenium import webdriver
import urllib

class Globo:
    def __init__(self):
        pass

    def find(self, browser, search, news):
        # Parâmetros
        # Agnaldo timoteo morreu ===>>> Agnaldo+timoteo+morreu
        params = {'q' : search}
        encoded_params = urllib.parse.urlencode(params)

        # Página
        browser = browser.get()
        browser.get('https://www.globo.com/busca/?' + encoded_params)

        # Elementos
        contents = browser.find_elements_by_xpath("//div[@class='widget--info__text-container']/a")

        for content in contents:
            title = content.find_element_by_xpath("div[@class='widget--info__title product-color ']").text
            text = content.find_element_by_xpath("p[@class='widget--info__description']").text

            news.add(title, text)