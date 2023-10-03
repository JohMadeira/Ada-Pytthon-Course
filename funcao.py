# EXEMPLO 1
def saudacao():
    print('Seja bem vindo(a)!')

saudacao()

# EXEMPLO 2
def saudacao(nome, curso='Engenharia de Dados'):
    print(f'Seja bem vindo(a), {nome}!')
    print(f'Você está fazendo o curso de {curso}.')

saudacao('Jonathan')

# EXEMPLO 3
def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)
print('O resultado é', resultado)

# EXEMPLO 4
def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(1,5)
print(resultado)