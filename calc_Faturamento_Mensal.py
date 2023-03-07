import json

# Ler o arquivo json com os dados de faturamento mensal
with open('faturamento.json') as json_file:
    faturamento_mensal = json.load(json_file)

# Calcular o menor e o maior valor de faturamento diário ocorrido no mês
menor_faturamento = min(faturamento_mensal)
maior_faturamento = max(faturamento_mensal)

# Calcular a média mensal de faturamento diário, desconsiderando os dias sem faturamento
faturamento_sem_zero = [valor for valor in faturamento_mensal if valor != 0]
media_faturamento = sum(faturamento_sem_zero) / len(faturamento_sem_zero)

# Contar quantos dias do mês tiveram um valor de faturamento diário superior à média mensal
dias_acima_media = sum(
    valor > media_faturamento for valor in faturamento_sem_zero)

# Imprimir os resultados

print("\nMenor valor de faturamento diário: R${:.2f}".format(
    menor_faturamento) + "\n")
print("Maior valor de faturamento diário: R${:.2f}" .format(
    maior_faturamento) + "\n")
print("Média mensal do Faturento diário: R${:.2f}".format(
    media_faturamento) + "\n")
print("Número de dias com faturamento diário acima da média mensal: ".format(
    dias_acima_media) + "\n")
print("Tamanho do Vetor: " + str(len(faturamento_sem_zero)) + "\n")
