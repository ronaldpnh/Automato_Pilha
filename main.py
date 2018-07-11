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

'''
def testepv(estado, regras, pilha):
	# estado atual, conjunto de regras e a pilha
	for regra in regras:
		if (estado == regra[0]) and (regra[1] == "?") and (r_pilha == "?"):
			if pilha == []:
				print("(" + regra[0] + ", " + regra[1] +", "+ 
					r_pilha + ") = ("+ prox_estado +", "+ w_pilha+
					") - Teste da pilha vazia [YES]")
				return True
			else:
				print("(" + regra[0] + ", " + regra[1] +", "+ 
					r_pilha + ") = ("+ prox_estado +", "+ w_pilha+
					") - Teste da pilha vazia [NOT]")
				return False
'''


def printar(estado, letra, r_pilha, prox_estado, w_pilha, pilha):
	if w_pilha != "_":
		if len(w_pilha)>1:
			for c in w_pilha:
				pilha.append(c)
		else:
			pilha.append(w_pilha)
			
	print("(" + estado + ", " + letra +", "+ r_pilha + ") = ("+ prox_estado +", "+ w_pilha+ ") - Pilha = {}".format(pilha))
	return (True,prox_estado)


def testepv(pilha, r_pilha, letra):
	if (len(pilha)==0) and (r_pilha=="?") and (letra == " "):
		return True
	return False

def leituraDaPalavra(inicial, finais, regras, alfapilha):
	palavra = sys.argv[2]
	palavra += " "
	estado_atual = inicial[0]
	pilha = []

	
	for letra in palavra:
		validacao = False

		for regra in regras:
			estado, simbolo, r_pilha, prox_estado, w_pilha = regra
			if (estado==estado_atual) and ((simbolo == letra) or (simbolo=="?")):				
				#print(regra)
				if testepv(pilha, r_pilha, letra):
					validacao, estado_atual = printar(estado, letra, r_pilha, prox_estado, w_pilha, pilha)
					break


				elif r_pilha == "_":
					validacao, estado_atual = printar(estado, letra, r_pilha, prox_estado, w_pilha, pilha)
					break

				elif (len(pilha)>0) and (r_pilha==pilha[-1]):
					pilha.pop()
					validacao, estado_atual = printar(estado, letra, r_pilha, prox_estado, w_pilha, pilha)
					break

				
				"""
				if r_pilha != "_":
					if (pilha != []) and (r_pilha == pilha[-1]):
						lido = pilha.pop()
					else:
						print("Não é possível desempilhar: Pilha Vazia ou Elemento não existente")
						return False
				"""

		if not validacao:
			return False

	if estado_atual in finais:
		return True
	else:
		return False


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
