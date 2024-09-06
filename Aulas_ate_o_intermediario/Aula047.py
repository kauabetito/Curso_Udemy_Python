pessoa = {
    'nome': 'Ruan',
    'sobrenome': 'Rocha',
}

a1 , a2 = pessoa.values()

print(a1, a2)

dados_pessoa = {
    'idade': 18,
    'altura': 1.8,
}

def mostrar_argumentos_nomeados(*args, **kwargs):
    print(kwargs)

mostrar_argumentos_nomeados(nome='ben 10', idade='' )