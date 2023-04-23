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

# EJERCICIO 8
# Escribe un programa que pida el limite inferior y superior de un intervalo. 
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. 
# Cuando termine el programa dará las siguientes informaciones:
# 	* La suma de los números que están dentro del intervalo (intervalo abierto).
# 	* Cuantos números están fuera del intervalo.
# 	* He informa si hemos introducido algún número igual a los límites del intervalo.

"""suma_dentro_intervalo = 0
cont_fuera_intervalo = 0
igual_limites = 0

# Me aseguro que el limite inferior es inferior al limite superior
while True:
    num_lim_sup = int(input("Introduce un limite superior:"))
    num_lim_inf = int(input("Introduce un limite inferior:"))
    if num_lim_inf > num_lim_sup:
        print("Error: el limite inferior tiene que ser inferior al limite superior")
    if num_lim_inf <= num_lim_sup:
        break;

num = int(input("Introduce un numero (0, para salir):"))
while num != 0:
    # Pertenece al intervalo
    if num > num_lim_inf and num < num_lim_sup:
        suma_dentro_intervalo = suma_dentro_intervalo + num
    else:
        # No pertenece al intervalo
        cont_fuera_intervalo = cont_fuera_intervalo + 1
    # Numero igual a alguno de los limites
    if num == num_lim_inf or num == num_lim_sup:
        igual_limites = True

    num = int(input("Introduce un numero (0, para salir):"))

print("La suma de los numeros dentro del intervalo: ", suma_dentro_intervalo)
print("La cantidad de numeros fuera del intervalo: ", cont_fuera_intervalo)
if igual_limites:
    print("Se ha introducido algun numero igual a los limites del intervalo")
else:
    print("No se ha introducido ningun numero igual a los limites del intervalo")"""

# EJERCICIO 9
# Escribe un programa que dados dos números, uno real (base) y un entero positivo 
# (exponente), saque por pantalla el resultado de la potencia. No se puede 
# utilizar el operador de potencia.
"""base = int(input("Introduce el numero base:"))
while True:
    exponente = int(input("Introduce el numero exponente de la potencia:"))
    if exponente < 0:
        print("Error: El exponente debe ser positivo")
    else:
        break;
potencia = 1
for i in range(1, exponente +1):
    potencia = potencia * base
print("Potencia: ", potencia)"""

# EJERCICIO 10
# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
"""for table in range(1,6):
    for num in range(1,11):
        print("%d * %d = %d" % (table, num, table * num))"""

# EJERCICIO 11
# Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
# divisible por algún otro número.
"""es_primo = True
numero_es_primo = int(input("Introduce un numero para comprobar si es primo:"))
for num in range(2, numero_es_primo):
    if numero_es_primo % num == 0:
        es_primo = False
if es_primo:
    print("Es numero primo")
else:
    print("No es numero primo")"""

# EJERCICIO 12
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
# si al final de cada mes deposita cantidades variables de dinero;
# además, se quiere saber cuánto lleva ahorrado cada mes.
"""ahorro_acum = 0
for mes in range(1, 13):
    cant_mensual = float(input("Cuanto has ahorrado en el mes %d?:" % mes))
    ahorro_acum = ahorro_acum + cant_mensual
    print("En el mes ", mes,"llevas ahorrado ", ahorro_acum)"""

# EJERCICIO 13
# Una empresa tiene el registro de las horas que trabaja diariamente un empleado 
# durante la semana (seis días) y requiere determinar el total de éstas, así como 
# el sueldo que recibirá por las horas trabajadas.
"""horas_acum = 0
sueldo_por_hora = float(input("Introduce el sueldo por hora:"))
for dia in range(1, 7):
    horas = int(input("Introduce el numero de horas que has trabajado el dia %d ?:" % dia))
    horas_acum = horas_acum + horas
print("Horas trabajadas a la semana:", horas_acum)
print("Sueldo a percibir:", horas_acum * sueldo_por_hora)"""

# EJERCICIO 14
# Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra 
# en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad. 
# Realizar un programa para determinar en qué kilómetro de esa carretera se 
# encontrarán.
"""km1 = 70
km2 = 150
while km1 != km2:
    km1 = km1 +1
    km2 = km2 -1
print("Se encontraran el el km:", km1)"""

# EJERCICIO 15
# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
# euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total 
# de lo que pagó después de los 20 meses.
"""pago_acum = 0
pago = 10
for mes in range(1, 21):
    pago_acum = pago_acum + pago
    pago = pago * 2
print("Al final de los 20 meses tuvo que pagar: ", pago_acum)"""

# EJERCICIO 16
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores 
# y, además, calcule cuánto pagó la empresa por los N empleados.
"""horas_acumuladas = 0
sueldo_hora = float(input("Introduce el salario por hora:"))
num_trabajadores = int(input("Introduce el numero de trabajadores:"))
for trabajador in range(1, num_trabajadores +1):
    horas_semana = int(input("¿Cuantas horas han trabajador %d ?:" % trabajador))
    horas_acumuladas = horas_acumuladas + horas_semana
    print("El trabajador %d tiene el sueldo %f" %(trabajador, horas_semana*sueldo_hora))
print("El pago de los %d trabajadores es de %f" %(num_trabajadores, horas_acumuladas*sueldo_hora))"""

# EJERCICIO 17
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana
# Para esto, se registran los días que trabajó y las horas de cada día. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores 
# y además calcule cuánto pagó la empresa por los N empleados.
"""trabajadores = int(input("¿Cuantos trabajadores trabajan en la empresa?:"))
sueldo_hora = int(input("¿Cual es el sueldo por hora?:"))
horas_acumuladas = 0
for trabajador in range(1, trabajadores +1):
    horas_trabajador = 0
    dias = int(input("¿Cuantos dias ha trabajado el trabajador %d?:" %trabajador))
    for dia in range(1, dias + 1):
        horas = int(input("¿Cuantas horas ha trabajado el trabajador %d el dia %f?:" %(trabajador, dia)))
        horas_trabajador = horas_trabajador + horas
    print("El trabajador %d tiene el sueldo %d" %(trabajador, horas_trabajador*sueldo_hora))
    horas_acumuladas = horas_acumuladas + horas_trabajador
print("La empresa pago en total a los %d trabajadores un total de %d:" % (trabajadores, horas_acumuladas*sueldo_hora))"""

# CADENA DE CARACTERES
"""cadena = "informatica"
print(cadena.upper())
print(cadena.capitalize())
print(cadena[2])
print(cadena.count("a"))
print(cadena.find("for"))
print(cadena.startswith("i"))
print(cadena.endswith("a"))"""

"""cadenita = "hola mundo"
print(cadenita.swapcase())

cad = "22:30:55"
cad_list = (cad.split(":"))
print(cad)
print(cad_list)"""

# EJERCICIO 1
# Escribir por pantalla cada carácter de una cadena introducida por teclado.
"""cad = input("Introduce una cadena:")
for caracter in cad:
    print(caracter)"""

# EJERCICIO 2
# Realizar un programa que comprueba si una cadena leida por teclado
# comienza por una subcadena introducida por teclado.
"""cad = input("Introduce una cadena:")
sub_cad = input("Introduce una subcadena:")
if cad.startswith(sub_cad):
    print("La cadena comienza por la subcadena")
else:
    print("La cadena no comienza por la subcadena")"""

# EJERCICIO 3
# Pide una cadena y un caracter por teclado, (valida que sea un caracter)
# y muestra cuantas veces aparece el caracter en la cadena.
"""cad = input("Introduce una cadena:")
car = input("Introduce un caracter:")
while len(car) != 1:
    car = input("ERROR, Introduce un caracter:")
print("El caracter", car, "aparece", cad.count(car), "veces en la cadena", cad)"""

# EJERCICIO 4
# Suponiendo que hemos introducido una cadena por teclado que representa 
# una frase (palabras separadas por espacios), realiza un programa que 
# cuente cuantas palabras tiene.
"""cont = 0
posicion = 0
fra = input("Introduce una frase:")
fra = fra.strip()
posicion = fra.find(" ", posicion)
while posicion != -1:
    cont = cont +1
    while fra[posicion +1] == " ":
        posicion = posicion +1
    posicion = fra.find(" ", posicion +1)
print("La frase", fra, "tiene", cont +1, "palabras")"""
# Otra solucion posible
"""fra = input("Introduce una frase:")
print(len(fra.split()))"""

# EJERCICIO 5
# Si tenemos una cadena con un nombre y apellidos, realizar un programa que 
# muestre las iniciales en mayúsculas.
"""iniciales = ""
posicion = 0
nombre = input("Introduce tu nombre:")
# Elimino los espacios por delante y por detrás
nombre = nombre.strip()
# La primera inicial es la primera letra de la primera palabra
iniciales = iniciales + nombre[0]
# Voy buscando espacios
posicion = nombre.find(" ", posicion)
while posicion != -1:
    # No tengo en cuenta los posibles espacios que haya entre palabras
    while nombre[posicion + 1] == " ":
        posicion = posicion +1
    iniciales = iniciales + nombre[posicion + 1]
    posicion = nombre.find(" ", posicion + 1)
print("Tus iniciales son: ", iniciales.upper())"""

# EJERCICIO 6
# Realizar un programa que dada una cadena de caracteres por caracteres, genere 
# otra cadena resultado de invertir la primera.
"""cad = input("Inserta una cadena:")
cad_invert = cad[::-1]
print("La cadena invertida es: ", cad_invert)"""

# EJERCICIO 7
# Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.
"""cad = input("Introduce una cadena: ")
while True:
    car = input("Introduce un caracter a buscar: ")
    if len(car) == 1:
        break
while True:
    car_sustituto = input("Introduce un caracter a sustituir: ")
    if len(car_sustituto) == 1:
        break
cad_new = cad.replace(car,car_sustituto)
print("La nueva cadena es: ", cad_new)"""

# EJERCICIO 8
# Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a 
# minúsculas y viceversa.
"""cad = input("Introduce una cadena: ")
print("La cadena modificada es: ",cad.swapcase())"""

# EJERCICIO 9
# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.
"""cadena = input("Introduce una cadena:")
sub_cadena = input("Introduce una subcadena:")
print(cadena.find(sub_cadena))
if cadena.find(sub_cadena) > -1:
    print("Cadena incluye subcadena")
else:
    print("Cadena no incluye subcadena")
# Otra manera de comprobarlo
if sub_cadena in cadena:
     print("Cadena incluye subcadena")
else:
    print("Cadena no incluye subcadena")"""

#EJERCICIOS LISTAS
# EJERCICIO 1
## Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
## y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado 
## y su cubo.

"""import random
lista_numeros = []
for indice in range(1,11):
    lista_numeros.append(random.randint(1,10))
for numero in lista_numeros:
    print(numero," ",numero **2," ",numero **3)"""

# EJERCICIO 2
# Crea una lista e inicalizala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra 
# sus elementos  por la pantalla.
"""lista1 = []
lista2 = []
# Recorro la lista1 y leo cada elemento por teclado.
for indice in range(1,6):
    lista1.append(input("Dame la cadena %d:" % indice))
# Copio la lista1 en la lista2 en orden inverso.
lista2=lista1[::-1]

# Recorro la lista2 para mostrarlo.
for cadena in lista2:
    print(cadena)"""

# EJERCICIO 3
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un 
# alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, 
# la nota media, la nota más alta que ha sacado y la menor.

"""notas = []
for indice in range(1,6):
	while True:
		nota = int(input("Introduce la nota %d:" % indice))
		if nota < 0 or nota >10:
			print("Nota invalida")
		if nota>=0 and nota<=10: break
	notas.append(nota)

# Muestro resultados

print("Notas: ",end="")
for nota in notas:
	print(nota," ",end="")
print()
print("Nota media: ",sum(notas)/len(notas))
print("Nota max: ",max(notas))
print("Nota min: ",min(notas))"""

# EJERCICIO 4
# Programa que declare una lista y la vaya llenando de números hasta que 
# introduzcamos un número negativo. Entonces se debe imprimir el vector 
# (sólo los elementos introducidos).
"""lista = []
numero = int(input("Introduce un numero (nº negativo para salir):"))
while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduce un numero (nº negativo para salir):"))
for numero in lista:
    print(numero," ",end="")"""

# EJERCICIO 5
# Hacer un programa que inicialice una lista de números con valores aleatorios 
# (10 valores), y posterior ordene los elementos de menor a mayor.
"""import random
lista = []
for indice in range(1,11):
    lista.append(random.randint(1,10))
# Ordeno la lista
lista.sort()
# Recorro el vector ordenado
for numero in lista:
    print(numero," ",end="")"""

# EJERCICIO 6
# Crea un programa que pida un número al usuario un número de mes 
# (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) 
# y el nombre del mes. Debes usar listas. Para simplificarlo vamos 
# a suponer que febrero tiene 28 días.
"""dias = [31,28,31,30,31,30,31,31,30,31,30,31]
nombre_mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
while True:
	mes = int(input("Introduce un mes (1-12):"))
	if mes < 1 or mes > 12:
		print("Error: mes incorrecto.")
	if mes>=1 and mes<=12: break
print("El mes de",nombre_mes[mes-1],"tiene",dias[mes-1],"días.")"""

# EJERCICIO 7
# Programa que declare tres listas 'lista1', 'lista2' y 'lista3' de cinco 
# enteros cada uno, pida valores para 'lista1' y 'lista2' y 
# calcule lista3=lista1+lista2.
"""lista1 = []
lista2 = []
lista3 = []
for indice in range(1,6):
	lista1.append(int(input("Introduce el elemento %d de la lista1:" % indice)))
for indice in range(1,6):
	lista2.append(int(input("Introduce el elemento %d de la lista2:" % indice)))
for indice in range(0,5):
	lista3.append(lista1[indice] + lista2[indice])
print("La lista3 es:")
for numero in lista3:
	print(numero," ",end="")"""

# EJERCICIO 8
# Queremos guardar los nombres y la edades de los alumnos de un curso. 
# Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre 
# un asterisco (*) Al finalizar se mostrar� los siguientes datos:
#  * Todos lo alumnos mayores de edad.
#  * Los alumnos mayores (los que tienen más edad)
"""nombres = []
edades = []
while True:
    nombre = input("Introduce el nombre del alumno:")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime la edad del alumno:")))
    if nombre == "*": break

# Calcular la edad máxima
edad_max = max(edades)

# Alumnos mayores de edad
print("Alumnos mayores de edad:")
print("=======================")
for nombre,edad in zip(nombres,edades):
    if edad >= 18:
        print(nombre)

# Alumnos mayores
print("Alumnos mayores")
print("===============")
for nombre,edad in zip(nombres,edades):
    if edad == edad_max:
        print(nombre)"""

# EJERCICIO 9
# Queremos guardar la temperatura mínima y máxima de 5 días. 
# Realiza un programa que de la siguiente información:
# * La temperatura media de cada día
# * Los días con menos temperatura
# * Se lee una temperatura por teclado y se muestran los días cuya temperatura
#   máxima coincide con ella. 
# Si no existe ningún día se muestra un mensaje de información.

# Recorrido para rellenar la tabla(5 dias con temp. max y min)
# En este caso se crea una lista de listas
"""temperaturas = []
for indice in range(1,6):
    temperatura = []
    temperatura.append(int(input("Dia %d. Temperatura máxima:" % indice)))
    temperatura.append(int(input("Dia %d. Temperatura minima:" % indice)))
    temperaturas.append(temperatura)

# Mostrar temperatura media
print("Temperaturas medias")
print("===================")
for temperatura in temperaturas:
    print("Dia %d. Temperatura media: %f:" % (indice, sum(temperatura)/len(temperatura)))
    indice += 1

# Calcular temperatura mínima más pequeña
# Supongo que es la primera
temp_min = temperaturas[0][1];
for temperatura in temperaturas:
    if temperatura[1] < temp_min:
        temp_min = temperatura[1]
print(temp_min)"""

# EJERCICIO 10
# Diseñar el algoritmo correspondiente a un  programa, que:
# 
# * Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# * Carga la tabla con valores numéricos enteros.
# * Suma todos los elementos de cada fila y todos los elementos de cada columna
#   visualizando los resultados en pantalla.
"""tabla = []
for indice_fila in range(1,6):
    fila = []
    for indice_colum in range(1,6):
        fila.append(int(input("Introduce el número de la fila %d y la columna %d:" % (indice_fila,indice_colum))))
    tabla.append(fila)
print(tabla)

# Suma de filas
indice_fila = 1
for fila in tabla:
    print("La suma de la fila %d es: %d" % (indice_fila,sum(fila)))
    indice_fila +=1

# Suma de columnas
for indice_colum in range(1,6):
    suma = 0
    for fila in tabla:
        suma = suma + fila[indice_colum - 1]
    print("La suma de los elemento de la columna %d es: %d" % (indice_colum,suma))"""

# EJERCICIO 11
# Diseñar el algoritmo correspondiente a un programa, que:
#  * Crea una tabla bidimensional de longitud 5x5 y nombre 'diagonal'.
#  * Carga la tabla de forma que los componentes pertenecientes a la diagonal de la 
#    matriz tomen el valor 1 y el resto el valor 0.
#  * Muestra el contenido de la tabla en pantalla.
matriz = []
for indice_fila in range(0,5):
    fila= []
    for indice_colum in range(0,5):
        # Si estoy en la diagonal inicializo 1
        if indice_fila == indice_colum or indice_fila == 4 - indice_colum:
            fila.append(1)
        # No estoy en la diagonal inicializo 0
        else:
            fila.append(0)
    matriz.append(fila)
# Recorro la lista para mostrarla
for fila in matriz:
    for elemento in fila:
        print(elemento," ",end="")
    print()





