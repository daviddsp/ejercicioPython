#!/usr/bin/python
# -*- coding: utf-8 -*-
numeros = [x for x in range(1,101)]
for num in range(0,len(numeros)):
	if (numeros[num] % 5 == 0) & (numeros[num]%3 == 0): #MÚLTIPLOS DE AMBOS
		numeros[num] = "FlizzBuzz"
		print "Los multiplos de ambos son :" , numeros[num]
	elif (numeros[num] % 3 == 0): #MÚLTIPLOS DE 3
		numeros[num] = "Flizz"
		print "Los multiplos de 3 son: " , numeros[num]
	elif (numeros[num] % 5 == 0): #MÚLTIPLOS DE 5
		numeros[num] = "Buzz"
		print "Los multiplos de 5 son: " , numeros[num]
	else:
		print numeros[num]
print numeros[num]	
