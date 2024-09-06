nome1, nome2, nome3, nome4 = ['Denise', 'Japacama', 'Betito', 'TESÂO']
nomes = ['Denise', 'Japacama', 'Betito', 'TESÂO']
nome1, nome2, nome3, nome4, = nomes
nome1, *_ = ['Denise', 'Japacama', 'Betito', 'TESÂO']

print(nome4)    
print(nome1, _) 

# tipo de lista tupla é uma lista imutavel, uma tupla é igual uma lista mas ela oferece mais desenpenho mais velocidade no codigo ela se cria sem os [] so as aspas '' ou podemos usar () no lugar dos cochetes 

Loucuras = '1', 'sexu', 'mortalew'

print(Loucuras)

numerate = enumerate(Loucuras)

print(numerate)

#otimizão do enumerate

for Numerada, Doideiras in enumerate(Loucuras):
    print(Numerada, Doideiras)