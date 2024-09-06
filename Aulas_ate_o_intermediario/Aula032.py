N1 = input("Na sua região que horas é? ")

try:
    N1 = int(N1)
    if N1 >= 0 and N1 <= 11:
        print("está peela manhã ai na sua região, então tenha um bom dia")

    elif N1 >= 12 and N1 <= 17:
        print("Aproveite esse céu azul, tenha uma Boa tarde!")

    elif N1 >= 18 and N1 <= 23:
        print("Está chegando a hora de ir dormir, tenha uma Boa Noite!")

except ValueError:
    print("digite um horario certo")
