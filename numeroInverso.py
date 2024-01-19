numero = (input("Ingrese un numero:"))
numero_inverso = ""
for i in range (len(numero)):
    numero_inverso += numero[-(i+1)]
print("el numero inverso es: ",numero_inverso)