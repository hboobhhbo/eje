nombre = input("cuál es tu nombre?")
print ("selcciona una opción")
print (" ")
print (nombre + " selecciona 1 para traducir números: ingles a español")
print (nombre + " selecciona 2 para traducir números: español a inglés")
print (nombre + " selecciona 3 para traducir números: alemán a español")
print (nombre + " selecciona 4 para traducir números: español a alemán")
print (nombre + " selecciona 5 para traducir números: ingles a alemán")
print(" ")
opcion = int(input("Escribre la opción que quieras escojer "))
if opcion < 1:
    print ("no tenemos esa opción")

if opcion > 5:
    print ("no tenemos esa opción")

if opcion == 1:
    print ("ingles a español")

    opcion_uno = input("escibe el color que deseas traducir ")

    if opcion_uno == "blue":
        print("el significado es AZUL")

    elif opcion_uno == "red":
        print("el significado es ROJO")
    
    elif opcion_uno == "green":
        print("el significado es VERDE")
    
    elif opcion_uno == "black":
        print("el significado es NEGRO")

    elif opcion_uno == "pink":
        print("el significado es ROSA")
    
    elif opcion_uno == "purple":
        print("el significado es MORADO")
    
    elif opcion_uno == "orange":
        print("el significado es NARANJA")

    elif opcion_uno == "yellow":
        print("el significado es AMARILLO")

    elif opcion_uno == "white":
        print("el significado es BLANCO")

    elif opcion_uno == "brown":
        print("el significado es CAFE")

    else:
        print("no sé el color")


if opcion == 2:
    print ("español a inglés")

    opcion_dos = input("escibe el color que deseas traducir ")

    if opcion_dos == "azul":
        print("el significado es BLUE")

    elif opcion_dos == "rojo":
        print("el significado es RED")
    
    elif opcion_dos == "verde":
        print("el significado es GREEN")
    
    elif opcion_dos == "negro":
        print("el significado es BLACK")

    elif opcion_dos == "rosa":
        print("el significado es PINK")
    
    elif opcion_dos == "morado":
        print("el significado es PURPLE")
    
    elif opcion_dos == "naranja":
        print("el significado es ORANGE")

    elif opcion_dos == "amarillo":
        print("el significado es YELLOW")

    elif opcion_dos == "blanco":
        print("el significado es WHITE")

    elif opcion_dos == "cafe":
        print("el significado es BROWN")
        
    else:
        print("no sé el color")

    
if opcion == 3:
    print ("alemán a español")

    opcion_tres = input("escibe el color que deseas traducir ")

    if opcion_tres == "blau":
        print("el significado es AZUL")

    elif opcion_tres == "rot":
        print("el significado es ROJO")
    
    elif opcion_tres == "grün":
        print("el significado es VERDE")
    
    elif opcion_tres == "schwarz":
        print("el significado es NEGRO")

    elif opcion_tres == "rosa":
        print("el significado es ROSA")
    
    elif opcion_tres == "lila":
        print("el significado es MORADO")
    
    elif opcion_tres == "orange":
        print("el significado es NARANJA")

    elif opcion_tres == "gelb":
        print("el significado es AMARILLO")

    elif opcion_tres == "weiss":
        print("el significado es BLANCO")

    elif opcion_tres == "braun":
        print("el significado es CAFE")
        
    else:
        print("no sé el color")

    
if opcion == 4:
    print ("español a alemán")

    opcion_cua = input("escibe el color que deseas traducir ")

    if opcion_cua == "azul":
        print("el significado es BLAU")

    elif opcion_cua == "rojo":
        print("el significado es ROT")
    
    elif opcion_cua == "verde":
        print("el significado es GRÜN")
    
    elif opcion_cua == "negro":
        print("el significado es SCHWARZ")

    elif opcion_cua == "rosa":
        print("el significado es ROSA")
    
    elif opcion_cua == "morado":
        print("el significado es LILA")
    
    elif opcion_cua == "naranja":
        print("el significado es ORANGE")

    elif opcion_cua == "amarillo":
        print("el significado es GELB")

    elif opcion_cua == "blanco":
        print("el significado es WEISS")

    elif opcion_cua == "cafe":
        print("el significado es BRAUN")
        
    else:
        print("no sé el color")


if opcion == 5:
    print ("ingles a alemán")

    opcion_uno = input("escibe el color que deseas traducir ")

    if opcion_uno == "blue":
        print("el significado es BLAU")

    elif opcion_uno == "red":
        print("el significado es ROT")
    
    elif opcion_uno == "green":
        print("el significado es GRÜN")
    
    elif opcion_uno == "black":
        print("el significado es SCHWARZ")

    elif opcion_uno == "pink":
        print("el significado es ROSA")
    
    elif opcion_uno == "purple":
        print("el significado es LILA")
    
    elif opcion_uno == "orange":
        print("el significado es ORANGE")

    elif opcion_uno == "yellow":
        print("el significado es GELB")

    elif opcion_uno == "white":
        print("el significado es WEISS")

    elif opcion_uno == "brown":
        print("el significado es BRAUN")

    else:
        print("no sé el color")

print ("Gracias por usar el traductor")