#for es el ciclo (haz esto varias veces pero siguiendo una secuencia)
# in es el conector
#range() es el generador de numeros, crea la secuencia que for va a recorrer 
for i in range (10):
    print ("hola")
#0 es de donde inicia a contar, 31 hasta donde y 10 de cuanto en cuanto debe contar
for x in range (0,31,10):
    print (x)#for es el ciclo (haz esto varias veces pero siguiendo una secuencia)
# in es el conector
#range() es el generador de numeros, crea la secuencia que for va a recorrer 
for i in range (10):
	    print ("hola")
	    
#0 es de donde inicia a contar, 31 hasta donde y 10 de cuanto en cuanto debe contar
for x in range (0,31,10):
	    print (x)
	    
#intentemos combinar for con booleanos
#creamos variable para la identificacion y hacemos una lista
IDidentificaciones = [1024, 1234, 4321, 7600]
#bucle while true para repetir el programa
while True:
#el usuario pone su ID
	usuario = int(input("ingresa tu numero de identificacion; "))
#definimos acceso como false
	acceso = False
#iteranos sobre identificaciones y guardamos en ID	
	for ID in IDidentificaciones:
#si usuario es igual a ID entonces acceso es igual a true		
		if usuario == ID:
			acceso = True
#si acceso es true se imprime la bienvenida y break cierra, si es false se denega (else)			
	if acceso:
		print("bienvenido")
		break
	else:
		print("acceso denegado intente de nuevo")

		
######NUEVO BLOQUE#######		
while True:
	edades = input("ingresa tu edad separadaso por comas: ").split(",")
	for edad in edades:
		edad = int(edad)
		if edad % 2 == 0:
			print (edad, "tu edad es numero par")
		else:
			print (edad, "tu edad es numero impar")
	print ("desea añadir mas edades?")
	respuesta = input ("si/no; ")
	if respuesta == "no":
		break