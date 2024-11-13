x = int(input("escribe un número entero menor a 2000"))
while x < 2000:
    print("este es tu número", x, "y es menor a 2000, le voy a sumar uno hasta llegar al número")
    x += 1
if x == 2000:
    print("felicidades no sabes sehuir instrucciones")
else:
    print("no se hizo nada ya que escribiste un número mayor, ya pon más atención")