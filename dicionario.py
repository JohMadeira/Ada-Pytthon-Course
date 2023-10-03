# CRIANDO DICIONARIOS

def criando(op='1'):
    dicionario = {}
    dicionario = dict()

    dicionario = { 'nome': 'Jonathan', 'idade': 30, 'altura': 1.6 }

    if op != '1':
        print(dicionario)
        print(dicionario['idade'])
    
    return dicionario

# ADICIONANDO ITENS
def adicionando(dicionario):
    dicionario['programador'] = True

    print(dicionario)

    dicionario['altura'] = 2

    print(dicionario)

# ITERAÇÃO
def iteracao(dicionario):
    for chave in dicionario:
        print(chave, dicionario[chave])

# TESTANDO EXISTENCIA
def teste(dicionario):
    print('peso' in dicionario)
    print('altura' in dicionario)

criando(2)
adicionando(criando())
iteracao(criando())
teste(criando())