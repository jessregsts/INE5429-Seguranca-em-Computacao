def lfsr_galois():
    estado_inicial = 0xACE1  # Qualquer estado inicial diferente de zero funciona
    lfsr = estado_inicial
    periodo = 0

    while True:
        lsb = lfsr & 1  # Obtém o bit menos significativo (bit de saída)
        lfsr >>= 1      # Desloca o registrador para a direita

        if lsb == 1:    # Se o bit de saída for 1
            lfsr ^= 0xB400  # Aplica a máscara de realimentação (tap positions)

        periodo += 1

        if lfsr == estado_inicial:
            break  # O ciclo completo foi alcançado

    return periodo

# Exemplo de uso
print("Período do LFSR (configuração de Galois):", lfsr_galois())

#0xACE1: é o valor inicial do registrador (pode ser alterado, mas não deve ser zero).

#0xB400: é a máscara de realimentação (tap mask) usada no deslocamento para a direita (Galois).

#Isso corresponde aos taps em posições específicas para um LFSR de 16 bits.

#A função retorna o período completo até o estado in