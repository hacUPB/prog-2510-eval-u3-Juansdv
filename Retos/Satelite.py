altitud_inicial = int(input("Ingrese la altitud del satelite (En kilometros):\n"))

arrastre = float(input("Ingrese el coeficiente de arrastre inicial: \n"))

altitud_reingreso = int(input("Ingrese la altitud minima de seguridad (En kilometros):\n"))

altitud_actual= altitud_inicial
orbita = 0


print("Simulando la desintegración orbital:")
while altitud_actual >= altitud_reingreso:
    altitud_perdida = arrastre * altitud_actual
    altitud_actual -= altitud_perdida
    arrastre += 0.0001
    orbita += 1
    print(f"Orbita {orbita}: Altitud actual= {altitud_actual}, coeficiente de arrastre: {arrastre.__round__(4)}")
    if altitud_perdida <= 0.01 :
        print("El satelite se ha estabilizado")
    
print(f"El Satelite ha reingresado en la atmósfera terrestre después de {orbita-1} orbitas")


