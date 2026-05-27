## Ecocamping
## control inventario: maxima 15 sitios - registro ocupados y disponibles
## registro ingreso: registrar entrada vehiculo. no se puede ingresar si se supera la capacidad  o numero invalida mnor igual a cero
## registro salida: registrar salida vehiculos, no se pueden retirar mas de los que ingresaron
## 
print("Gestion Ecocamping 'Bosque Vivo'")
capacidad_maxima = 15 
sitios_ocupados = 0 
ejecutando = True
while ejecutando:
    print ("\n=== MENU CONTROL REGISTRO")
    print ("1.- ver sitios disponibles")
    print ("2.- ingreso vehiculos")
    print ("3.- salida vehiculos")
    print ("4.- estado camping")
    print ("5.- salir")
    print (".")
    try:
        opcion = int(input("selecione una opcion (1-5): "))
    except ValueError:
        print ("Opcion no valida")
        continue
## despliegue de opciones
if opcion == 1:
    disponibles = capacidad_maxima - sitios_ocupados
    print (f"\n[INFO] Sitios libres por recibir vehiculos: {disponibles}")
else:
    print ("Opcion fuera de rango")