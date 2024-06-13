# > Dicionarios

# Criando Dicionários

dicionario = {}
dicionario = dict()

dicionario = {'Nome' : 'Lucas', 'Idade' : 29, 'Altura' : 1.87}
print(dicionario)
print(dicionario['Idade'])

# inserindo elementos no dicionario

dicionario['Programador'] = True
print(dicionario)

# se eu usar a mesma chave vai sobrescrever o valro vou mudar a alutra pra 2
dicionario['Altura'] = 2
print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('Altura' in dicionario)