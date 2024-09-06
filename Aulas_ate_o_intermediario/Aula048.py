from pprint import pprint

def p(valor):
    pprint(valor, sort_dicts=False, width=40)

print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)
print(lista)

lista = [
    numero * 2 
    for numero in range (10)
]

print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    produto
    for produto in produtos
]

p(novos_produtos)

print(*novos_produtos, sep='\n')

