import json
from datetime import datetime


def calcula_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)

    # Inicializa variáveis para cálculo do menor e maior faturamento
    menor = float('inf')
    maior = float('-inf')

    # Inicializa variáveis para cálculo da média e dias com faturamento acima da média
    soma = 0
    dias_com_faturamento = 0

    # Percorre os dados do faturamento diário
    for registro in dados:
        # Converte a data do registro para um objeto datetime
        data = datetime.strptime(registro['data'], '%d-%m-%Y')

        # Desconsidera dias sem faturamento (sábados e domingos)
        if data.weekday() >= 5:
            continue

        # Atualiza menor e maior faturamento
        faturamento = registro['valor']
        if faturamento < menor:
            menor = faturamento
        if faturamento > maior:
            maior = faturamento

        # Atualiza soma e contagem de dias com faturamento
        soma += faturamento
        dias_com_faturamento += 1

    # Calcula média e dias com faturamento acima da média
    media = soma / dias_com_faturamento
    dias_acima_da_media = 0
    for registro in dados:
        data = datetime.strptime(registro['data'], '%Y-%m-%d')
        if data.weekday() >= 5:
            continue
        faturamento = registro['valor']
        if faturamento > media:
            dias_acima_da_media += 1

    # Retorna os resultados
    return menor, maior, dias_acima_da_media


menor, maior, dias_acima_da_media = calcula_faturamento("faturamento.json")
print("Menor valor de faturamento diário:", menor)
print("Maior valor de faturamento diário:", maior)
print("Número de dias com faturamento diário acima da média mensal:",
      dias_acima_da_media)
