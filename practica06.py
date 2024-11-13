print("hola este es un cajero")
nombre = input("cuál es tu nombre? ")
nip = int(input(nombre + " inserte su NIP "))
tarjeta = (input ("De que banco es tu tarjeta? "))
saldo = int(input("cuál es tu saldo? "))
print("muy bien " + nombre + " que operación deseas hacer? tu saldo es de ", saldo, "mxn")

if tarjeta == "BBVA" or "Santander" or "Banamex":
    print("Bienvenido al cajero")


    ejecutar = True 


    while ejecutar:
        print("***selecciona la opción que deseas hacer***")
        print("presiona 1 para consultar saldo")
        print("presiona 2 para realizar un retiro")
        print("presiona 3 para hacer un abono")
        print("*******************************************")
        opcion = int(input("escribe la opción que deseas hacer "))

        if opcion == 1:
            print("tu saldo es de ", saldo, "mxn")
            opcion_uno = input(" deseas hacer otra operación?, precione 1 si desea realizar otra, si no desea realizar otra presione 2 ")
            if opcion_uno == 1:
                print("tendrás que regresar al menú principal")
                ejecutar = True 
            elif opcion_uno == 2:
                print("gracias por usar el cajero, hasta luego.")
                ejecutar = False
            else:
                print("opción no válida")


        if opcion == 2:
            opcion_dos = int(input("de cuanto deseas hacer tu retiro? "))
            if opcion_dos > saldo:
                print ("saldo insuficiente")
            if opcion_dos > 8000:
                print ("por día no puedes retirar más de 8000 mxn")
            else:
                print("hiciste un retiro de ", opcion_dos)
                print("tu saldo actual es de ", saldo - opcion_dos, "mxn")

            opcion_uno = input(" deseas hacer otra operación?, precione 1 si desea realizar otra, si no desea realizar otra presione 2 ")
            if opcion_uno == 1:
                print("tendrás que regresar al menú principal")
                ejecutar = True 
            elif opcion_uno == 2:
                print("gracias por usar el cajero, hasta luego.")
                ejecutar = False
            else:
                print("opción no válida")
        

            if opcion == 3:
                opcion_tres = int(input("de cuanto deseas hacer el abono? "))
            if opcion_tres > saldo:
                print ("saldo insuficiente")
        
            else:
                print("hiciste un abono de ", opcion_tres)
                print("tu saldo actual es de ", saldo - opcion_tres, "mxn")

            opcion_uno = input(" deseas hacer otra operación?, precione 1 si desea realizar otra, si no desea realizar otra presione 2 ")
            if opcion_uno == 1:
                print("tendrás que regresar al menú principal")
                ejecutar = True 
            elif opcion_uno == 2:
                print("gracias por usar el cajero, hasta luego.")
                ejecutar = False
            else:
                print("opción no válida")
else:
    print("no aceptamos ese banco, solo BBVA, Santander o Banamex")