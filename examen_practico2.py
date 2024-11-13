print("hola este es el restaurante carpirindo")
nombre = input("cuál es tu nombre? ")
print ("le muestro la carta señor/señora", nombre)
print ("tenemos un apartado para comida, bebidas y postres")
saldo = int(input("de cuánto es tu presupuesto? "))
print("muy bien " + nombre + " que desea pedir? ")

if saldo > 50:
    print("Bienvenido al cajero")


    ejecutar = True 


    while ejecutar:
        print("***selecciona la opción que desee pedir***")
        print("presiona 1 para ver el apartado de comida")
        print("presiona 2 para ver el apartado de bebidas")
        print("presiona 3 para ver el apartado de postres")
        print("*******************************************")
        opcion = int(input("escribe la opción que deseas hacer "))

        if opcion == 1:
            print("tu presupuesto es de ", saldo, "mxn")
            print("la comida que tenemos son: tacos, quesadillas o carne")
            opcion_uno = input("eliga la comida que desee ")
            if opcion_uno == "tacos":
                print("perfecto, tiene un costo de 50 pesos")
            if saldo < 50:
                print("no puedes pagar los tacos")
            else: 
                print("en un momento se los llevamos")
                saldo_final = saldo - 50

            if opcion_uno == "quesadillas":
                print("perfecto, tiene un costo de 60 pesos")
            if saldo < 60:
                print("no puedes pagar los tacos")
            else: 
                print("en un momento se los llevamos")
                saldo_final = saldo - 60
            
            if opcion_uno == "carne":
                print("perfecto, tiene un costo de 80 pesos")
                if saldo < 80:
                    print("no puedes pagar los tacos")
                else: 
                    print("en un momento se los llevamos")
                    saldo_final = saldo - 80


            opcion_uno = input(" deseas pedir algo más? precione 1 si desea pedir otra cosa, si no desea pedir algo más presione 2 " )
            if opcion_uno == 1:
                print("tendrás que regresar al menú ")
                ejecutar = True 
            elif opcion_uno == 2:
                print("gracias por venir al restaurante, hasta luego. Tu dinero sería de ", saldo_final)
                ejecutar = False
            else:
                print("opción no válida")


        if opcion == 2:
            print("tu presupuesto es de ", saldo, "mxn")
            print("las bebidas que tenemos son: jamaica, horchata y limón")
            opcion_uno = input("eliga la comida que desee ")
            if opcion_uno == "jamaica":
                print("perfecto, tiene un costo de 50 pesos")
                if saldo < 50:
                    print("no puedes pagar la bebida")
                else: 
                    print("en un momento se los llevamos")
                    saldo_final = saldo - 50

            if opcion_uno == "horchata":
                print("perfecto, tiene un costo de 50 pesos")
                if saldo < 50:
                    print("no puedes pagar la bebida")
                else: 
                    print("en un momento se los llevamos")
                saldo_final = saldo - 50
            
            if opcion_uno == "limón":
                print("perfecto, tiene un costo de 50 pesos")
                if saldo < 50:
                    print("no puedes pagar la bebida")
                else: 
                    print("en un momento se los llevamos")
                    saldo_final = saldo - 50

                
            opcion_uno = input(" deseas pedir algo más? precione 1 si desea pedir otra cosa, si no desea pedir algo más presione 2 " )
            if opcion_uno == 1:
                print("tendrás que regresar al menú ")
                ejecutar = True 
            elif opcion_uno == 2:
                print("gracias por venir al restaurante, hasta luego. Tu dinero sería de ", saldo_final)
                ejecutar = False
            else:
                print("opción no válida")
        

        if opcion == 3:
            print("tu presupuesto es de ", saldo, "mxn")
            print("los postres que tenemos son: helado, flan y pastel")
            opcion_uno = input("eliga la comida que desee ")
            if opcion_uno == "helado":
                print("perfecto, tiene un costo de 60 pesos")
                if saldo < 60:
                    print("no puedes pagar el postre")
                else: 
                    print("en un momento se los llevamos")
                    saldo_final = saldo - 60

            if opcion_uno == "flan":
                print("perfecto, tiene un costo de 70 pesos")
                if saldo < 70:
                    print("no puedes pagar el postre")
                else: 
                    print("en un momento se los llevamos")
                    saldo_final = saldo - 70
            
            if opcion_uno == "pastel":
                print("perfecto, tiene un costo de 80 pesos")
                if saldo < 80:
                    print("no puedes pagar el postre")
                else: 
                    print("en un momento se los llevamos")
                    saldo_final = saldo - 80

                
            opcion_uno = input(" deseas pedir algo más? precione 1 si desea pedir otra cosa, si no desea pedir algo más presione 2 " )
            if opcion_uno == 1:
                print("tendrás que regresar al menú ")
                ejecutar = True 
            elif opcion_uno == 2:
                print("gracias por venir al restaurante, hasta luego. Tu dinero sería de ", saldo_final)
                ejecutar = False
            else:
                print("opción no válida")
        
else:
    print("con ese presupuesto no puede ingresar, debido a que los precios son más elevados")