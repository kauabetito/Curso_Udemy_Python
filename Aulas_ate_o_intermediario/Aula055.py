# Introdução ás Generator functions em Python
# generator = (n for n in range(1000000))

'''def genarator(n=0, maximum=10):
    yield 1 # A cada Yield o codigo pausa 
    print('continuando...')
    yield 2 # Pausar
    print('outra vez')
    yield 3 # Pausar
    return 'Acabou' 
'''

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen = generator(maximum=23412)
for i in gen:
    print(i)