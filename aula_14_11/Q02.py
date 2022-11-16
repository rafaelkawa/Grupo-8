## Interview Question 1
def acharElementoFaltando():
    # Declarar a lista
    lista = list(range(101))
    lista.remove(0)
    lista.remove(34)
    print(lista)
    for index, item in enumerate(lista):
        # Comparar iterador com o elemento atual do array
        print(index+1,item)
        if (index+1 != item):
            print(f"Elemento Faltando:{index+1}")
            break
acharElementoFaltando()

## Interview Question 2

class Node:
    def __init__(self, val):
    self.value = val
    self.prox = None

class LinkedList:
    def __init__(self,head=None):
        self.head= None

    def add(self,val):
        novoNo = Node(val)
        if (self.head is None):
            self.head = novoNo
            return self.head.val
        
        aux = self.head
        while aux.prox:
                aux = aux.prox
        aux.prox = novoNo
    