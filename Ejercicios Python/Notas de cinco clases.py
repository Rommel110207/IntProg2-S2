# Solicitar las notas de la primera asignatura
print("Digite las notas de sus 3 cortes evaluativos de la primera asignatura:")
Acorte1 = float(input("Nota del corte 1: "))
Acorte2 = float(input("Nota del corte 2: "))
Acorte3 = float(input("Nota del corte 3: "))
promedio1 = (Acorte1 + Acorte2 + Acorte3) / 3

# Solicitar las notas de la segunda asignatura
print("Digite las notas de sus 3 cortes evaluativos de la segunda asignatura:")
Bcorte1 = float(input("Nota del corte 1: "))
Bcorte2 = float(input("Nota del corte 2: "))
Bcorte3 = float(input("Nota del corte 3: "))
promedio2 = (Bcorte1 + Bcorte2 + Bcorte3) / 3

# Solicitar las notas de la tercera asignatura
print("Digite las notas de sus 3 cortes evaluativos de la tercera asignatura:")
Ccorte1 = float(input("Nota del corte 1: "))
Ccorte2 = float(input("Nota del corte 2: "))
Ccorte3 = float(input("Nota del corte 3: "))
promedio3 = (Ccorte1 + Ccorte2 + Ccorte3) / 3

# Solicitar las notas de la cuarta asignatura
print("Digite las notas de sus 3 cortes evaluativos de la cuarta asignatura:")
Dcorte1 = float(input("Nota del corte 1: "))
Dcorte2 = float(input("Nota del corte 2: "))
Dcorte3 = float(input("Nota del corte 3: "))
promedio4 = (Dcorte1 + Dcorte2 + Dcorte3) / 3

# Solicitar las notas de la quinta asignatura
print("Digite las notas de sus 3 cortes evaluativos de la quinta asignatura:")
Ecorte1 = float(input("Nota del corte 1: "))
Ecorte2 = float(input("Nota del corte 2: "))
Ecorte3 = float(input("Nota del corte 3: "))
promedio5 = (Ecorte1 + Ecorte2 + Ecorte3) / 3

# Mostrar los promedios de cada asignatura
print("El promedio de sus asignaturas es:")
print(f"Primera asignatura: {promedio1:.2f}")
print(f"Segunda asignatura: {promedio2:.2f}")
print(f"Tercera asignatura: {promedio3:.2f}")
print(f"Cuarta asignatura: {promedio4:.2f}")
print(f"Quinta asignatura: {promedio5:.2f}")