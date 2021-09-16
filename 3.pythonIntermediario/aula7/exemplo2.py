d1 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',
}

d1['str'] = 'Agora ela existe'
d1.update({'nova_chave':'novo_valor'})
del d1[123]

print(d1[(1,2,3,4)])
print(d1.get('nome da chave'))
print(d1.get('str'))
print(d1.get('nova_chave'))
print(d1)
#
print('str' in d1)
print('str' in d1.keys())  # PROCURANDO PELA CHAVE
print('valor' in d1.values())  # PROCURANDO PELO VALOR (deu false pq o valor foi alterado na linha 7)
#
print(len(d1))  # TAMANHO DO DICIONARIO - 3 PARES NO EXEMPLO