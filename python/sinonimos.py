import urllib
import time

#map dicionario
active = True
sinonimos = {}
sinonimos['morreu'] = 'faleceu'
sinonimos['faleceu'] = 'morreu'
sinonimos['safar'] = 'evitar'
sinonimos['evitar'] = 'safar'
sinonimos['roubar'] = 'furtar'
sinonimos['furtar'] = 'roubar'
sinonimos['roubou'] = 'furtou'
sinonimos['furtou'] = 'roubou'
sinonimos['deduzir'] = 'concluir'
sinonimos['concluir'] = 'deduzir'
sinonimos['aceitou'] = 'admitiu'
sinonimos['admitiu'] = 'aceitou'
sinonimos['esbanjar'] = 'malgastar'
sinonimos['malgastar'] = 'esbanjar'
sinonimos['esbanjar'] = 'desperdiçar'
sinonimos['desperdiçar'] = 'esbanjar'
sinonimos['cresceu'] = 'aumentou'
sinonimos['aumentou'] = 'cresceu'
sinonimos['melhorou'] = 'aprimorou'
sinonimos['aprimorou'] = 'melhorou'
sinonimos['equilibrou'] = 'estabilizou'
sinonimos['estabilizou'] = 'equilibrou'
sinonimos['aperfeiçoou'] = 'melhorou'
sinonimos['melhorou'] = 'aperfeiçoou'
sinonimos['personalizar'] = 'customizar'
sinonimos['customizar'] = 'personalizar'
sinonimos['otimizou'] = 'aprimorou'
sinonimos['aprimorou'] = 'otimizou'
sinonimos['expurgou'] = 'limpou'
sinonimos['limpou'] = 'expurgou'
sinonimos['disputou'] = 'concorreu'
sinonimos['concorreu'] = 'disputou'
sinonimos['reajustar'] = 'reacerto'
sinonimos['reacerto'] = 'reajustar'
sinonimos['testou'] = 'experimentou'
sinonimos['experimentou'] = 'testou'
sinonimos['dialogou'] = 'discutiu'
sinonimos['discutiu'] = 'dialogou'
sinonimos['atacou'] = 'enfrentou'
sinonimos['enfrentou'] = 'atacou'
sinonimos['atirou'] = 'alvejou'
sinonimos['alvejou'] = 'atirou'
sinonimos['suportou'] = 'aguentou'
sinonimos['aguentou'] = 'suportou'
sinonimos['fracassou'] = 'falhou'
sinonimos['falhou'] = 'fracassou'
sinonimos['abandonou'] = 'afastou'
sinonimos['afastou'] = 'abandonou'
sinonimos['lutou'] = 'enfrentou'
sinonimos['enfrentou'] = 'lutou'
sinonimos['esforçou'] = 'empenhou'
sinonimos['empenhou'] = 'esforçou'
sinonimos['questionou'] = 'discutiu'
sinonimos['discutiu'] = 'questionou'
sinonimos['combateu'] = 'pelejou'
sinonimos['pelejou'] = 'combateu'
sinonimos['combateu'] = 'batalhou'
sinonimos['batalhou'] = 'combateu'
sinonimos['acreditou'] = 'confiou'
sinonimos['confiou'] = 'acreditou'
sinonimos['disputou'] = 'concorreu'
sinonimos['concorreu'] = 'disputou'
sinonimos['matar'] = 'assassinar'
sinonimos['assassinar'] = 'matar'


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

class Sinonimos:
	def find(self, word):
		if active == False:
			return ""

		for sinonimo in sinonimos:
			if levenshtein(sinonimo, word) < 0.2:
				return sinonimos[sinonimo]

		return ""