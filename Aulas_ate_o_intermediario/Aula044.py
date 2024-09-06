# len - quantas chaves
# keys - iterável coma as chaves
# values - interável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o última item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'name': 'Kauã',
    'sobrenome': 'Betito',   
}

pessoa.setdefault('idade', None)

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))


for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave,valor)

import copy

d1 = {
    'name': 'Kauã',
    'c1': 1,
    'c2': 2,
    'list': [0,1,2],
}

name = d1.pop('name')

ultima_chave = d1.popitem() # Apaga o última item adicionado

d1.update({ # update - Atualiza um dicionário com outro e adiciona mais coisas nele
    'va' : 'novo valor',
    'idade': 18,
})
d1.update(data='23/01/2006', copo='STANLEY')

d2 = copy.deepcopy(d1)
'''d1['list'][0] = 23'''


d2['c1'] = 1000
print(name)
print(d1)

