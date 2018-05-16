# uso de algunas librerías estandar
import math
print(dir(math))
print(math.sin.__doc__,"\n\n")

#algunas funciones del modulo math
print(math.ceil(5.6),"\n")
print(math.floor(5.6),"\n")
print(math.pi,"\n")
print(round(math.pi,4),"\n")
print(math.sqrt(2),"\n")
print("\n\n")

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data),"\n")


def entero_aletorio():
    import random
    return random.randint(1,100)

print(entero_aletorio(),"\n")

from datetime import date
now = date.today()
print(now)