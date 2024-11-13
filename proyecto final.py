nombre = input ("Cuál es tu nombre? ")
producto_1 = int (input ("Cuál es precio de su primer producto? "))
producto_2 = int (input ("Cuál es precio de su segundo producto? "))
producto_3 = int (input ("Cuál es precio de su tercer producto? "))
producto_4 = int (input ("Cuál es precio de su cuarto producto? "))
subtotal = producto_1 + producto_2 + producto_3 + producto_4
porciento = .16
porciento_d = .30
descuento = subtotal * .30
descuento_2 = subtotal - descuento
iva = subtotal * porciento
total_1 = subtotal + iva
total_2 = descuento_2 + iva
print ("Su subtotal es de" , subtotal) 
if subtotal >= 500:
    print ("Tu compra es mayor a 500, tienes un descuento del 30%. El total a pagar es", total_2)
else:
    print ("Tu compra es menor a 500, no tienes descuento. El total a pagar es ", total_1)
    