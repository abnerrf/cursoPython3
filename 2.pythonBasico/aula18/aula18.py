'''
MANIPULANDO STRINGS
* Strings indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir isso em:
    https://docs.python.org/3/library/stdtypes.html (tipos built-in)
    https://docs.python.org/3/library/functions.html (funções built-in)
'''
# positivos    [012345678]
# negativos   -[987654321]
# texto      = 'Python s2'
texto = 'Python s2'
url = 'www.google.com.br/'
print( texto[2])
print(url[:-4])
print(url[0:9:2])  # vai do caracter 0 até o 9, pulando de 2 em 2