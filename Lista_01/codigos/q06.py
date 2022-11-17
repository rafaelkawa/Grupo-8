#Questão 6
class Node:
    def __init__(self, value):
        self.value = value
        self.prox = None


class ListaEncadeada:
    def __init__(self,head=None):
        self.head = None

    def add(self, value):
      novoNo = Node(value)

      # If empty linked list is given
      if self.head is None:
          self.head = novoNo
          return

      # Traversing the given LL to reach the end
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

    def acharMeio(self):
      meio = self.head
      fim = self.head
      while(fim.prox and fim.prox.prox):
          fim = fim.prox.prox
          meio = meio.prox
      
      return meio

    def removerDuplicados(self,head):
        aux = head
        while aux and aux.prox:
            if aux.value == aux.prox.value:
                aux.prox = aux.prox.prox
            else:
                aux = aux.prox
        return head



if __name__ == '__main__':
    # Start with the empty list
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

    meio = lista.acharMeio()
    print("Nó do Meio: ")
    print(meio.value)

    lista.head = lista.removerDuplicados(lista.head)
    lista.printLista()