num_sorteado = 18

num_escolhido = int(input("Digite um numero entre 1 a 20: "))

while num_escolhido != num_sorteado:
    print("Você errou, tente novamente!!")

    num_escolhido = int(input("Digite um numero entre 1 a 20: "))

print("Parábens você ganhou!!")

# Exemplo 2

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1