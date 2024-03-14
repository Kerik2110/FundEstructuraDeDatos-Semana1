class Metodos():
       def mostrar_precios():
              print("Precio unico del boleto: $3.000")
              print("Descuentos por edad: ")
              print("Categoría 1: 5-14 35%")
              print("Categoría 2: 15-19 25%")
              print("Categoría 3: 20-45 10%")
              print("Categoría 4: 46-65 25%")
              print("Categoría 5: 66+ 35%")

       def comprar_entradas():
              nombre = input("Ingrese su nombre: ")
              edad = int(input("Ingrese su edad: "))
              boleto = 3000

              if edad < 5:
                     print("Los menores de 5 años no pueden ingresar al teatro.")
              elif edad >= 5 and edad <= 14:
                     descuento = boleto * (35/100)
                     precio_final = boleto - descuento
                     print(nombre, " tienes un descuento del 35%")
                     print("Valor final entrada: ", precio_final)
              elif edad >= 15 and edad <= 19:
                     descuento = boleto * (25/100)
                     precio_final = boleto - descuento
                     print(nombre, " tienes un descuento del 25%")
                     print("Valor final entrada: ", precio_final)
              elif edad >= 20 and edad <= 45:
                     descuento = boleto * (10/100)
                     precio_final = boleto - descuento
                     print(nombre, " tienes un descuento del 10%")
                     print("Valor final entrada: ", precio_final)
              elif edad >= 46 and edad <= 65:
                     descuento = boleto * (25/100)
                     precio_final = boleto - descuento
                     print(nombre, " tienes un descuento del 25%")
                     print("Valor final entrada: ", precio_final)
              elif edad > 66:
                     descuento = boleto * (35/100)
                     precio_final = boleto - descuento
                     print(nombre, " tienes un descuento del 35%")
                     print("Valor final entrada: ", precio_final)

       def dinero_perdido():
              boleto = 3000
              categoria1 = boleto * (35/100)
              categoria2 = boleto * (25/100)
              categoria3 = boleto * (10/100)
              categoria4 = boleto * (25/100)
              categoria5 = boleto * (35/100)
              
              print("Dinero perdido por cada boleto")
              print("Categoria 1: ", categoria1)
              print("Categoria 2: ", categoria2)
              print("Categoria 3: ", categoria3)
              print("Categoria 4: ", categoria4)
              print("Categoria 5: ", categoria5)
