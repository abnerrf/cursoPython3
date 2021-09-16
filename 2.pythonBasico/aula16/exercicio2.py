"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora: ')

if not hora.isdigit():
    print('Você não digitou um horário valido.')
else:
    hora = int(hora)
    if (0 <= hora <= 11):
        print('Bom dia!')
    elif (12 <= hora <= 17):
        print('Boa tarde!')
    elif (18 <= hora <= 23):
        print('Boa noite!')
    else:
        print('Horário Inválido.')
