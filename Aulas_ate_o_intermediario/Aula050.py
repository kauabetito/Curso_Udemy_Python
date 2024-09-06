produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor
    if isinstance(valor, (int,float)) else valor.upper()
    for chave, valor
    in produto.items()
    if chave != "nome"
}

lista = [
    ('v', 'valor a'),
    ('t', 'valor t'),
    ('y', 'valor s'),
]
dc = {
    chave: valor 
    for chave, valor in lista
}

s1 = {2 ** i for i in range(+1,11) }

print(s1)
print(dict(lista))
