# LISTAS
notas = [7.9, 9.7, 8.2]

# CRIANDO LISTA
lista1 = []
lista2 = list()
lista_de_listas = [10, [1, 2, 3]]

# INDEDXAÇÃO

lista_index = [10, 'Jonathan', 3.1415, True]
print(lista_index[0])
print(lista_index[1])
print(lista_index[2])
print(lista_index[3])

# SLICE

lista_slice = [10, 50, 30, 40, 25, 60, 5]
print(lista_slice[0:3])
print(lista_slice[3:6])
print(lista_slice[3:])
print(lista_slice[2:6:2])

# PERCORRER

for elemento in lista_slice:
    print(elemento)

print(len(lista_slice))

for i in range(len(lista_slice)):
    print(lista_slice[i])