Algoritmo numeroInvertido
	Definir cadena, invertir como cadena
	cadena <- "223"
	invertir <- ""
	para i <- Longitud(cadena) hasta 1 con paso -1
		inverso <- invertir + Subcadena(cadena, i, 3)
	FinPara
	escribir inverso
FinAlgoritmo