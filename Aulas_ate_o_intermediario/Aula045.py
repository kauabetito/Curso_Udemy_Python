# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
d1 = set('Ronaldo')
s2 = {'Kauã', 2,3}  # vazio
# print(d1,s2, type(d1))  # com dados

s1 = set()
s1.add('2')
s1.add('3')
s1.add('342') # adiciona itens ao set
s1.update(('vi',312,22)) # adiciona itens ao set
# s1.clear() # Limpa o set
s1.discard('vi') #elimina algum valor passado
# print(s1)
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
s1 = {1,2,3}

s2 = {2,3,4}
s3 = s1 | s2 # união | união (union) - Une
s4 = s1 & s2 # intersecção & (intersection) - Itens presentes em ambos
s5 = s1 - s2 # diferença - Itens presentes apenas no set da esquerda
s6 = s1 ^ s2 # diferença simétrica ^ - Itens que não estão em ambos

print(s3)
print(s4)
print(s5)
print(s6)

