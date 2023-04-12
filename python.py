# EJERCICIO 1
# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el
#producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de 
#un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)
# resultado = 1
# num = int(input("Dime un numero: "))
# contador = 2
# while contador <= num:
#     resultado = resultado * contador
#     contador = contador +1
# print("El resultado es", resultado)

# EJERCICIO 2
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1
# al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor 
# que el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
# El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), 
# si se llega al limite de intentos te muestra el número que había generado.
"""import random
intentos = 10
num_secreto  =  random.randint(1,100)
num_ingresado = int(input("Adivine el numero secreto (de 1 a 100):"))

while num_secreto != num_ingresado and intentos>1:
    if num_secreto > num_ingresado:
        print("Muy bajo")
    else: 
        print("Muy alto")
    intentos  =  intentos-1
    print("Le quedan ",intentos," intentos:")
    num_ingresado = int(input("Adivine el numero (de 1 a 100):"))

if num_secreto == num_ingresado:
    print("Exacto! Usted adivino en ",11-intentos," intentos.")
else:
    print("El numero era: ",num_secreto)"""

#EJERCICIO 3
# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media 
# de todos los números introducidos.
"""suma = 0
cont =0

# Con el mientras si el primer número es 0 no va a entrar en el bucle
num=int(input("Número (0 para salir):"))
while num != 0:
	suma = suma + num
	cont = cont + 1
	num=int(input("Número (0 para salir):"))

# Si cont=0 no puedo realizar la división
if cont > 0:
	media = suma / cont
else:
	media = 0"""

# EJERCICIO 3 V2
"""suma = 0
cont = 0
while True:
    num = int(input("Introduce un número(0 para salir):"))
    suma = suma + num
# Si num=0 no debemos tenerlo en cuenta para calcular la media.
    if num != 0:
        cont = cont + 1
    if num == 0:
        break
if cont != 0:
    media = suma / cont
else:
    media = 0
print("Suma:", suma)
print("Media:", media)"""


#EJERCICIO 4
# Realizar un algoritmo que pida números (se pedir� por teclado la cantidad de 
# números a introducir). El programa debe informar de cuantos números introducidos 
# son mayores que 0, menores que 0 e iguales a 0.
"""cont_negativos = 0
cont_positivos = 0
cont_ceros = 0
cantidad_num=int(input("¿Cuántos números vas a introducir?:"))
for i in range(1,cantidad_num + 1):
	print("Número ",i,":",end="");
	num=int(input())
	if num>0:
		cont_positivos = cont_positivos + 1
	else:
		if num<0:
			cont_negativos = cont_negativos + 1
		else:
			cont_ceros = cont_ceros + 1

print("Números positivos:",cont_positivos);
print("Números negativos:",cont_negativos);
print("Números igual a 0:",cont_ceros);"""

# EJERCICIO 5
# Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
# en caso contrario, el programa termina cuando se introduce un espacio.

"""while True:
	car = input("Introduce un carácter:")
	if len(car) == 1:
		break
while car != " ":
	if car.upper() == "A" or car.upper() == "E" or car.upper() == "I" or car.upper() == "O" or car.upper() == "U":
		print("VOCAL")
	else:
		print("NO VOCAL")
	while True:
		car = input("Introduce un carácter:")
		if len(car) == 1:
			break"""

# EJERCICIO 5 V2
"""while True:
    while True:
        car=input("Introduce un carácter:")
        if len(car) == 1:
            break
    if car !=" ":
        if car.upper() == "A" or car.upper() == "E" or car.upper() == "I" or car.upper() == "O" or car.upper() == "U":
            print("VOCAL")
        else:
            print("NO VOCAL")
    if car == " ":
        break"""

# EJERCICIO 6
# Escribir un programa que imprima todos los números pares entre dos números que 
# se le pidan al usuario.
"""num1 = int(input("Introduce el primer numero:"))
num2 = int(input("Introduce el segundo numero:"))
if num1 % 2 == 1:
    num1 = num1 + 1
for num in range(num1, num2 +1, 2):

    print(num," ", end = "")"""

# EJERCICIO 7
# Realizar una algoritmo que muestre la tabla de multiplicar de un número 
# introducido por teclado.
"""tabla = int(input("Que tabla deseas mostrar:"))
for num in range(1,11):
    print("%d * %d = %d" % (tabla, num, tabla * num))"""

#hola
