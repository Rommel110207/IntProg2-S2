# Solicitar al usuario el monto en dolares
dolares= float(input("introduce el monto en dolares: "))
# Solicitar el tipo de cambio (1 dolar= C$36.6243)
tipo_cambio= float(input("Introduce el tipo de cambio(36.6243): "))
moneda= dolares * tipo_cambio
# Mostrar el resultado
print(f"{dolares} dolares son equivalentes a {moneda: .2f} en cordobas")