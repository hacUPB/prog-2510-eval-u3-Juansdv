nota = 0
contador = 0
suma = 0
promedio = 0

while nota != -1:

    nota = float(input("Ingrese las calificaciones de los estudiantes. Escribe -1 para finalizar \n"))
    contador += 1
    print(f"Calificación {contador}: {nota}")
    suma = nota + suma
    if nota < 0.0 or nota > 5.0:
        print("Nota invalida. Intente de nuevo")
    if nota == -1:
        suma += 1
        promedio = (suma / (contador - 1 ))
        contador -= 1
    else:
        promedio = promedio

print(f"Se ingresaron {contador} calificaciones. Promedio final de: {promedio}")

