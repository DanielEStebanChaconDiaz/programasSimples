ha = int(input("Hora actual:\n"))
hf = int(input("Horas futuras:\n"))
i = 1
ht = 0
for i in range (hf):
    ht = (ha + hf)%24
print(f"La hora futura es:{ht}")