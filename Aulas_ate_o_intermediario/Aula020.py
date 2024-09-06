N1 = int(input("Digite o primeiro valor: "))
N2 = int(input("Digite o segundo valor: "))

if N1 > N2:
    print(f"o valor {N1} é maior que o {N2}")
elif N2 > N1:
    print(f"o valor {N2} é maior que o {N1}")
else:
    print("Os dois são iguais")

# Professor fez assim:

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
