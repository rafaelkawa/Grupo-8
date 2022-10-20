 Questão 6
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class ListaEncadeada:
    def __init__(self,head=None):
        self.head = None

    def add(self, val):
      novoNo = Node(val)

      # If empty linked list is given
      if self.head is None:
          self.head = novoNo
          return

      # Traversing the given LL to reach the end
      aux = self.head
      while aux.next:
          aux = aux.next
      aux.next = novoNo

    def printLista(self):
      if self.head is None:
          return ""

      node = self.head
      while node:
          print(node.value, end = "   ")
          node = node.next

    def acharMeio(self):
      meio = self.head
      fim = self.head
      while(fim.next and fim.next.next):
          fim = fim.next.next
          meio = meio.next
      
      return meio

if __name__ == '__main__':
    # Start with the empty list
    lista = ListaEncadeada()
    lista.add(1)
    lista.add(2)
    lista.add(3)
    lista.add(4)
    lista.add(5)
    print(f'A lista atualmente é:')
    lista.printLista()
    print('\n')

    meio = lista.acharMeio()
    print("Nó do Meio: ")
    print(meio.value)