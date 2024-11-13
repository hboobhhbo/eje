print ("este es un cuento de aventuras ")
nombre = input ("cuál es tu nombre? ")
print ("ok" + nombre + "necesito saber si eres mayor de edad")

print ("presiona 1 si eres mayor de edad y deseas continuar")
print ("presiona 2 si eres menor de edad y deseas continuar")
print ("presiona 3 si no deseas continuar")

opcion = int(input("Escribe la opción que quieras escojer "))

if opcion == 1:
    print ("tenemos a un mayor de edad")

    opcion_uno = input ("escribe el animal que quieras, entre burro y jirafa ")

    if opcion_uno == "burro":
        print ("elegiste burro")

        if opcion_uno == "burro":
            opcion_uno = input("escribe que te da más miedo, quedarte perdido, caer o que te patee")
            print(nombre + " entonces lo que más miedo te da al estar con el burro es " + opcion_uno + "?")
            opcion_uno = input ("si o no?")

            if opcion_uno == "si":
                print ("no le tienes que tener miedo a eso, de hecho los burros son muy longevos y resistentes")
            elif opcion_uno == "no":
                print ("te equivocaste, vuelve a empezar")
    
    elif opcion_uno == "jirafa":
        print ("elegiste jirafa")

        if opcion_uno == "jirafa":
            opcion_uno = input("escribe que te da más miedo, su tamaño, que te lama o que te pise")
            print(nombre + " entonces lo que más miedo te da al estar con el burro es " + opcion_uno + "?")
            opcion_uno = input ("si o no?")

            if opcion_uno == "si":
                print ("no le tienes que tener miedo a eso, de hecho las jirafas pasan mucho tiempo con la lengua fuera de la boca y el color azul actúa como una especie de crema solar.")
            elif opcion_uno == "no":
                print ("te equivocaste, vuelve a empezar")

if opcion == 2:
    print ("tenemos a un menor de edad")

    opcion_uno = input ("escribe el animal que quieras, entre burro y jirafa ")

    if opcion_uno == "burro":
        print ("elegiste burro")

        if opcion_uno == "burro":
            opcion_uno = input("escribe que te da más miedo, quedarte perdido, caer o que te patee")
            print(nombre + " entonces lo que más miedo te da al estar con el burro es " + opcion_uno + "?")
            opcion_uno = input ("si o no?")

            if opcion_uno == "si":
                print ("no le tienes que tener miedo a eso, de hecho los burros son muy longevos y resistentes")
            elif opcion_uno == "no":
                print ("te equivocaste, vuelve a empezar")
    
    elif opcion_uno == "jirafa":
        print ("elegiste jirafa")

        if opcion_uno == "jirafa":
            opcion_uno = input("escribe que te da más miedo, su tamaño, que te lama o que te pise")
            print(nombre + " entonces lo que más miedo te da al estar con el burro es " + opcion_uno + "?")
            opcion_uno = input ("si o no?")

            if opcion_uno == "si":
                print ("no le tienes que tener miedo a eso, de hecho las jirafas pasan mucho tiempo con la lengua fuera de la boca y el color azul actúa como una especie de crema solar.")
            elif opcion_uno == "no":
                print ("te equivocaste, vuelve a empezar")

if opcion == 3:
    print("esta bien, reinicia cuando quieras continuar")

