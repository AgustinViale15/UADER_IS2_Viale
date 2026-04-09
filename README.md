# Trabajo Práctico N°1 - Gestión de la Configuración

## Información del Estudiante

- **Materia:** Ingeniería de Software II
- **Estudiante:** Agustín Viale
- **Institución:** UADER (Universidad Autónoma de Entre Ríos)
- **Fecha:** 25/03/2026

---

## Contenido del Repositorio

Este repositorio contiene los archivos correspondientes al Trabajo Práctico N°1 de la materia Ingeniería de Software II.

### Estructura de Carpetas

El repositorio está organizado con la siguiente estructura:


### Descripción de Carpetas

1. **src** - Contiene los archivos de código fuente:
   - `primes.py` - Programa que muestra números primos entre 1 y 500
   - `factorial.py` - Programa para calcular factoriales
   - `factorial_OOP.py` - Versión orientada a objetos del factorial
   - `collatz/` - Programa de la conjetura de Collatz con gráfico

2. **doc** - Destinada para la documentación del proyecto

3. **bin** - Para almacenar archivos ejecutables

4. **script** - Para scripts auxiliares y herramientas

---

## Programa primes.py

### Funcionalidad
El programa `primes.py` tiene como objetivo mostrar todos los números primos comprendidos entre 1 y 500.

### Algoritmo Implementado
1. Se definen los límites inferior y superior del intervalo
2. Se recorre cada número dentro del intervalo
3. Para cada número mayor a 1, se verifica si tiene divisores
4. Si no tiene divisores, se muestra como número primo

### Ejemplo de Ejecución
Prime numbers between 1 and 500 are:
2
3
5
7
11
13
17
...
499


---

## Programa factorial.py

### Funcionalidad
Calcula el factorial de números enteros.

### Formatos Soportados
- Número simple: `5`
- Rango: `4-8`
- Hasta límite: `-10` (calcula 1 a 10)
- Desde límite: `5-` (calcula 5 a 60)

---

## Programa factorial_OOP.py

### Funcionalidad
Versión orientada a objetos del programa factorial, implementando una clase `Factorial` con métodos para cálculo de factoriales.

---

## Programa Collatz

### Funcionalidad
Calcula la conjetura de Collatz (3n+1) para números entre 1 y 10000 y genera un gráfico.

### Gráfico Generado
Iteraciones
^
| .
| . .
| . .
| . .
|. .
+-------------------> Números


---

## Tecnologías Utilizadas

- **Python 3.13.4** - Lenguaje de programación
- **Git** - Control de versiones
- **GitHub** - Alojamiento del repositorio remoto
- **Matplotlib** - Librería para generación de gráficos

---

## Instalación y Ejecución

### Requisitos Previos
1. Python 3.x instalado
2. Git instalado
3. Pip instalado

### Pasos para ejecutar los programas

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/AgustinViale15/UADER_IS2_Viale.git

   Navegar a la carpeta del proyecto: cd UADER_IS2_Viale
   Instalar dependencias: pip install matplotlib
   Ejecutar programas: python src/primes.py
python src/factorial/factorial.py 5
python src/factorial_OOP.py 4-8
python src/collatz/collatz.py

Comandos Git Utilizados
A continuación, se presentan los comandos más importantes utilizados durante el desarrollo:

git clone - Clonar el repositorio remoto

git add . - Agregar cambios al área de staging

git commit -m "mensaje" - Confirmar cambios localmente

git push origin - Subir cambios al repositorio remoto

git pull - Descargar cambios del repositorio remoto

git status - Ver estado de los cambios

git restore - Recuperar archivos desde el repositorio

Referencias
Documentación oficial de Python - Documentación del lenguaje Python

Guía de Markdown - Sintaxis básica de Markdown

GitHub Docs - Documentación oficial de GitHub

Conjetura de Collatz - Wikipedia
