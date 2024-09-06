# dir, hasattrt e getattr em Python

string = 'João Safado'
metodo = '1upper'

if hasattr (string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)