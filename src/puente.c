#include <stdio.h>

// Función que realiza el cálculo de conversión
int procesar_gini(float valor_float) {
    int entero = (int)valor_float;
    return entero + 1;
}

// Wrapper que será llamado desde Python
int ejecutar_calculo(float gini_input) {
    printf("[C] Dato recibido en C desde Python: %.2f\n", gini_input);
    int resultado = procesar_gini(gini_input);
    printf("[C] Resultado procesado (convertido a entero + 1): %d\n", resultado);
    return resultado;
}