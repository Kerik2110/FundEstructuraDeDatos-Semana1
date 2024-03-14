from metodos import Metodos

menu = 1
while menu == 1:
    print("Bienvenido a Bienes Raices")
    print("¡¡Casas de $30.000!!")
    print("1- Calcular costos")
    print("2- Salir del programa")

    bandera = 1
    while bandera == 1:
        try:
            op = int(input("Ingrese una opcion: "))
            if op >= 0 and op <= 4:
                bandera = 0
            else:
                print("Ingrese una opción válida")
        except ValueError:
            print("Ingrese una opción válida")

    if op == 1:
        Metodos.calcular_beneficio()
    elif op == 2:
        print("Gracias por utilizar el programa.")
        break
    else:
        print("Error. Opcion invalida")