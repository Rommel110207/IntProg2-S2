Algoritmo ejercicio1
Definir nombre, apellido, nombre_completo Como Caracter	
definir edad, edad_dias Como Entero	
Definir peso, pesolb Como Real	
Escribir "escribe o ingresa los siguientes datos "
escribir "nombre"
Leer nombre
Escribir "apellido"
leer apellido
Escribir "edad"
leer edad
Escribir "peso"
Leer peso
nombre_completo = Concatenar(apellido, " ")
nombre_completo = Concatenar(nombre_completo, nombre)
edad_dias = edad * 365
pesolb = peso / 2.204
Escribir "nombre completo ", nombre_completo
Escribir "edad en dias ", edad_dias
escribir "Peso en Kg", pesolb
FinAlgoritmo
