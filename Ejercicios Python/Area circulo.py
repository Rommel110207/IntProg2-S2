# Calcular el area de un circulo usando el valor de pi
import math
radio= float(input("Introduce el radio del circulo"))
area= math.pi * (radio **2)
# Mostrar el resultado
print(f"El area de un circulo con radio {radio} es: {area: .2f}")