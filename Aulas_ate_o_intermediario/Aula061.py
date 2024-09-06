import importlib

import Aula061_m

print(Aula061_m.olá)

for i in range(10):
    importlib.reload(Aula061_m)
    print(i)

print('Fim')