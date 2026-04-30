#pequeña bienvenida
print("hola mundo de la programacion")
nombre = input("como te llamas?:  ")
print ("bienvenido", nombre)

#cambio de dispositivo
print ("hagamos una suma")
while True:
    try:
        a = float(input ("ingresa el primer numero: "))
        b = float(input ("ingresa el segundo numero: "))
        resultado = a + b 
        print ("resultado", resultado)
        break

    except:
        print ("¡¡¡ERROR!!! debe ingresar solo numeros")

#eval(): ejecuta texto como codigo 
#usar eval con precaucion mayormente usar solo para pruebas 

#hacer suma con multiplicacion 
print ("ingresa dos numeros para sumar y uno para multiplicar")
while True:
    try:
        numero1 = float(input("ingresa el primer numero: "))
        numero2 = float(input("ingresa el segundo numero: "))
        resultados = numero1+numero2 

        print("el resultado es: ", resultados)
        multi = float(input("ingresa numero para multiplicar: "))
        print ("el resultado es: ", resultados * multi)
        break

    except:
        print ("ingrese solo numeros")