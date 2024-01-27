Algoritmo horafutura 
	i=0
	Escribir "ingrese la hora actual"
	Leer HA
	Escribir "ingrese la hora futura"
	Leer HF
	si i <=24
		HT = (HA+HF) MOD 24
		Escribir "dentro de " , HF , " seran las " , HT
	FinSi
FinAlgoritmo