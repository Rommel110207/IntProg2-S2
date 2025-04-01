Algoritmo edadYpeso
	Definir nombre, apellido, nombre_completo Como Cadena
	Definir edad, edad_dias Como Entero
	Definir peso, pesolb Como Real
	Escribir 'escribe o ingresa los siguientes datos '
	Escribir 'nombre'
	Leer nombre
	Escribir 'apellido'
	Leer apellido
	Escribir 'edad'
	Leer edad
	Escribir 'peso'
	Leer peso
	nombre_completo <- Concatenar(apellido,' ')
	nombre_completo <- Concatenar(nombre_completo,nombre)
	edad_dias <- edad*365
	pesolb <- peso/2.204
	Escribir 'nombre completo ', nombre_completo
	Escribir 'edad en dias ', edad_dias
	Escribir 'Peso en Kg', pesolb
FinAlgoritmo
