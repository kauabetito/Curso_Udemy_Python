import sys

import Aula060_m
from Aula060_m import hi
from Aula060_m import vezes

sys.path.append('/home')
print('Este módulo se chama', __name__)
#print(*sys.path, sep='\n')
print(hi)
print(vezes(8,5))