
def Conversor_Real_Para_Dolar(Real): # 1,00 Real Brasileiro é igual a 0.18 Dolar em 10 de agosto de 2024
    Dolar = 0.1815 # O Valor de 1 Real Brasileiro convertido em Dolar
    conversor = Real * Dolar
    return conversor

def Conversor_Dolar_Para_Real(Dolar): # 1,00 Real Brasileiro é igual a 0.18 Dolar em 10 de agosto de 2024
    Real = 5.509 # O Valor de um Dolar Americano Convertido em Real
    conversor = Dolar * Real
    return conversor

print(Conversor_Dolar_Para_Real(50))