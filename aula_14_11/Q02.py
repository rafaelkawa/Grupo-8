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

## Interview Question 3
def somaTarget(self, listaNum,target):
    hashmapNum = {}
    # primeiro adiciona td no hashmap
    for i, num in enumerate(listaNum):
        alvoFinal = target - num  
        if alvoFinal in hashmapNum:
            return [i, hashmapNum[alvoFinal]]
        else: 
            hashmapNum[value] = i
## Interview Question 4

class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None

class ListaEncadeada:
    def __init__(self,head=None):
        self.head= None

    def add(self,value):
        novoNo = Node(value)
        if (self.head is None):
            self.head = novoNo
            return self.head.value
        aux = self.head
        while aux.prox:
            aux = aux.prox
        aux.prox = novoNo

    def printLista(self):
      if self.head is None:
          return ""

      node = self.head
      while node:
          print(node.value, end = "   ")
          node = node.prox

    def removerDuplicados(self,head):
        aux = head
        while aux and aux.prox:
            if aux.value == aux.prox.value:
                aux.prox = aux.prox.prox
            else:
                aux = aux.prox
        return head

if __name__ == '__main__':
    lista = ListaEncadeada()
    lista.add(1)
    lista.add(2)
    lista.add(2)
    lista.add(2)
    lista.add(3)
    lista.add(3)
    lista.add(4)
    lista.add(5)
    lista.add(5)
    lista.add(5)
    print(f'A lista atualmente é:')
    lista.printLista()
    print('\n')

    lista.head = lista.removerDuplicados(lista.head)
    print('\n Removendo Valores Duplicados...')
    lista.printLista()
    print('\n')

# Interview Question 5
 def kthSmallest(self, raiz, k):
         count = self.getNodes(raiz.esq)
         if count+1 < k:
             return self.kthSmallest(raiz.dir, k-count-1)
         elif count+1 == k:
             return raiz.val
         else:
             return self.kthSmallest(raiz.esq, k)

     def getNodes(self, raiz):
         if not raiz:
             return 0
         return 1 + self.getNodes(raiz.esq) + self.getNodes(raiz.dir)

