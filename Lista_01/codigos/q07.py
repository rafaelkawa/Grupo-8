
### Questão 7

#Resposta: Uma fila do tipo FIFO (First In, First Out)

from queue import Queue

fila = Queue()
def tocar (lista):
  while not lista.empty():
    print(f'\n  Agora esta tocando: {lista.get()}')
  print('Fim da Lista de Músicas')

rodar = True
fila.put(input("Adicione uma Música:  "))
print("Adicionada com Sucesso")
while (rodar):
  decisao = int(input("1 - Adicionar mais uma musica \n 2 - Tocar Playlist \n"))
  if decisao == 1:
    fila.put(input('Digite a música'))
    print("Adicionada com Sucesso")
  if decisao == 2:
    rodar = False
    tocar(fila)