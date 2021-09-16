d1 = {
    'chave1' : 'valor',
    'chave2' : 'Outro valor',
    'chave3' : 'Tupla',
}

for k, v in d1.items():
    print(k, v)

clientes = {
    'clientes1' : {
        'nome' : 'Abner',
        'sobrenome' : 'Rodrigues',
    },
    'cleintes2' : {
        'nome' : 'João',
        'sobrenome':'Moreira',
    },
    'cleintes3' : {
        'nome' : 'Maria',
        'sobrenome':'Joaquina',
    },
    'cleintes4' : {
        'nome' : 'Hebert',
        'sobrenome':'Richards',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')