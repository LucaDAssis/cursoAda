# Listas

notas = [7.9, 8.7, 9.8]

# Criando Listas

lista = []
lista = list()
lista = [26, "Lucas Assis", 3.14, True]
lista_de_listas = [10, [1, 2, 3]]

# indexação e Slices (fatiamento)

lista = [26, "Lucas Assis", 3.14, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Slices

lista = [10, 20, 30, 40, 50, 60, 70, 80]

#aqui estou printando os indices 0 1 e 2 no caso 10, 20 e 30
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[0:3:2])

# interação com o For

# utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

print("Complemento da lista", len(lista))

for i in range(len(lista)):
    print(lista[i])

# append

print("Antes do Append", lista)

lista.append(3)

print("Depois do Append", lista)

# insert

lista.insert(2, 19)

print("Depois do Insert", lista)

# Extend

lista2 = [1, 2, 3]
lista.extend(lista2)

print("Depois do Extend", lista)

# Pop

lista.pop()

print("Lista depois do Pop", lista)

lista.pop(0)
print("Lista dpois do Pop especifico", lista)

# remove

lista.remove(3)

print("Lista depois do Remove", lista)

# count para contar quantos tem na lista por exemplo quantos Lucas tem na lista
# Index para saber qual a posição da lista
# Sort serve pra ordenar a lista de forma crescente
# pra fazer decrecente tem um reserve

#Funções para listas

# len 
print(len(lista))

# sum
print(sum(lista))

# max
print(max(lista))

# min
print(min(lista))


