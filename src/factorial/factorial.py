#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(n):
   
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


if len(sys.argv) > 1:
    
    try:
        numero = int(sys.argv[1])
    except ValueError:
        print("Error: El argumento debe ser un número entero")
        sys.exit(1)
else:
    
    try:
        numero = int(input("Ingrese un número para calcular su factorial: "))
    except ValueError:
        print("Error: Debe ingresar un número entero")
        sys.exit(1)


if numero < 0:
    print("Error: El factorial no está definido para números negativos")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
