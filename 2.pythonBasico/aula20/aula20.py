'''
While / Else
contadores acumuladores
'''

cont = 1
acumulador = 1

while cont <= 10:
    print(cont, acumulador)

    acumulador += cont
    cont += 1
else:
    print('Cheguei no else.')