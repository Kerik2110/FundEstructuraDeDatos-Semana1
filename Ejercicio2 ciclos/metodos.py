class Metodos():
    def calcular_beneficio():
        ingresos = int(input("Monto mensual de ingresos: "))
        casa = 30000

        if ingresos >= 80000:
            pie = casa * (15/100)
            print("El pie de la casa será de: ", pie)
            mensualidad = (casa - pie)/(10*12)
            print("La mensualidad a pagar en 10 años será de: ", mensualidad)
            
        elif ingresos <= 80000:
            pie = casa * (30/100)
            print("El pie de la casa será de: ", pie)
            mensualidad = (casa - pie)/(7*12)
            print("La mensualidad a pagar en 7 años será de: ", mensualidad)
        