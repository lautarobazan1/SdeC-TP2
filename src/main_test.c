#include <stdio.h>

extern int procesar_gini(float valor_float);

int main() {
    float gini_prueba = 42.7f;
    printf("[Main C] Llamando a procesar_gini con valor: %.2f\n", gini_prueba);
    
    int resultado = procesar_gini(gini_prueba);
    
    printf("[Main C] Resultado devuelto por ASM: %d\n", resultado);
    return 0;
}