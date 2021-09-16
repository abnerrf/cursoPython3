"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def saudacao(msg, nome):
    print(f'{msg} {nome}')

saudacao('Olá', 'Aderbaldo')
saudacao('Oieee', 'Todoroki')
saudacao('Oi', 'Maria')
"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(2, 7, 1)
soma(4, 7, 154)
soma(2, 57, 33)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def percent(n1, n2):
    return print(n1 + (n1 * n2 / 100))

ap = percent(50, 10)
print(ap)
ap = percent(15, 74)
print(ap)
ap = percent(100, 25)
print(ap)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def funcao(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    if x % 3 == 0:
        return 'Fizz'
    if x % 5 == 0:
        return 'Buzz'
    return x

print(funcao(7))
print(funcao(15))
print(funcao(4275))

