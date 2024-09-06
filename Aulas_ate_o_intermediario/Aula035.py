from random import choice
import os

frase = ['desenvolvimento', 'programação', 'software', 'hardware', 'python', 'javaScript', 'agachamento Livre']
cont = 0
acerto = ''


while True:
    if cont == 0:
        frase = choice(frase)
    cont += 1
   
    letra_adigi = str(input("\nDigite uma letra para adivinhar a frase secreta: "))

    if len(letra_adigi) > 1:
        print("\nDigite apenas uma letra.")
        continue

    if letra_adigi in frase:
        acerto += letra_adigi

    palavra_for = ''

    for letra_secre in frase:
        if letra_secre in acerto:
            palavra_for += letra_secre
        else:
            palavra_for += '*'

    print('\n', palavra_for)

    if palavra_for == frase:
        os.system('clear')
        print(f"Parabens você completou a frase {frase}. Você tentou acertar ela {cont} vezes") 
        cont -= cont
        acerto = ''