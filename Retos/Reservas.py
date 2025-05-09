def genero():
    while True:    
        try:
            genero = int(input("Ingrese su genero:\n1. Para hombre\n2. Para mujer\n"))
            match genero:
                case 1:
                    genero = "Bienvenido a JS Airlines. Señor"
                    break
                case 2:
                    genero = "Bienvenida a JS Airlines. Señora"
                    break
                case _:
                    print("\nOpción no disponible. Intentelo nuevamente.\n")
        except ValueError:
            print("\nNo se permiten caracteres. Intentelo nuevamente.\n")


    usuario= str(input("Ingrese su nombre y su apellido:\n"))
    print(f"{genero} {usuario}")

genero()

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
dia = str(input("Porfavor eliga el día de la semana en la que desea viajar, es decir, lunes, martes... \n")).capitalize()
numlista = dias.index(dia)



ciudad_o = str(input("Actualmente operamos en estos aeropuertos. Porfavor, seleccione su ciudad de origen: \n1. Medellín\n2. Bogotá\n3. Montería\n4. Cartagena\n5. Barranquilla\n ")).lower()
destino = str(input("Porfavor seleccione su ciudad de destino:\n1. Medellín\n2. Bogotá\n3. Montería\n4. Cartagena\n5. Barranquilla\n")).lower()


distancia= 0

numdia = int(input("Porfavor, introduzca el dia del mes: \n"))

if numdia < 1 or numdia > 31:
    print("Rango de día invalido")



if ciudad_o == "medellin" and destino == "bogota" or ciudad_o == "bogota" and destino == "medellin":
    distancia = 240
elif ciudad_o == "medellin" and destino == "monteria" or ciudad_o == "monteria" and destino == "medellin":
    distancia = 298
elif ciudad_o == "medellin" and destino == "cartagena" or ciudad_o == "cartagena" and destino == "medellin":
    distancia = 461
elif ciudad_o == "medellin" and destino == "barranquilla" or ciudad_o == "barranquilla" and destino == "medellin":
    distancia = 710
elif ciudad_o == "bogota" and destino == "monteria" or ciudad_o == "monteria" and destino == "bogota":
    distancia = 492
elif ciudad_o == "bogota" and destino == "cartagena" or ciudad_o == "cartagena" and destino == "bogota":
    distancia = 657
elif ciudad_o == "bogota" and destino == "barranquilla" or ciudad_o == "barranquilla" and destino == "bogota":
    distancia = 688
elif ciudad_o == "monteria" and destino == "cartagena" or ciudad_o == "cartagena" and destino == "monteria":
    distancia = 187
elif ciudad_o == "monteria" and destino == "barranquilla" or ciudad_o == "barranquilla" and destino == "monteria":
    distancia= 275
elif ciudad_o == "cartagena" and destino == "barranquilla" or ciudad_o == "barranquilla" and destino == "cartagena":
    distancia = 94
else:
    print("Ruta no encontrada")




if distancia < 400:
    if 0 <= numlista <= 3:
        precio = "$79.900"
    elif 4 <= numlista <= 6:
        precio = "$119.900"
    else:
        print("Día invalido")
elif distancia > 400:
    if 0 <= numlista <= 3:
        precio = "$156.900"
    elif 4 <= numlista <= 6:
        precio = "$213.000"
    else:
        print("Día invalido")
else:   
    print("Ha ocurrido un error.")



print(f"Tu vuelo de {ciudad_o.capitalize()} a {destino.capitalize()} del día {dia.capitalize()} {numdia} de abril esta reservado. Precio a pagar: {precio}")

