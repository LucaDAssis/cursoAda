# função inicial

def saudacao():
    print('Seja Bem Vindo!!')
    print('Aprendendo Python!!')

saudacao() # usar parenteses para chamar a função

# Função com Parâmetros

def saudacao(nome, curso):
    print(f"Seja Bem Vindo, {nome} ")
    print(f'Aprendendo Python!! na {curso}')

saudacao('Lucas', 'AdaTech')

# Função com parâmetros default

def saudacao(nome, curso='Java'):
    print(f"Seja Bem Vindo, {nome} ")
    print(f'Aprendendo Python!! na {curso}')

saudacao('Lucas')

# Funções com Retorno

def soma(num1, num2):
    return num1 + num2
resultado = soma(5,7)

print('O Resultado da soma é, ', resultado)