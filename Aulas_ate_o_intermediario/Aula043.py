'''introdução á dicionarios em python '''

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

pessoa['nome2'] = 'Kauã Lima'

print(pessoa, type(pessoa))
print(pessoa['nome2'])
del pessoa['sobrenome']

#print(pessoa.get('sobrenome', 'Não existe'))

if pessoa.get('sobrenome') is None:
    print('Não Existe')
else:
    print(pessoa['sobrenome'])