lista = [1, 3, 12, 8, 2]

print('Lista: ', lista)

lista.append(3)

print('Append: ', lista)

lista.insert(2, 10)

print('Insert: ', lista)

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Extend: ', lista)

lista.pop()

print('Pop: ', lista)

lista.pop(0)

print('Pop indice', lista)

lista.remove(3)

print('Remove', lista)

print('Quantidade de 2: ', lista.count(2))

print('Indice elemento 12: ', lista.index(12))

lista.sort()

print('Sort: ', lista)

print('Tamanho: ', len(lista))

print('Soma: ', sum(lista))

print('Maior: ', max(lista))

print('Menor: ', min(lista))