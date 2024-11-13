print("hola bienvenido a Volaris DANTE")
nombre = input("cuál es tu nombre? ")
print("muy bien " + nombre + " que operación deseas hacer?")


ejecutar = True 


while ejecutar:
    print("***selecciona la opción que deseas hacer***")
    print("presiona 1 para comprar boletos")
    print("presiona 2 para documentar tu maleta")
    print("presiona 3 para realizar check in ")
    print("*******************************************")
    opcion = int(input("escribe la opción que deseas hacer "))


    if opcion ==1: 
        print("elije el destino")
        opcion_uno = input("Brazil, Argentina o Colombia")

        if opcion_uno == "Brazil":
            print("destino Brazil")
            if opcion_uno == "Brazil":
                opcion_uno = input("escoje la zona del avion quieres tus boletos, adelante, mitad, atras")
            
            opcion_uno = input("escriba confirmar para seguir")

            if opcion_uno == "confirmar":
                print("Adelante costo es de 9000, Mitad costo de 7000, Atras costo de 5000")
    
    elif opcion_uno == "Argentina": 
        print("destino Argentina")
        if opcion_uno =="Argentina":
            print("elegiste Argentina")
        if opcion_uno== "Argentina":
            opcion_uno = input("escoje la zona del avion quieres tus boletos, adelante, mitad, atras")
        
        opcion_uno = input("escriba confirmar para seguir")
    
        if opcion_uno == "confirmar":
            print("Adelante costo de 9000, Mitad costo de 7000, Atras costo de 5000")

    elif opcion_uno == "Colombia": 
        print("destino Colombia")
        if opcion_uno =="Colombia":
            print("elegiste Colombia")
        if opcion_uno== "Colombia":
            opcion_uno = input("escoje la zona del avion quieres tus boletos, adelante, mitad, atras")
        
        opcion_uno = input("escriba confirmar para seguir")
    
        if opcion_uno == "confirmar":
            print("Adelante costo de 9000, Mitad costo de 7000, Atras costo de 5000")

        opcion_uno = input(" deseas hacer otra operación?, precione 1 si desea realizar otra, si no desea realizar otra presione 2 ")
        if opcion_uno == 1:
                print("tendrás que regresar al menú principal")
                ejecutar = True 
        elif opcion_uno == 2:
                print("gracias por consultar en Volaris, hasta pronto.")
                ejecutar = False
        else:
                print("opción no válida")

    if opcion ==2: 
        print("Documentar su maleta")
        print("Conteste lo siguente")

    peso = int(input("escriba el peso de su maleta"))
    if peso < 50:
        print ("el peso de su maleta es de" ,peso, "kg, cumple con los requisitos")
        print ("el precio es de 1000 mxn")
    if peso > 50:
        print("el peso de su maleta no es permitido")
    else:
        opcion_uno = input(" deseas hacer otra operación?, precione 1 si desea realizar otra, si no desea realizar otra presione 2 ")
        if opcion_uno == 1:
                print("tendrás que regresar al menú principal")
                ejecutar = True 
        elif opcion_uno == 2:
                print("gracias por consultar en Volaris, hasta pronto.")
                ejecutar = False
        else:
                print("opción no válida")
    

    if opcion ==3: 
        print("realizar check in ")
    opcion_tres = input("escriba 1 para llenar el nombre completo, escriba 2 para llenar fecha de nacimeinto")

    if opcion_tres == 1:
        print("elegiste contestar nombre completo")
        opcion_tres = input("escribe tu nombre completo")
        print("gracias" ,opcion_tres,)
       
        opcion_uno = input(" deseas hacer otra operación?, precione 1 si desea realizar otra, si no desea realizar otra presione 2 ")
        if opcion_uno == 1:
                print("tendrás que regresar al menú principal")
                ejecutar = True 
        elif opcion_uno == 2:
                print("gracias por consultar en Volaris, hasta pronto.")
                ejecutar = False
        else:
                print("opción no válida")

    elif opcion_tres == 2: 
        print("elegiste contestar fecha de nacimiento")
        if opcion_tres == 2:
                opcion_tres = input("escribe tu fecha de nacimiento")
                print("gracias, tu fecha de nacimiento es el ", opcion_tres)

        opcion_uno = input(" deseas hacer otra operación?, precione 1 si desea realizar otra, si no desea realizar otra presione 2 ")
        if opcion_uno == 1:
                print("tendrás que regresar al menú principal")
                ejecutar = True 
        elif opcion_uno == 2:
                print("gracias por consultar en Volaris, hasta pronto.")
                ejecutar = False
        else:
                print("opción no válida")

       