c1 = int(input("ingrece la nota del certamen 1:\n"))
c2 = int(input("ingrece la nota del certamen 2:\n"))
nl = int(input("ingrece la nota de laboratorio:\n"))

nc = (59.5 - 0.3 * nl)/0.7
c3 = 3 * nc - (c1 + c2) + 1

print(f"necesita {int(round(c3))} en el certamen 3")