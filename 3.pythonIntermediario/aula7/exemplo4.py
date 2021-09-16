import copy

d1 = {1: 'a', 2: 'b', 3: 'c'}
# v = d1
# v = d1.copy()  # PARA COPIAR A VARIAVEL DE FORMA QUE O QUE FOR ALTERADO EM UMA, NÃO ALTERE A OUTRA
v = copy.deepcopy(d1)  # FORMA IDEAL DE COPIAR, USANDO O MODULO COPY, UMA SERA INDEPENDENTE DA OUTRA

print(d1)
print(v)