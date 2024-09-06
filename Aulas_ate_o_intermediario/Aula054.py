# Generator expression, iterables e iterators em Python
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem__iter__e__next__

for i in iterator:
    print(i)

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

for i in generator:
    print(i)
# print(next(iterator))