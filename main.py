import re, sys

def leArquivo():
	arquivo = open(sys.argv[1], "r")
	automato = []
	##-----Adiciona cada linha na lista-----
	for linha in arquivo:
		automato.append(linha)
	##--------------------------------------
	arquivo.close()
	return automato

def limpaPrimeiraLinha(automato):
	primeira_linha = automato[0]
	regex = re.compile(r'\{[^\}]*\}')
	dados = re.findall(regex, primeira_linha)
	result = []
	for elemento in dados:
		result.append(elemento.strip("{}").replace(" ", "").split(","))
	return result

def buscaEstadoInicial(automato):
	primeira_linha = automato[0]
	regex = re.compile(r"Z|,\sq\w*,\s{")
	dado = re.findall(regex, primeira_linha)
	inicial = [elemento.strip(",{ ") for elemento in dado]
	return inicial

def leRegrasDeTransicao(automato):
	regras = []
	for i in range(1, len(automato)):
		automato[i] = automato[i].strip("\n").replace(" ", "").split(",")
		regras.append(automato[i])
	return regras

def testepv(estado, regras, pilha):
	# estado atual, conjunto de regras e a pilha
	for regra in regras:
		if (estado == regra[0]) and (regra[1] == "?") and (regra[2] == "?"):
			if pilha == []:
				print("(" + regra[0] + ", " + regra[1] +", "+ 
					regra[2] + ") = ("+ regra[3] +", "+ regra[4]+
					") - Teste da pilha vazia [YES]")
				return True
			else:
				print("(" + regra[0] + ", " + regra[1] +", "+ 
					regra[2] + ") = ("+ regra[3] +", "+ regra[4]+
					") - Teste da pilha vazia [NOT]")
				return False

def leituraDaPalavra(inicial, finais, regras, alfapilha):
	palavra = sys.argv[2]
	estado_atual = inicial[0]
	pilha = []

	i = 0
	for letra in palavra:
		validacao = False

		for regra in regras:
			if (regra[0] == estado_atual) and (regra[1] == letra):

				if regra[4] != "_":
					pilha.append(regra[4])

				estado_atual = regra[3]

				if regra[2] != "_":
					if (pilha != []) and (regra[2] == pilha[len(pilha)-1]):
						lido = pilha.pop()
					else:
						print("Não é possível desempilhar: Pilha Vazia ou Elemento não existente")
						return False

				print("(" + estado_atual + ", " + letra +", "+ 
					regra[2] + ") = ("+ regra[3] +", "+ regra[4]+
					") - Pilha = {}".format(pilha))

				validacao = True
				break
		i += 1

		if not validacao:
			return False

	return testepv(estado_atual, regras, pilha)


def main():
	##-------Le arquivo-----------------------------------
	automato = leArquivo()
	##-------Pega dos dados da primeira linha da lista----
	dados = limpaPrimeiraLinha(automato)
	##-------Busca estado inicial-------------------------
	inicial = buscaEstadoInicial(automato)
	##-------Le as regras para transicao------------------
	regras = leRegrasDeTransicao(automato)
	##-------Atribui os devidos elementos-----------------
	alfabeto = dados[0]
	estados = dados[1]
	finais = dados[2]
	alfapilha = dados[3]
	##-------Printa as informações------------------------
	print("\n-> Alfabeto: {}".format(alfabeto))
	print("-> Estados: {}".format(estados))
	print("-> Estado Inicial: {}".format(inicial))
	print("-> Estado Final: {}".format(finais))
	print("-> Alfabeto Pilha : {}".format(alfapilha))
	print("-> Regras de Transição: ")
	for regra in regras:
		print(regra)
	print()
	##-------Testa se a palavra e valida ou nao-----------
	print("Processamento: "+ sys.argv[2])
	
	validade = leituraDaPalavra(inicial, finais, regras, alfapilha)
	if validade == True:
		return ("\nPalavra Valida")
	else:
		return ("\nPalavra Invalida")


if len(sys.argv) != 3:
	print("Requer um arquivo txt e uma palavra para processar")
	print("Tente: python3 main.py <arquivo-txt> <palavra>")
else:
	print(main())
