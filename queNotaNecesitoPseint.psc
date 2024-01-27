Algoritmo queNotaNecesito
	Escribir "ingrese nota del certamen 1"
	Leer C1
	Escribir "ingrese nota del certamen 2"
	Leer C2
	Escribir "ingrese nota del Laboratorio"
	Leer NL
	CN<-(59.5 - (0.3 * NL))/0.7
	C3<-3 * CN - (C1+C2) +1
	Escribir "nececita", C3, "en el certamen 3"
FinAlgoritmo
