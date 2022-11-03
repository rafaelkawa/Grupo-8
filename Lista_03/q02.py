#2. Elabore um algoritmo recursivo para efetuar 
#uma busca em uma árvore binária de busca pressupondo as estruturas de dados do exemplo anterior.

# classe nó da Árvore
class No:
    def __init__(self, val=0, esq=None, dir=None):  #construtor do nó
        self.val = val
        self.esq = esq
        self.dir = dir
    def__init__()

class Solution:
    def buscarBST(self, raiz, val):
        if val==raiz.val:
            return raiz
        elif val> raiz.val:
            self.buscarBST(raiz.dir,val)
        elif val< raiz.val:
            self.buscarBST(raiz.esq,val)
