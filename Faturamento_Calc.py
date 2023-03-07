def calcula_faturamento(vetor):
    # Calcula o menor e o maior valor de faturamento diário
    menor = vetor[0]
    maior = vetor[0]
    for valor in vetor:
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor

    # Calcula a média mensal de faturamento diário
    media_mensal = sum(vetor) / len(vetor)

    # Calcula o número de dias em que o faturamento diário foi superior à média mensal
    dias_acima_da_media = 0
    for valor in vetor:
        if valor > media_mensal:
            dias_acima_da_media += 1

    # Retorna os resultados
    return menor, maior, dias_acima_da_media, media_mensal


faturamento_diario = [1000, 1200, 800, 1500, 900, 1100, 1300, 1400, 950, 1000, 1100, 1200, 1300,
                      1400, 1500, 900, 1000, 1100, 1200, 1300, 1400, 1500, 900, 1100, 1200, 1300, 1400, 1500, 900]
menor, maior, dias_acima_da_media, media_mensal = calcula_faturamento(
    faturamento_diario)
print("\nMenor valor de faturamento diário: R$" + str(menor) + ".00\n")
print("Maior valor de faturamento diário: R$" + str(maior) + ".00\n")
print(f"Média mensal do Faturento diário: R${media_mensal:.2f}\n")
print("Número de dias com faturamento diário acima da média mensal: " +
      str(dias_acima_da_media)+"\n")
print("Tamanho do Vetor: " + str(len(faturamento_diario)) + "\n")
