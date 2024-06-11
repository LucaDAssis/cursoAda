
"""for variavel in range(5):
    print(variavel)

#começando em 1 e terminado em 10 exemplo ele começa no numero da primeira viruga e termnar no segundo numero menos 1
for variavel in range(1, 11):
    print(variavel)

#aqui ele começa no primeiro numero e para no segundo numero pulando de acordo com o terceiro numero que coloquei
for variavel in range(1, 12, 3):
    print(variavel)"""

soma = 0
for i in range(1, 4):
    nota = float(input(f"informe sua nota{i}: "))
    soma = soma + nota
print(soma/3)