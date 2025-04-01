# Solicitar la cantidad de productos
cantidad = float(input("Ingrese la cantidad de productos: "))

# Solicitar el precio unitario
precio_unitario = float(input("Ingrese el precio unitario del producto: "))

# Calcular el total
total = cantidad * precio_unitario

# Calcular el descuento (10% del total)
descuento = total * 0.10

# Calcular el total final a pagar
monto_final = total - descuento

# Mostrar el resultado
print(f"El total final a pagar es: {monto_final:.2f}")