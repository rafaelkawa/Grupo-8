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