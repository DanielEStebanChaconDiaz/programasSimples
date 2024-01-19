notas=[]
num = int(input("Cuantas notas desea agregar:\n"))
for i in range(num):
    nota = float(input(f"Ingurese la nota {i+1}:\n"))
    notas.append(nota)
snota = 0
for nota in notas:
    snota+=nota
promedio = snota/len(notas)
print(promedio)