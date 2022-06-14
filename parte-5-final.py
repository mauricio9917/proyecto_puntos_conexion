import os
from math import sin, cos, sqrt, acos, radians, asin, degrees
import json
import urllib.parse
import requests

# Declaraciones de valores

id_usuario = 51631 #datos iniciales
contraseña = 13615
datos_persona = [id_usuario, contraseña]   
captcha_1 = 1*6+1+1-5   # datos de captcha
captcha_2 = 6*1+1+1-5*1 
captcha_3 = 1+1+1
digito_inicial = 631
suma = 634

ubicacionWifi = [
                [6.211,-72.482, 2],      #Ubicaciones preestablecidas
                [6.212,-72.470, 25],
                [6.105,-72.342, 25],
                [6.210,-72.442, 50]
                ]

coordenadas = []

#APIs

main_api = 'https://www.mapquestapi.com/directions/v2/route?'
key = 'VOckc5kM7y9iINOVsL7iWKnAoUBznCeC'

# Funciones 

    # Inicio de sesión

def mostrar_inicio():
    print("--------------------------------------------------------------------")
    print("    Bienvenido al Sistema de Ubicación Para Zonas públicas WiFi     ")
    print("--------------------------------------------------------------------")

def iniciar_sesion():
    ingreso_id_usuario = float(input("Digite su número de usuario: "))
    if ingreso_id_usuario == datos_persona[0]:
        ingreso_contraseña = float(input("Correcto. Ingrese su contraseña: "))
        if ingreso_contraseña == datos_persona[1]:
            captcha = float(input(f"Correcto. Ingrese la suma de {digito_inicial} + {captcha_1 or captcha_2 or captcha_3}: "))
            if captcha == suma:
                #inicio de sesión exitoso
                mostrar_ingreso_exitoso()
            else:
                mostrar_error()
        else:
            mostrar_error()
    else:
        mostrar_error()

def mostrar_error():
    print("Error")
    exit(0)

def mostrar_ingreso_exitoso():
    print("ingreso exitoso")
    print("Sesión iniciada")

def mostrar_menu():
    print('--------MENÚ DE OPCIONES----------')
    print('Elija una de las siguientes opciones:')
    menu = "1. Cambiar contraseña \
        \n2. Ingresar coordenadas actuales \
        \n3. Ubicar zona WiFi mas cercana \
        \n4. Usar mapas para llegar hacia una ubicación \
        \n5. Guardar archivo con ubicacion cercana \
        \n6. Actualizar registros de zonas WiFi desde archivo \
        \n8. Cerrar sesión"
    print(menu)

    # Opción 1

def cambiar_contraseña(contraseña_actual, nueva_contraseña):
    contraseña_actual = int(input("Ingrese la contraseña actual: "))
    if contraseña_actual == datos_persona[1]:
        comprobar_contraseña(nueva_contraseña)
    else:
        mostrar_error()

def comprobar_contraseña(nueva_contraseña):
    print("La contraseña ingresada concuerda con la contraseña previa.")
    nueva_contraseña = int(input("Ingrese una nueva contraseña: "))
    if nueva_contraseña != datos_persona[1]:
        cambio_exitoso_contraseña(nueva_contraseña)
    else:
        mostrar_error()
    return nueva_contraseña

def cambio_exitoso_contraseña(nueva_contraseña):
    datos_persona.remove(contraseña)
    datos_persona.insert(1,nueva_contraseña)
    print("Cambio de contraseña exitoso")
    return datos_persona

    # Opción 2

def ingresar_coordenadas_actuales():
    if len(coordenadas) == 0:
        for i in range(3):
            ingresar_latitud_longitud(i)
    else:
        for i in range(len(coordenadas)):
            print(f"coordenada [latitud, longitud]: {i+1} : {coordenadas[i]}")

        anadir_arreglo_coordenadas()
        confirmar_actualizacion_coordenada()

def actualizar_coordenada(i):
    print(f"Se actualiza el n° : {i}")
    latitud = float(input("Latitud: "))
    validar_latitud(latitud)

    longitud = float(input("Longitud: "))
    validar_longitud(longitud)

    coordenadas[i][0] = latitud
    coordenadas[i][1] = longitud   

def validar_latitud(latitud):
    if latitud < 5.888 or latitud > 6.306:
        print("error coordenada")
        exit(0)

def validar_longitud(longitud):
    if longitud < -72.552 or longitud > -72.321:
        print("error coordenada")
        exit(0)

def ingresar_latitud_longitud(i):
    latitud = float(input(f"ingrese latitud {i+1}: "))
    validar_latitud(latitud)
    longitud = float(input(f"ingrese longitud {i+1}: "))
    validar_longitud(longitud)
    coordenadas.append([latitud,longitud]) 

def anadir_arreglo_coordenadas():
    col1 = [item[0] for item in coordenadas]
    print(f"Coordenada ubicada más al norte {max(col1)}")
    col2 = [item[1] for item in coordenadas]
    print(f"Coordenada ubicada más al oriente {max(col2)}")

def confirmar_actualizacion_coordenada():
    optInt = int(input("Presione 1,2 o 3 para actualizar la respectiva coordenada.\n\
        Presione 0 para regresar al menú: "))
    if optInt in [0, 1, 2, 3]:
        if optInt == 0:
            mostrar_menu()
        actualizar_coordenada(optInt-1)
    else:
        print("error actualización")
        exit(0)

    # Opción 3

def ubicar_wifi_cercano():
    if len(coordenadas) == 0:
        mostrar_error()
    else:
        for i in range(len(coordenadas)):
            print(f"coordenada [latitud, longitud]: {i+1} : {coordenadas[i]}")

        optInt = int(input("Por favor elija su ubicación actual (1,2 o 3)\n \
        para calcular la distancia a los puntos de conexión: "))

        if optInt in [1, 2, 3]:
            print(f"Se calcula la distancia en el n° : {optInt}")
            p1 = coordenadas[optInt -1]
            distancias = []
            for item in ubicacionWifi:
                p2 = item
                dist = calcularDistancia(p1, p2)
                distancias.append(dist)                    
                distancias.sort()
            #print(distancias)
            
            print("Zonas WiFi cercanas con menos usuarios conectados:")
            print(f"La zona wiFi 1: ubicada en [{ubicacionWifi[2][0]}, {ubicacionWifi[2][1]}] \
a {int(distancias[0])} metros, tiene en promedio {ubicacionWifi[2][2]} usuarios")
            print(f"La zona wiFi 2: ubicada en [{ubicacionWifi[3][0]}, {ubicacionWifi[3][1]}] \
a {int(distancias[1])} metros, tiene en promedio {ubicacionWifi[3][2]} usuarios")
            opcFinish=int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
            velocidadBusProm=16.67*60 #m/min
            velocidadPieProm=0.483*60 #m/min
            if opcFinish != 1 and opcFinish != 2:
                mostrar_error()
            elif opcFinish==1:
                tiempoBusProm=(distancias[0]/velocidadBusProm)
                tiempoPieProm=(distancias[0]/velocidadPieProm)
                print("Para dirigirse a la zona WiFi, dirigirse primero al oriente, \
y luego hacia el norte. Los tiempos promedio:")
                print(f"En bus, sería de {int(tiempoBusProm)} minutos")
                print(f"A pie, sería de {int(tiempoPieProm)} minutos, {(int(tiempoPieProm)/60)} horas")
            elif opcFinish==2:
                tiempoBusProm=(distancias[1]/velocidadBusProm)
                tiempoPieProm=(distancias[1]/velocidadPieProm)
                print("Para dirigirse a la zona WiFi, dirigirse primero al occidente, \
y luego hacia el norte. Los tiempos promedio:")
                print(f"En bus, sería de {int(tiempoBusProm)} minutos")
                print(f"A pie, sería de {int(tiempoPieProm)} minutos, {(int(tiempoPieProm)/60)} horas")
        else:
            mostrar_error()

def calcularDistancia(p1,p2):
    p1radianes = [radians(p1[0]), radians(p1[1])] 
    p2radianes = [radians(p2[0]), radians(p2[1])]

    deltaLati = p2radianes[0]-p1radianes[0]
    deltaLong = p2radianes[1]-p1radianes[1]
    R = 6372.795477598

    raiz = (sin(deltaLati/2)**2+cos(p1radianes[0])*cos(p2radianes[0])*sin(deltaLong/2)**2)

    dist = 2*R*asin(sqrt(raiz)) *1000
    return dist

    # Opción 4

def usar_mapas():
    while True:
        print('NOTA: Presione q o escribe quit para salir de esta opción.')
        orig = input('Ingrese el origen: ')
        if orig == 'quit' or orig == 'q':
            break
        dest = input('Ingrese el destino: ')
        if dest == 'quit' or dest == 'q':
            break
        url = main_api + urllib.parse.urlencode({'key':key, 'from':orig, 'to':dest})
        print('URL: '+(url))
        json_data = requests.get(url).json()
        json_status = json_data['info']['statuscode']
        if json_status == 0:
            print(f'API Status: {str(json_status)} = A successful route call')
            print('----------------------------------------------------------')
            print(f'Información de viaje desde {orig} a {dest}')
            print(f'Duración del viaje: {json_data["route"]["formattedTime"]}')
            print(f'Kilometros: {str("{:.2f}".format(json_data["route"]["distance"]*1.61))}')
            print(f'Combustible usado [gal]: {str("{:.2f}".format(json_data["route"]["fuelUsed"]))}')
            print('-----------------------------------------------------------')
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print('-----------------------------------------------------------')
        elif json_status == 402:
            print("**********************************************")
            print("Estado de código: " + str(json_status) + "; Entradas de usuario no válidas para una o ambas localizacione")
            print("**********************************************\n")
        elif json_status == 611:
            print("**********************************************")
            print("Estado de código: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
            print("**********************************************\n")
        else:
            print("************************************************************************")
            print("For Staus Code: " + str(json_status) + "; Refer to:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("************************************************************************\n")

    # Opción 4

def guardar_archivo():
    if (len(coordenadas)==0):
        mostrar_error()
    else:
        ruta_nombre="salida.txt"
        archivo = open(ruta_nombre,'w')
        diccInfo={
            'actual': [coordenadas],
            'Zona WiFi 1': [ubicacionWifi[2][0], ubicacionWifi[2][1], ubicacionWifi[2][2]],
            'recorrido': [16628,'Bus',16]
            }
        print(f"actual: {diccInfo['actual']}")
        print(f"Zona WiFi 1: {diccInfo['Zona WiFi 1']}")
        print(f"recorrido: {diccInfo['recorrido']}")

        print("¿Está de acuerdo con la información a exportar?")
        opcExp=int(input("Presione 1 para confirmar, 0 para volver al menú principal: "))
        if opcExp==1:
            archivo.write(str(f"actual: {diccInfo['actual']}\n"))
            archivo.write(str(f"Zona WiFi 1: {diccInfo['Zona WiFi 1']}\n"))
            archivo.write(str(f"recorrido: {diccInfo['recorrido']}\n"))
            archivo.close()
            print("Exportando archivo...")
        elif opcExp==0:
            pass
        else:
            mostrar_error()

    # Opción 5

def actualizar_registros():
    archivo = open('zona_wifi.txt','r')
    print(archivo.read())
    archivo.close()
    print("Datos de coordenadas para zonas WiFi actualizados.")
    opcAct=int(input("Presione 0 para volver al menú principal: "))
    if opcAct==0:
        pass
    else:
        mostrar_error()

    # Opción 7

def cerrar_sesion():
    print("Hasta pronto")
    exit(0)

    # Otra opción

def otra_opcion():
    mostrar_error()
    

# Parte 1

mostrar_inicio()
iniciar_sesion()

# Parte 2

while True:

    mostrar_menu()
    opcion = int(input('Opción: '))

    if opcion == 1:
        cambiar_contraseña(contraseña, datos_persona)

    elif opcion == 2:
        ingresar_coordenadas_actuales()

    elif opcion == 3:
        ubicar_wifi_cercano()
    
    elif opcion == 4:
        usar_mapas()

    elif opcion == 5:
        guardar_archivo()

    elif opcion == 6:
        actualizar_registros()

    elif opcion == 7:
        cerrar_sesion()

    else:
        otra_opcion()
        

