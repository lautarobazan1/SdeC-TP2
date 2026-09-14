#include <stdio.h>

// Declaración externa: la función se implementa en calculos.s
extern int procesar_gini(float valor_float);

// Wrapper llamado por Python mediante ctypes
int ejecutar_calculo(float gini_input) {
    printf("[C] Dato recibido en C desde Python: %.2f\n", gini_input);
    
    // Invocación a la rutina en ensamblador
    int resultado = procesar_gini(gini_input);
    
    printf("[C -> ASM] Resultado procesado en Ensamblador (entero + 1): %d\n", resultado);
    return resultado;
}