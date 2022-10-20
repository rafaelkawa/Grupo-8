# Criaçao da lista
ls <- list("a"=1, "b"=2, "c"=3)

# Adiçao de um elemnto ao fim
l2 <- append(ls,30)

# Soma dos elementos
print(Reduce('+', l2))
