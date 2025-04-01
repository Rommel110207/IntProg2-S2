Algoritmo porcentaje
Definir cantidad, precioUnitario, total, descuento, montoFinal Como Real
Escribir "Ingrese la cantidad de productos:"
Leer cantidad
Escribir "Ingrese el precio unitario del producto:"
Leer precioUnitario
total <- cantidad * precioUnitario
descuento <- total * 0.10
montoFinal <- total - descuento
Escribir "El monto final a pagar es: ", montoFinal
FinAlgoritmo
