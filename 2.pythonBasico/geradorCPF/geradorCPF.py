from random import randint
numero = str(randint(100000000, 999999999))
reverso = 10
new_cpf = numero
cont = 0
for index in range(19):
    if index > 8:
        index -= 9

    cont += int(new_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (cont % 11)

        if d > 9:
            d = 0
        cont = 0
        new_cpf += str(d)
print(new_cpf)