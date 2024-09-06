# Yield from
def gen1():
    print("começou o gen1")
    yield 1 
    yield 2
    yield 3
    print("terminou o gen1")


def gen2():
    yield from gen1()
    print("começou o gen2")
    yield 4
    yield 5
    yield 6
    print("terminou o gen2")


def gen3(gen):
    yield from gen()
    print("começou o gen3")
    yield 7
    yield 8
    yield 9
    print("terminou o gen3")

g = gen3(gen2)
for numero in g:
    print(numero)