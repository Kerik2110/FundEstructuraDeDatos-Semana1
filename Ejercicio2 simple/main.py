from metodos import Metodos

print("Bienvenido a Bienes Raices")
print("¡¡Casas de $30.000!!")
print("1- Calcular costos")
print("2- Salir del programa")

op = int(input("Ingrese una opcion: "))

if op == 1:
    Metodos.calcular_beneficio()
elif op == 2:
    print("Gracias por utilizar el programa.")
else:
    print("Error. Opcion invalida")