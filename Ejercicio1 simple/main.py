from metodos import Metodos

print("Bienvenido a su programa")
print("1- Mostrar precios")
print("2- Comprar entradas")
print("3- Dinero perdido al aplicar descuento")
print("4- Salir del programa")
op = int(input("Ingrese la opción: "))

if op == 1:
    Metodos.mostrar_precios()
    pregunta = input("Desea comprar una entrada?: ")
    if pregunta == "si":
        Metodos.comprar_entradas()
    else:
        print("Gracias. Vuelva pronto")
elif op == 2:
    Metodos.comprar_entradas()
elif op == 3:
    Metodos.dinero_perdido()
elif op == 4:
    print("Gracias por utilizar el programa")
else:
    print("ERROR. Opción no valida!!")