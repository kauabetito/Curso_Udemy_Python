lista = ['maria', 'helena', 'luiz']
cont = -1
indeces = range(len(lista))

for indece in indeces:
    print(indece, lista[indece], type(lista[indece]))


for name in lista:
    cont += 1 
    print(cont, name, type(name))