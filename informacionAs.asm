global calcular_conversion
section .text

calcular_conversion:
	movsd xmm1, [rel factor]
	mulsd xmm0, xmm1
	ret ; Devuelve el resultado guardado en xmm0

section .data
	factor: dq 2.0

