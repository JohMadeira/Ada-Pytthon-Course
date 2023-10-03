# ESTRUTURAS CONDICIONAIS

idade = 30

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

media = float(input('Informe sua média: '))
if media >= 7:
    print('Aprovada(o)')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovada(o)!!')


media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado')