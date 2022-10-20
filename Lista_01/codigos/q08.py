### Questão 8
#Apesar de não ser o algoritmo mais rápido, o bubble sort funciona muito bem para quantidade média de itens a serem ordenados 
from heapq import heappop, heappush

def ordenarRemedios(listaRemedios):
    heap = []
    for remedio in listaRemedios:
        heappush(heap, remedio)

    remediosOrdenados = []

    while heap:
        remediosOrdenados.append(heappop(heap))

    return remediosOrdenados

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(ordenarRemedios(array))
