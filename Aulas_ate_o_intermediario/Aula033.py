Name = input("Digite o seu nome: ")

try:
    Name = str(Name)
    if Name <= Name[:4]:
        print("seu nome é curto")
    elif Name <= Name[:6]:
        print("o tamanho do seu nome normal")
    else:
        print("o tamanho do seu nome é considerado grande")
except ValueError:
    print("Digite um nome")
