# raise - lançando exceções (erros)
def erro_dividi_por_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def divide(n, d):
    erro_dividi_por_zero(d)
    return n / d

print(divide(2, 0))
raise ValueError ('Explodiu o cod')