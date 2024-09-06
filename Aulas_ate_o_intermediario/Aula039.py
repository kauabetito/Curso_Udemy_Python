import os 

compras = []

while True:


    print("\nSelecione uma opção abaixo: ")
    opção = str(input("[i] para inserir. [a] para apagar. [l] para listar: "))

    if opção == 'i':
        inserir_local = int(input('\nem qual local você quer inserir?  Aponte o local com numeros inteiros positivos: '))
        inserir = str(input('o que você quer inserir de novo item de compra? '))
        compras.insert(inserir_local, inserir)  

    elif opção == 'a':
        remover = int(input('\nescolha um dos itens para ser removido: '))
        compras.pop(remover)

    elif opção == 'l':
        os.system('clear')

        if len(compras) == 0:
            print('\n\033[0;31;40mNão tem nada para se listar na lista\033[m')

        for numerado, loja in enumerate(compras):
            print('\n', numerado,'-', loja, '\n')
        
    
    else:
        print('\n\033[0;31;40mSelecione uma das opções acima\033[m')
    

    


