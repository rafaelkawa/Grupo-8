
### Questão 3

#Como a estrutura de dados Pilha faz uso da lógica LIFO (o último a entrar é o primeiro a sair), para inverter uma String deve-se inserir letra por letra na pilha até a palavra estar toda empilhada, e depois, tirar letra por letra em uma string.*

!pip install pythonds
from pythonds.basic.stack import Stack

def reverterString(palavra):

    pilha = Stack()     

    for letra in palavra:       
        pilha.push(letra)  

    palavraInvertida = ''            
    while not pilha.isEmpty():
        palavraInvertida = palavraInvertida + pilha.pop()

    return palavraInvertida
print(reverterString("Leo Rocha"))
