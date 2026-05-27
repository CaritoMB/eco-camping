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
        continue ## vuelve al while, no a la linea siguiente 
## despliegue de opciones
    if opcion == 1:
        disponibles = capacidad_maxima - sitios_ocupados
        print (f"\n[INFO] Sitios libres por recibir vehiculos: {disponibles}")
    elif opcion == 2:
        sitios_libres = capacidad_maxima - sitios_ocupados
        if sitios_libres == 0:
            print ("lo sentimos, no quedan sitios disponibles")
        else:
            try:
                ingreso = int(input("¿cuantos sitios o vehiculos van a ingresar?: "))
                if ingreso <= 0:
                    print ("error: la cantidad de ingreso debe ser mayor a cero")
                elif ingreso > sitios_libres:
                    print (f"error: solo puede ingresar un maximo de {sitios_libres} sitios")
                else:
                    sitios_ocupados += ingreso
                    print (f"Ingreso registrado, se han ocupado {ingreso} sitios")
            except ValueError:
                print ("error al ingresar cantidad de sitios")
    elif opcion == 3:
        print (f"\n-- registrar salida (vehiculos o sitios ocupados): {sitios_ocupados}")
        if sitios_ocupados == 0:
            print ("no hay sitios ocupados, no puede ingresar una salida")
        else:
            try:
                salida = int (input("¿cuantos vehiculos se retiran?: "))
                if salida < 0:
                    print ("error: la cantidad de salida debe ser mayor a cero")
                elif salida > sitios_ocupados:
                    print (f"error: no se puede retirar mas de {sitios_ocupados} vehiculos (segun los sitios ocupados)")
                else
                    sitios_ocupados -= salida
                    print (f"--> Salida Registrada, se han liberado {salida} sitios")
            except ValueError:
                print ("Error al ingresar la salida")
    elif opcion == 4:
        porcentaje_ocupacion = (sitios_ocupados / capacidad_maxima) * 100
        print (f"\n[ESTADO] ocupacion actual: {sitios_ocupados} / {capacidad_maxima} sitios")
        print (f"[ESTADO] el camping esta al {porcentaje_ocupacion:.1f}% de su capacidad")
    elif opcion == 5:
        print ("cerrando el sistema .....")
        ejecutando = False
    else:
        print ("Opcion fuera de rango")