'''
SISTEMAS DE PERGUNTAS E RESPOSTAS
'''

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '15',},
        'resposta_certa': 'b',
    },    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6',},
        'resposta_certa': 'c',
    },    'Pergunta 3': {
        'pergunta': 'Quanto é 10-7? ',
        'respostas': {'a': '3', 'b': '4', 'c': '10',},
        'resposta_certa': 'a',
    },    'Pergunta 4': {
        'pergunta': 'Quanto é 2/2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '15',},
        'resposta_certa': 'a',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha a opção correta: ')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('CERTA RESPOSTA! rs')
        respostas_certas += 1
    else:
        print('ERROOOOOU, BURRO PRA CARALHO!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')