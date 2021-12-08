#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import string
import sys
import numpy as np
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from browser import Browser
from yahoo import Yahoo
from globo import Globo
from duck import Duck
from database import Database
from sinonimos import Sinonimos
from google import Google
from news import News
from sklearn.feature_extraction.text import CountVectorizer

sinonimos = Sinonimos()

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]/float(len(s1))

# remove stop words e pontuações
def clear_text(text):
	language = "portuguese"

	#remove stop words
	text = ' '.join([word for word in text.split() if word not in stopwords.words(language)])

	#remove pontuações
	text = text.translate(text.maketrans('', '', string.punctuation))

	return text

# verifica se existem palavras que podem indicar fake news
def check_fake_news(news):
	fake_news_words = ["fake news", "mentira", "falso", "falsa","tendenciosa"]
	text = ''

	# concatena título e corpo da notícia
	for content in news.contents:
		text += clear_text(content.title.lower()) + clear_text(content.text.lower())

	# verifica se exist alguma palavra indicando se é fake news	
	for word in fake_news_words:
	    if word in text:
	    	print('Pode se tratar de uma fake news independente da porcentagem calculada')
	    	break

def check(search, news):
	porcentagem = 0
	search_words = search.lower().split()

	# para cada notícia
	for content in news.contents:
		# concatena título com corpo e depois split no texto
		news_words = (clear_text(content.title.lower()) + clear_text(content.text.lower())).split()
		words_exists = {}

		# verifica se cada palavra da pesquisa existe na notícia
		# se a palavra existir no texto, é salvo a palavra e sua posição no texto
		for search_word in search_words:
		    for i in range(len(news_words)):
		    	news_word = news_words[i]

		    	# compara palavra do texto com e sem sinonimo
		    	if levenshtein(search_word, news_word) < 0.2 or levenshtein(sinonimos.find(news_word), search_word) < 0.2:
		    		if words_exists.get(search_word) is None:
		    			words_exists[search_word] = [] # cria array associado a palavra

	    			# salva posição no array da palavra encontrada
		    		words_exists[search_word].append(i);

		# só faz cálculo se achar mais de uma palavra na notícia
		if len(words_exists) > 1:
			# determina porcentagem das palavras da pesquisa que existem na notícia independente da posição
			words_perc = len(words_exists)/len(search_words) * 100
			positions = []

			# insere primeira posição de cada palavra
			for word in words_exists:
				for pos in words_exists[word]:
					positions.append(pos)
			positions.sort()

			best_distance = 99999
			best_positions = []

			# Determina a melhor distância entre as palavras
			# exemplo: "agnaldo timoteo morreu" 
			# Encontrou posições das palavras na notícia:
			#    "agnaldo" = [5, 10, 22]
			#    "timoteo" = [7, 11, 25]
			#    "morreu"  = [9, 12, 26]
			# Então as posições mais proximas de todas palavras
			# ficaria as posições: (10, 11, 12)
			# Então é calculado a distância entre as posições (10, 11, 12) pois 
			# é a sequência de palavras mais próxima. Nesse caso 0% de desconto
			# pois não existe palavras entre as palavras da sequência
			for i in range(len(positions) - len(words_exists) + 1):
				p = positions[i]
				w = inside(words_exists, p)		
				ars = [p]	

				c = 1
				for pos2 in positions:
					if c == len(words_exists):
						break;

					if pos2 <= p:
						continue;

					if inside(words_exists, pos2) == w:
						continue;

					exists = 0
					for pa in ars:
						if inside(words_exists, pa) == inside(words_exists, pos2):
							exists = 1
							break;

					if exists == 1:
						continue;

					w = inside(words_exists, pos2)
					ars.append(pos2)
					c += 1

				if len(ars) == len(words_exists):
					dist = distance(ars)

					#print(ars)
					if dist < best_distance:
						best_distance = dist
						best_positions = ars

			#print(positions)
			#print(words_exists)
			#print(best_positions)

			# quantidade de palavras entre a sequência vezes a "penalidade"
			space = distance(best_positions)

			# multiplica qtd palavras pela "penalidade"
			space_perc = space * 7.5;

			#print(words_perc * ((100-space_perc)/100))
			#print()

			if space_perc < 100:	
				porcentagem += words_perc * ((100-space_perc)/100)

	return porcentagem/len(news.contents)

def inside(words, pos):
	for word in words:
		for pn in words[word]:
			if pn == pos:
				return word

	return ""

# retorna quantidade de palavras entre a sequência
def distance(positions):
	distance = 0
	for i in range(len(positions)-1):
		distance += positions[i+1] - positions[i] - 1

	return distance

###################################################################################################
###################################################################################################
###################################################################################################
nltk.download('stopwords')

search = clear_text(sys.argv[1])

news = News()

web_browser = Browser()
web_browser.init()

yahoo = Yahoo()
yahoo.find(web_browser, search, news)

duck = Duck()
duck.find(web_browser, search, news)

google = Google()
google.find(web_browser, search, news)

#for content in news.content#f:
	#print(content.titl#f)
	#print(content.text)
	#print()
#print('Total de noticias: ' + str(len(news.contents)))

perc_total = check(search, news)

print(str('{:.2f}'.format((perc_total))) + "%")
check_fake_news(news)

# salvar no banco de dados
db = Database()
db.save(search, perc_total)

web_browser.quit()