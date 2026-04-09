import sys

class Factorial:
    """
    Clase para calcular factoriales de números enteros
    """
    
    def __init__(self):
        """
        Constructor de la clase Factorial
        """
        self.resultados = []
        self.ultimo_min = None
        self.ultimo_max = None
    
    def _calcular_factorial(self, n):
        """
        Método privado que calcula el factorial de un número
        """
        if n < 0:
            return None
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
    def run(self, min_valor, max_valor):
        """
        Método que calcula los factoriales entre min_valor y max_valor
        
        Parámetros:
            min_valor: Límite inferior (int)
            max_valor: Límite superior (int)
        
        Retorna:
            Lista con los resultados [ (numero, factorial), ... ]
        """
        self.resultados = []
        self.ultimo_min = min_valor
        self.ultimo_max = max_valor
        
        # Validar que min_valor <= max_valor
        if min_valor > max_valor:
            print("Error: El límite inferior no puede ser mayor que el superior")
            return []
        
        # Calcular factorial para cada número en el rango
        for num in range(min_valor, max_valor + 1):
            fact = self._calcular_factorial(num)
            self.resultados.append((num, fact))
        
        return self.resultados
    
    def mostrar_resultados(self):
        """
        Muestra los resultados calculados
        """
        if not self.resultados:
            print("No hay resultados para mostrar")
            return
        
        if self.ultimo_min == self.ultimo_max:
            print(f"\nFactorial de {self.ultimo_min}:")
        else:
            print(f"\nFactoriales desde {self.ultimo_min} hasta {self.ultimo_max}:")
        print("-" * 30)
        
        for num, fact in self.resultados:
            if fact is None:
                print(f"{num}! = No definido (número negativo)")
            else:
                print(f"{num}! = {fact}")


def main():
    """
    Función principal para probar la clase Factorial
    """
    # Crear una instancia de la clase Factorial
    calc = Factorial()
    
    # Probar con diferentes casos
    
    print("=== PRUEBA 1: Factorial de 5 ===")
    print("Calculando factorial de 5...")
    calc.run(5, 5)
    calc.mostrar_resultados()
    
    print("\n" + "="*40)
    
    print("\n=== PRUEBA 2: Factoriales del 4 al 8 ===")
    print("Calculando factoriales del 4 al 8...")
    calc.run(4, 8)
    calc.mostrar_resultados()
    
    print("\n" + "="*40)
    
    print("\n=== PRUEBA 3: Factoriales del 1 al 10 ===")
    print("Calculando factoriales del 1 al 10...")
    calc.run(1, 10)
    calc.mostrar_resultados()
    
    print("\n" + "="*40)
    
    # Permitir que el usuario ingrese valores personalizados
    print("\n=== PROBAR CON VALORES PERSONALIZADOS ===")
    try:
        entrada = input("Ingrese min-max (ejemplo: 3-7): ")
        if '-' in entrada:
            partes = entrada.split('-')
            min_val = int(partes[0])
            max_val = int(partes[1])
            print(f"\nCalculando factoriales del {min_val} al {max_val}...")
            calc.run(min_val, max_val)
            calc.mostrar_resultados()
        else:
            num = int(entrada)
            print(f"\nCalculando factorial de {num}...")
            calc.run(num, num)
            calc.mostrar_resultados()
    except ValueError:
        print("Error: Ingrese un formato válido (ejemplo: 3-7 o 5)")
    except Exception as e:
        print(f"Error: {e}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()