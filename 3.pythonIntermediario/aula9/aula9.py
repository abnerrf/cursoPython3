'''
SETS EM PYTHON (CONJUNTOS)
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
'''

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.discard(2)
s1.update([4,5,6],{6,7,8})

print(s1)

l1 = [1,2,1,2,2,3,3,4,4,4,4,6,6,6,5,7,8,9,'Abner','Abner']
l1 = set(l1)
l1 = list(l1)

print(l1)

s2 = {1,2,3,4,5,7,9}
s3 = {1,2,3,4,5,6}
s4 = s2 | s3
s5 = s2 & s3
s6 = s3 - s2
s7 = s2 ^ s3
print(s4)
print(s5)
print(s6)
print(s7)