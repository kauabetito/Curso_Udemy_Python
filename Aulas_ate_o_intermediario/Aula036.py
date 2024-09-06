str = 'ABCDE'
lista = [123, True, 'Kauã gostoso', 1.2,['Olá mundo']]
lista[-3] = 'mario'
print(lista[2])
print(lista)
lista2 = ['Ceo of the sexlo', 23123041247, 'leu é cuzin meu', 2*3/32**100-100-5125230*7**82*1]
print(lista2[3])
del lista2[3]
print(lista2)
lista.append(3322)

lista.insert(23,5)
lista3 = lista + lista2
print(lista3)

# for in com listas

lista = ['maria','helena', 'luiz']

for nome in lista:
    print (nome, type(nome))