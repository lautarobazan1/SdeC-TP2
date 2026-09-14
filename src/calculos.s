.global procesar_gini
.type procesar_gini, @function

procesar_gini:
    # PROLOGO: Reservar e iniciar el marco de pila (Stack Frame)
    pushq   %rbp
    movq    %rsp, %rbp

    # SEGÚN LA CONVENCIÓN SYSTEM V ABI (64-bits):
    # El primer parámetro flotante ingresa en el registro vectorial %xmm0
    
    # 1. Convertir el float de %xmm0 a entero de 32 bits y guardarlo en %eax
    cvttss2si %xmm0, %eax

    # 2. Sumar 1 al valor entero almacenado en %eax
    addl    $1, %eax

    # EPILOGO: Restaurar el puntero base de la pila y retornar
    # El resultado final se devuelve en el registro %eax
    popq    %rbp
    ret
