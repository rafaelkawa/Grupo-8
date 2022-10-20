
### Questão 5
from collections import deque

def navegarWeb():
  pilha = deque()
  menu = deque()
  menu.append("vazio")
  print(f"Site: {pilha}")
  encerrar = False
  count = 0
  while encerrar != True:
    escolha = int(input("Escolha a navegacão: 1 - Avancar | 2 - Voltar | 3 - Pagina Inicial | 4 - Encerrrar Aplicacao" ))
    if escolha == 1:
      count = count + 1 
      pilha.append(f'pagina{count} >' )
      menu.append(f'pagina{count} >')
      print(menu)
    elif escolha == 2:
      count= count - 1
      pilha.pop()
      menu.append(f'voltar >')
      if count == 0:
        menu.append(f'vazio')
      else:
        menu.append(f'pagina{count} >')
      print(menu)
    elif escolha == 3:
      count = 1
      pilha.clear()
      pilha.append(f'pagina{count} >')
      menu.append(f' voltar pagina inicial')
      menu.append(f'pagina{count}')
      print(menu)
    elif escolha == 4:
      menu.append(f'fechar aplicacao')
      pilha.clear()
      encerrar = True
      print(menu)
  print('finalizado')

navegarWeb()
