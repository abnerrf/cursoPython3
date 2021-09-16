while True:
    reverso = 10
    cpf = input('Digite o seu CPF: ')
    new_cpf = cpf[:-2]
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

    sequencia = new_cpf == str(new_cpf[0]) * 11  # Evita CPFs em sequencia
    if cpf == new_cpf and not sequencia:
        print('Válido!')
    else:
        print('Inválido!')