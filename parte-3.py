# reto 3 ----------------------

def mostrarMenu(): 
    print("------------------")
    print(main)
    cont = 0
    while cont < len(menu):
        print(f"{cont + 1}. {menu[cont]}")
        cont +=1

def validarLatitude(latitud):
    if latitud < 5.888 or latitud > 6.306:
        print("error coordenada")
        exit(0)

def validarLongitude(longitud):
    if longitud < -72.552 or longitud > -72.321:
        print("error coordenada")
        exit(0)
    
def actCoordenada(i):
    print(f"Se actualiza el n° : {i}")
    latitud = float(input("Latitud: "))
    validarLatitude(latitud)

    longitud = float(input("Longitud: "))
    validarLongitude(longitud)
    coordenadas[i][0] = latitud
    coordenadas[i][1] = longitud

# RETO 1

print("--------------------------------------------------------------------")
print("    Bienvenido al Sistema de Ubicación Para Zonas públicas WiFi     ")
print("--------------------------------------------------------------------")

# inicialización de variables
usuarioIngre = 51631
contraseña = 13615
datosPer = [usuarioIngre, contraseña]   
cap1 = 1*6+1+1-5
cap2 = 6*1+1+1-5*1 
cap3 = 1+1+1
finDig = 631
suma = 634

# Condicionales hasta confirmar el inicio de sesión

usuarioIngre = float(input("Digite su número de usuario: "))

if usuarioIngre == datosPer[0]:
    contraseñaIngre = float(input("Correcto. Ingrese su contraseña: "))
    if contraseñaIngre == datosPer[1]:
        captcha = float(input(f"Correcto. Ingrese la suma de {finDig} + {cap1 or cap2 or cap3}: "))
        if captcha == suma:
            #inicio de sesión exitoso
            print("ingreso exitoso")
            print("Sesión iniciada")
        else:
            print("Error")
            exit(0)
    else:
        print("Error")
        exit(0)
else:
    print("Error")
    exit(0)

    
# RETO 2

import os

main = "El menú de opciones es:"
prim = "Cambiar contraseña"
segu = "Ingresar coordenadas actuales"
terc = "Ubicar zona WiFi mas cercana"
cuar = "Guardar archivo con ubicacion cercana"
quin = "Actualizar registros de zonas WiFi desde archivo"
sext = "Elegir opcion de menu favorita"
sept = "Cerrar sesión"

menu = [prim, segu, terc, cuar, quin, sext, sept]
msg = "Elija una opción: "
coordenadas = []

while True:
    mostrarMenu()
    opcion = int(input(msg))
    # TODO 1: Validar las opciones que sean correctas Y DAR LOS TRES INTENTOS
    if opcion == 1:
        contraseñaActual = int(input("Ingrese la contraseña actual: "))
        if contraseñaActual == datosPer[1]:
            print("La contraseña ingresada concuerda con la contraseña previa.")
            nuevaContraseña = int(input("Ingrese una nueva contraseña: "))
            if nuevaContraseña != datosPer[1]:
                datosPer.remove(contraseña)
                datosPer.insert(1,nuevaContraseña)
                print("Cambio de contraseña exitoso")
            else:
                print("Error")
                exit(0)
        else:
            print("Error")
            exit(0)

    elif opcion == 2:
        if len(coordenadas) == 0:
            for i in range(3):
                latitud = float(input(f"ingrese latitud {i+1}: "))
                validarLatitude(latitud)
                longitud = float(input(f"ingrese longitud {i+1}: "))
                validarLongitude(longitud)
                coordenadas.append([latitud,longitud]) 
        else:
            for i in range(len(coordenadas)):
                print(f"coordenada [latitud, longitud]: {i+1} : {coordenadas[i]}")

            col1 = [item[0] for item in coordenadas]
            print(f"Coordenada ubicada más al norte {max(col1)}")
            col2 = [item[1] for item in coordenadas]
            print(f"Coordenada ubicada más al oriente {max(col2)}")

            optInt = int(input("Presione 1,2 o 3 para actualizar la respectiva coordenada.\n\
            Presione 0 para regresar al menú: "))
            if optInt in [0, 1, 2, 3]:
                if optInt == 0:
                    break
                actCoordenada(optInt-1)
            else:
                print("error actualización")
                exit(0)
    
    elif opcion == 3:

        print(f"Usted ha elegido la opción {opcion}")
        exit(0)

    elif opcion == 4:
        print(f"Usted ha elegido la opción {opcion}")
        exit(0)

    elif opcion == 5:
        print(f"Usted ha elegido la opción {opcion}")
        exit(0)

    elif opcion == 6:
        favor = int(input("seleccione opción favorita: "))
        if favor !=0 and favor <= 5:
            print("Para confirmar por favor responda: ")
            print("Si me giras pierdo 1 unidad por eso debes colocame siempre de pie.")
            resp1 = int(input("La respuesta es: "))
            if resp1 == 3:
                print("Para confirmar por favor responda: ")
                print("Me separaron de un hermano siamés, antes era 8 y ahora soy un: ")
                resp2 = int(input("La respuesta es: "))
                if resp2 == 1:
                    #if favor == 1:
                    clearConsole = lambda: os.system('cls' if os.name == 'nt' else 'clear')
                    clearConsole()
                    #print(main)
                    menu [0], menu[favor-1] = menu[favor-1], menu[0]
                else:
                    print("Error")
                    mostrarMenu()
                    msg = "Elija una opción: "
                    opcion = int(input(msg))
            else:
                print("Error")
                mostrarMenu()
                msg = "Elija una opción: "
                opcion = int(input(msg))
        else:
            print("Error")
            exit(0)

    elif opcion == 7:
        print("Hasta pronto")
        exit(0)

    else:
        print("Error")
        c = 0
        while opcion != 0:
            if c <=2:
                c = c + 1
                mostrarMenu()
                msg = "Elija una opción: "
                opcion = int(input(msg))
            else:
                print("Error")
                exit(0)
        