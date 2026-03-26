#!/usr/bin/python3
# Python program to display all the prime numbers within an interval
# Programa que determina si un número es primo

# Definir los límites del intervalo
lower = 1		# Límite inferior del intervalo
upper = 500		# Límite superior del intervalo

# Mostrar título en pantalla
print("Prime numbers between", lower, "and", upper, "are:")

# Recorrer cada número dentro del intervalo
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
