# profiling_example.py
import cProfile
import random

def slow_function():
    total = 0
    for _ in range(1000000):
        total += random.randint(1, 10)
    return total

def fast_function():
    return sum(random.randint(1, 10) for _ in range(1000000))

def main():
    result_slow = slow_function()
    result_fast = fast_function()
    print("Slow Function Result:", result_slow)
    print("Fast Function Result:", result_fast)

if __name__ == "__main__":
    # Perfilamos la función principal
    cProfile.run("main()")

# python profiling_example.py
#Bien, parece que has ejecutado exitosamente el perfilador cProfile. Este informe proporciona información valiosa sobre el rendimiento de tu 
# código. Aquí hay algunas observaciones:

# 1. **Llamadas a la función y Tiempo de Ejecución:**
#    - La función `slow_function` fue llamada 1 vez y llevó un total de 2.541 segundos.
#    - La función `fast_function` fue llamada 1 vez y llevó un total de 2.356 segundos.
#    - El programa en su totalidad tomó 4.897 segundos.

# 2. **Detalles de Llamadas:**
#    - Se realizaron muchas llamadas a funciones internas relacionadas con la generación de números aleatorios (`random`).
#    - La función `randint` en particular contribuyó significativamente al tiempo total de ejecución.

# 3. **Estadísticas por Llamada:**
#    - `slow_function` es más lenta en términos de tiempo de ejecución por llamada en comparación con `fast_function`.
#    - La generación de números aleatorios (`randint`, `randrange`, etc.) es una parte significativa del tiempo total.

# Basándote en esta información, podrías considerar optimizar la generación de números aleatorios o encontrar maneras de reducir la carga computacional de `slow_function` y `fast_function`.

# Si deseas sugerencias específicas sobre cómo optimizar el código, estaré encantado de ayudarte.
