nombre = input ("Cuál es tu nombre? ")
tarjeta = (input ("De que banco es tu tarjeta? "))
tipo_t = (input ("De que es tu tarjeta, debito o crédito? "))
retiro = (input("Desea hacer un retiro?"))
transferencia = (input("Desea hacer una transferencia?"))
consultar = (input("Desea ver su saldo?"))
saldo = 5000
if retiro == ("si" or "Si"):
   dinero = int(input("Cuánto dinero desea retirar?"))
   print (nombre, "retiraste $", dinero," con tu tarjeta de", tipo_t)
elif transferencia == ("si" or "Si"):
   dinero_2 = int(input("cuánto dinero desea transferir?"))
   num_cuenta = input("A que número de cuenta se va a transferir?")
   print (nombre, "transferiste $", dinero_2,"a", num_cuenta,)
elif consultar == ("si" or "Si"):
   print("Su saldo es de $5000" )
if dinero or dinero_2  > 5000:
   print ("Saldo insuficiente, su operación due canselada")
print ("Gracias por usar el cajero")

