# Try, except, else , finally

a = 18
b = 0

try:
    c = a / b
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Variavel sem nenhuma atribuuição')
except (TypeError, IndexError) as error:
    print("Erro: ",error)
    print("MGS:", error)
    print("Nome:" ,error.__class__.__name__)
    print('TypeError + IndexError')
except Exception:
    print('Erro desconhecido.')
print('fora do Try')

# Pode se usar quantos except você quiser
try:
    print('Abrir arquivo')
    # open
    
except ZeroDivisionError:
    print('Divão por zero')
    ...

else:
    print('quando se tem o except e finally o else serve para dizer que o codigo funcionou sem erros!')

finally:
    print('Fechar arquivo') # finally sempre sera executado
    ...