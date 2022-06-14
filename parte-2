def mostrarMenu(): 
    print("------------------")
    print(main)
    cont = 0
    while cont < len(menu):
        print(f"{cont + 1}. {menu[cont]}")
        cont +=1
# RETO 1

print("--------------------------------------------------------------------")
print("    Bienvenido al Sistema de Ubicación Para Zonas públicas WiFi     ")
print("--------------------------------------------------------------------")

# inicialización de variables
nombreUsuario = 51631   
contraseña = 13615   
cap1 = 1*6+1+1-5
cap2 = 6*1+1+1-5*1 
cap3 = 1+1+1
finDig = 631
suma = 634

# Condicionales hasta confirmar el inicio de sesión
usuarioIngre = float(input("Digite su número de usuario: "))

if usuarioIngre == nombreUsuario:
    contraseñaIngre = float(input("Correcto. Ingrese su contraseña: "))
    if contraseñaIngre == contraseña:
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

while True:
    mostrarMenu()
    opcion = int(input(msg))
    # TODO 1: Validar las opciones que sean correctas Y DAR LOS TRES INTENTOS
    if opcion == 1:
        print(f"Usted ha elegido la opción {opcion}")
        exit(0)

    elif opcion == 2:
        print(f"Usted ha elegido la opción {opcion}")
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
        





