lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda item: item[1], reverse = True)
print(lista)

print(sorted(lista, key=lambda i: i[1]))
print(sorted(lista, key=lambda i: i[1], reverse = True))  # ORGANIZAR POR PREÇO

print(sorted(lista, key=lambda i: i[0]))
print(sorted(lista, key=lambda i: i[0], reverse = True))  # ORGANIZAR POR DESCRIÇÃO