#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Constantes para límites por defecto
LIMITE_SUPERIOR_POR_DEFECTO = 60
LIMITE_INFERIOR_POR_DEFECTO = 1

def factorial(n):
    """
    Calcula el factorial de un número n
    Parámetros:
        n: Número entero no negativo
    Retorna:
        El factorial de n, o None si n es negativo
    """
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def procesar_rango(texto):
    """
    Procesa diferentes formatos de entrada:
    - "5" -> (5, 5)
    - "4-8" -> (4, 8)
    - "-10" -> (1, 10)
    - "5-" -> (5, 60)
    
    Parámetros:
        texto: Cadena de entrada del usuario
    Retorna:
        Tupla (desde, hasta) con los límites del rango
    """
    texto = texto.strip()
    
    # Caso: "-hasta" (ej. -10) - calcula desde 1 hasta el número
    if texto.startswith('-') and texto.count('-') == 1:
        hasta = int(texto[1:])
        desde = LIMITE_INFERIOR_POR_DEFECTO
        return desde, hasta
    
    # Caso: "desde-" (ej. 5-) - calcula desde el número hasta 60
    if texto.endswith('-') and texto.count('-') == 1:
        desde = int(texto[:-1])
        hasta = LIMITE_SUPERIOR_POR_DEFECTO
        return desde, hasta
    
    # Caso: "desde-hasta" (ej. 4-8)
    if '-' in texto:
        partes = texto.split('-')
        if len(partes) == 2:
            desde = int(partes[0])
            hasta = int(partes[1])
            return desde, hasta
    
    # Caso: número simple (ej. 5)
    num = int(texto)
    return num, num

def mostrar_resultados(desde, hasta):
    """
    Calcula y muestra los factoriales en el rango especificado
    """
    if desde > hasta:
        print("Error: El límite inferior no puede ser mayor que el superior")
        return
    
    # Mostrar encabezado según el tipo de cálculo
    if desde == hasta:
        print(f"Calculando factorial de {desde}:")
    else:
        print(f"Calculando factoriales desde {desde} hasta {hasta}:")
    print("-" * 30)
    
    # Calcular y mostrar cada factorial
    for num in range(desde, hasta + 1):
        if num < 0:
            print(f"{num}: Factorial no definido (números negativos no tienen factorial)")
        else:
            resultado = factorial(num)
            print(f"{num}! = {resultado}")

def mostrar_ayuda():
    """
    Muestra las instrucciones de uso del programa
    """
    print("=== Calculadora de Factoriales ===")
    print("Formatos aceptados:")
    print("  - Número simple: 5")
    print("  - Rango: 4-8")
    print("  - Hasta límite: -10 (calcula 1 a 10)")
    print("  - Desde límite: 5- (calcula 5 a 60)")
    print("==================================")

def main():
    """
    Función principal del programa
    """
    # Si no hay argumentos, mostrar ayuda y solicitar entrada
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
        # Si el argumento es --help o -h, mostrar ayuda
        if entrada in ['--help', '-h']:
            mostrar_ayuda()
            return
    else:
        mostrar_ayuda()
        entrada = input("\nIngrese número o rango: ")
    
    try:
        desde, hasta = procesar_rango(entrada)
        mostrar_resultados(desde, hasta)
                
    except ValueError:
        print("\nError: Formato inválido.")
        print("Use números enteros. Ejemplos válidos:")
        print("  - Número: 5")
        print("  - Rango: 4-8")
        print("  - Hasta: -10")
        print("  - Desde: 5-")

# Punto de entrada del programa
if __name__ == "__main__":
    main()