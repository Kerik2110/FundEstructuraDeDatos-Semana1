from metodos import Metodos

separador = "--------------------"
menu = 1
while menu == 1:
    print("Bienvenido a su programa")
    print("1- Mostrar precios")
    print("2- Comprar entradas")
    print("3- Dinero perdido al aplicar descuento")
    print("4- Salir del programa")
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
        Metodos.mostrar_precios()
        pregunta = input("Desea comprar una entrada?: ")
        if pregunta == "si":
            Metodos.comprar_entradas()
        else:
            print("Gracias. Vuelva pronto")
        break
    elif op == 2:
        Metodos.comprar_entradas()
        print(separador)
    elif op == 3:
        Metodos.dinero_perdido()
        print(separador)
    elif op == 4:
        print("Gracias por utilizar el programa")
        menu = 0