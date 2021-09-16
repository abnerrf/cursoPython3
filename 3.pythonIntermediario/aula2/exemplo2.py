def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('Blaaaaaaaaaaaaaa')