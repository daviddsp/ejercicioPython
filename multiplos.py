#!/usr/bin/python
def listaNumeros():
    numeros = range(1,101)
    return numeros

def multiplos3():           
    listaM3 = [x for x in range(1,101) if x%3 == 0]
    return listaM3

def multiplos5():           
    listaM5 = [x for x in range(1,101) if x%5 == 0]
    return listaM5

def multiploAmbos():           
    listaAmbos = [x for x in range(1,101) if x%3 == 0 or x%5 == 0]
    return listaAmbos

numeros = listaNumeros()
cantidadValores = len(numeros)
print cantidadValores
multiplos3 = multiplos3()
cantidadValores = len(multiplos3)
print cantidadValores
print multiplos3
multiplos5 = multiplos5()
print multiplos5