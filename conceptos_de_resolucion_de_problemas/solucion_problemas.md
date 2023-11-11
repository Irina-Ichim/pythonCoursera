# Resumen: Solución de Problemas de Rendimiento en un Servidor Web

En este ejercicio, aprendimos sobre la identificación y solución de problemas de rendimiento en un servidor web. Aquí están los puntos clave:

## 1. Herramientas de Evaluación de Rendimiento

- Utilizamos `ab` (Apache Benchmark) para medir el rendimiento del servidor web.
- Interpretamos los resultados de las pruebas para evaluar la velocidad de respuesta del servidor.

## 2. Diagnóstico de Problemas de Rendimiento

- Empleamos el comando `top` para examinar el uso de recursos y detectar procesos intensivos en CPU.
- Identificamos procesos problemáticos, en este caso, procesos `ffmpeg` que afectaban el rendimiento.

## 3. Prioridades de Procesos y Renice

- Cambiamos las prioridades de los procesos utilizando el comando `renice`.
- Exploramos estrategias para mejorar el rendimiento ajustando las prioridades de los procesos.

## 4. Identificación de Causas Raíz

- Examinamos la salida de `ps` para obtener información detallada sobre los procesos en ejecución.
- Determinamos la causa raíz de los problemas de rendimiento, destacando procesos `ffmpeg` en paralelo.

## 5. Optimización de Procesos

- Modificamos scripts para ejecutar procesos intensivos en CPU de manera más eficiente.
- Detuvimos y reiniciamos procesos para aplicar cambios sin interrumpir completamente las tareas en curso.

## 6. Automatización de Tareas

- Creamos scripts de shell para automatizar tareas repetitivas.
- Utilizamos bucles y comandos en shell para gestionar procesos de manera eficiente.

## 7. Evaluación de Resultados

- Interpretamos cambios en el rendimiento después de realizar ajustes.
- Confirmamos mejoras mediante pruebas adicionales.

Estos conceptos son esenciales para la administración y optimización efectiva de servidores web, especialmente al abordar problemas de lentitud o bajo rendimiento.
