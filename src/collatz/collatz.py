import matplotlib.pyplot as plt
import sys

class Collatz:
    def __init__(self):
        self.resultados = {}
        self.secuencias = {}
    
    def calcular_iteraciones(self, n):
        if n <= 0:
            return -1
        
        iteraciones = 0
        numero_original = n
        secuencia = [n]
        
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            secuencia.append(n)
            iteraciones += 1
        
        self.secuencias[numero_original] = secuencia
        return iteraciones
    
    def analizar_rango(self, inicio=1, fin=10000):
        print(f"Analizando números desde {inicio} hasta {fin}...")
        print("Esto puede tomar unos segundos...")
        
        for num in range(inicio, fin + 1):
            iteraciones = self.calcular_iteraciones(num)
            self.resultados[num] = iteraciones
            
            if num % 1000 == 0:
                print(f"Procesados {num} números...")
        
        print(f"¡Análisis completado! Total: {len(self.resultados)} números")
        return self.resultados
    
    def obtener_estadisticas(self):
        if not self.resultados:
            return None
        
        iteraciones = list(self.resultados.values())
        
        return {
            'max_iteraciones': max(iteraciones),
            'min_iteraciones': min(iteraciones),
            'promedio_iteraciones': sum(iteraciones) / len(iteraciones),
            'numero_max_iteraciones': max(self.resultados, key=self.resultados.get),
            'numero_min_iteraciones': min(self.resultados, key=self.resultados.get)
        }
    
    def mostrar_secuencia(self, n):
        if n not in self.secuencias:
            print(f"Número {n} no ha sido analizado aún")
            return
        
        secuencia = self.secuencias[n]
        print(f"Secuencia de Collatz para {n}:")
        print(f"Longitud: {len(secuencia)} iteraciones")
        print(f"{secuencia[:10]}..." if len(secuencia) > 10 else secuencia)
        print(f"Número de iteraciones: {self.resultados[n]}")

def generar_grafico(resultados, titulo="Conjetura de Collatz - Iteraciones por Número"):
    numeros = list(resultados.keys())
    iteraciones = list(resultados.values())
    
    plt.figure(figsize=(12, 8))
    plt.scatter(numeros, iteraciones, s=1, c='blue', alpha=0.5)
    plt.xlabel('Número de inicio (n)', fontsize=12)
    plt.ylabel('Número de iteraciones', fontsize=12)
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    max_iter = max(iteraciones)
    max_num = numeros[iteraciones.index(max_iter)]
    min_iter = min(iteraciones)
    min_num = numeros[iteraciones.index(min_iter)]
    promedio = sum(iteraciones) / len(iteraciones)
    
    texto_estadisticas = f"""
Estadísticas:
- Máximo de iteraciones: {max_iter} (n={max_num})
- Mínimo de iteraciones: {min_iter} (n={min_num})
- Promedio de iteraciones: {promedio:.2f}
    """
    
    plt.text(0.02, 0.98, texto_estadisticas, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()

def main():
    print("=" * 60)
    print("PROGRAMA: CONJETURA DE COLLATZ (3n+1)")
    print("=" * 60)
    print("\nEsta conjetura establece que para cualquier número entero positivo,")
    print("aplicando repetidamente las reglas:")
    print("  - Si es par: n = n/2")
    print("  - Si es impar: n = 3n + 1")
    print("siempre se llega al número 1.\n")
    
    collatz = Collatz()
    
    try:
        import matplotlib
        print("✓ Matplotlib encontrado")
    except ImportError:
        print("✗ Matplotlib no está instalado")
        print("  Instalalo con: pip install matplotlib")
        print("  Luego ejecutá el programa nuevamente")
        return
    
    print("\nOpciones:")
    print("1. Analizar números del 1 al 10000 (recomendado)")
    print("2. Analizar rango personalizado")
    
    opcion = input("\nSeleccione una opción (1 o 2): ").strip()
    
    if opcion == "2":
        try:
            inicio = int(input("Ingrese el número inicial: "))
            fin = int(input("Ingrese el número final: "))
            
            if inicio > fin:
                print("Error: El número inicial debe ser menor que el final")
                return
            
            if inicio < 1:
                print("Error: Los números deben ser positivos")
                return
                
            resultados = collatz.analizar_rango(inicio, fin)
        except ValueError:
            print("Error: Ingrese números válidos")
            return
    else:
        resultados = collatz.analizar_rango(1, 10000)
    
    print("\n" + "=" * 60)
    print("ESTADÍSTICAS DEL ANÁLISIS")
    print("=" * 60)
    
    estadisticas = collatz.obtener_estadisticas()
    if estadisticas:
        print(f"Números analizados: {len(resultados)}")
        print(f"Número con MÁS iteraciones: {estadisticas['numero_max_iteraciones']} ")
        print(f"  (iteraciones: {estadisticas['max_iteraciones']})")
        print(f"Número con MENOS iteraciones: {estadisticas['numero_min_iteraciones']} ")
        print(f"  (iteraciones: {estadisticas['min_iteraciones']})")
        print(f"Promedio de iteraciones: {estadisticas['promedio_iteraciones']:.2f}")
    
    print("\n" + "=" * 60)
    ver_secuencia = input("¿Desea ver la secuencia de un número específico? (s/n): ").strip().lower()
    
    if ver_secuencia == 's':
        try:
            num = int(input("Ingrese el número: "))
            collatz.mostrar_secuencia(num)
        except ValueError:
            print("Error: Ingrese un número válido")
    
    print("\n" + "=" * 60)
    print("GENERANDO GRÁFICO...")
    print("=" * 60)
    print("\nSe abrirá una ventana con el gráfico.")
    print("Cierre la ventana para finalizar el programa.\n")
    
    generar_grafico(resultados)
    
    print("\n¡Programa finalizado!")

if __name__ == "__main__":
    main()