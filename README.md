# Sistemas de Computación
# Trabajo Práctico 2 - Procesamiento Multicapa e Inspección del Stack Frame (Índice GINI)

**Integrantes:**
- Aguilar Bazán, Lautaro Ismael
- Faro, Tomás Martin
- Monaldi, Renata


---


## 📌 1. Descripción del Proyecto y Arquitectura

Este proyecto implementa una solución en **arquitectura de tres capas** para obtener, transmitir y procesar el indicador socioeconómico **GINI** del Banco Mundial:

1. **Capa Superior (Python - Ingesta de datos API REST):**  
   Consume la API REST del Banco Mundial para recuperar el índice GINI en formato JSON (`https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?...`). Los datos procesados se transfieren a la capa C mediante la librería estándar `ctypes`.

2. **Capa Intermedia (C - Puente/Wrapper):**  
   Gestiona el enlace dinámico y la llamada a bajo nivel mediante una librería compartida (`libpuente.so`), coordinando la transferencia de parámetros hacia la rutina en ensamblador.

3. **Capa Inferior (Ensamblador x86_64 - Lógica de Cómputo):**  
   Recibe el valor del índice GINI en punto flotante (`float`), realiza la conversión a entero truncado, le incrementa una unidad (`+1`) y devuelve el resultado final aplicando la convención de llamadas **System V AMD64 ABI**.

---
