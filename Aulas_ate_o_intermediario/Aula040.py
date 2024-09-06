nome1 = str(input('digite o seu nome: '))
nome2 = str(input('digite o seu nome: '))
nome3 = str(input('digite o seu nome: '))


def viado():
    print(f'{nome1} é gay')

def parâmetros(a, b, c):
    print(f'Olá {nome1}')
    print(f'Olá {nome2}')
    print(f'Olá {nome3}')

def soma(x,y, z= None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z) 
    else:
        print(f'{x=} {y=}', x + y)

def saudação(nome5):
    print(f'Olá {nome5}')

def multiplicacao(x,y):
    print(x * y)
 
parâmetros(3, 4, 5)
saudação('guilherme')
multiplicacao(8, 10)
soma(5, 5, 5)
soma(5, 5, )
