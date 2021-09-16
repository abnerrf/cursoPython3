"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

try:
    num = int(num)
    if num % 2 == 0:
        print('O número digitado é par.')
    else:
        print('O número digitado é impar.')
except:
    print('O número digitado não é um número inteiro.')