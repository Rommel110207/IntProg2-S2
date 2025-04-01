# Ingrese el monto en cordobas
cordobas= float(input("Introduce el monto en cordobas "))
# Solicitar el tipo de cambio actual(1 dolar= C$36.6243)
tipo_cambio= float(input("Introduce el tipo de cambio(36.6243)"))
#conversion
dolares= cordobas/tipo_cambio
#Mostrar el resultado
print(f"{cordobas} cordobas son equivalentes a {dolares: .2f} dolares. ")