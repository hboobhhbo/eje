print("Calculador de promedio")
nombre = input("¿Cuál es tu nombre? ")
perspectivas_del_mundo_actual = int(input(nombre + " Dime tu calificación de perspectivas del mundo actual: "))
ingles = int(input(nombre + " Dime tu calificación de ingles: "))
informatica = int(input(nombre + " Dime tu calificación de informática: "))
quimica = int(input(nombre + " Dime tu calificación de química: "))
matematicas = int(input(nombre + " Dime tu calificación de mathe: "))
espanol = int(input(nombre + " Dime tu calificación de español: "))
yo_y_los_demás = int(input(nombre + " Dime tu calificación de Yo y los demás: "))
promedio = (perspectivas_del_mundo_actual + ingles + informatica + quimica + matematicas + espanol + yo_y_los_demás) / 7 

if promedio >= 70: 
    print(nombre + " aprobaste regular con", promedio )
elif promedio >= 80: 
    print(nombre + " aprobaste normal con", promedio )
elif promedio >= 90: 
    print(nombre + " aprobaste muy bien, con", promedio )
elif promedio >= 95: 
    print(nombre + " aprobaste con exelencia con", promedio )
else:
    print(nombre + " reprobaste repite el año con", promedio )