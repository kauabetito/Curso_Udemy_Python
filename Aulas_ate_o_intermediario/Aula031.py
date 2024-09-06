N1 = input("Digite um numero: ")

try:
    N1 = int(N1)
    if N1 % 2 == 0:
        print(f"o número que você digitou {N1} é par")
    elif N1 % 2 != 0:
        print(f"o número que você digitou {N1} é impar")

except ValueError:
    print("para o algoritimo funcionar digite um numero inteiro")
