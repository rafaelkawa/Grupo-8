# 4. O algoritmo recursivo de inserção em árvore binária de busca apresentado é bastante simples e reflete bem a estrutura da própria árvore. 
#Não será possível também realizar a função deste algoritmo com um algoritmo iterativo? 
#Crie um algoritmo iterativo para a inserção simples em uma árvore binária de busca

# classe nó da Árvore
class No:
    def __init__(self, val=0, esq=None, dir=None):  #construtor do nó
        self.val = val
        self.esq = esq
        self.dir = dir
    def__init__()

def inserirBST(self, raiz, val):
	if not raiz:
		return No(val)

	aux = raiz

	while aux:
		if val < aux.val: # olha se o val e menor que o valor a ser inserido
			if not aux.esq: # vé se o nó é uma folha
				aux.esq = No(val)
				break
			aux = aux.esq
		else:   # olha se o val eh maior que o valor a ser inserido
			if not aux.dir: #ve se o nó eh uma folha
				aux.dir = No(val)
				break
			aux = aux.dir

	return raiz