#Aula do curso Udemy 108 a 109

x = 1 

def escopo1():
    x = 10
    print(x)
    
    def escopo2():
        y = 3
        print(x,y)

        return
    escopo2()

escopo1()

def multiplicacao(*args):
    total = 0
    for numero in args:
        total += numero * total
    return total

def soma(*args): # Soma os números X e Y
    total = 0
    for numero in args:
        total += numero
    return total



soma1 = soma(100,100)
soma2 = soma(250, 900)
resultado2somas = soma(soma1,soma2)


numeros = (1,2,3,4,5,10,2,4,51,23)

print(resultado2somas)
print(sum(numeros))
print(multiplicacao(10,2))

