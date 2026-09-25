#include <stdio.h>
#include <stdlib.h>

extern double calcular_conversion(double valor);

int main (int argc, char *argv[]){
	double valor_api = 42.7 ; 

	if (argc > 1){
	valor_api = atof(argv[1]);
	}
	
	printf("resultado de la api: %.2f\n", valor_api);
	
	double resultado =  calcular_conversion(valor_api);

	printf("Resultado devuelto por Assembler %.2f\n", resultado")
	
	return 0;
}

