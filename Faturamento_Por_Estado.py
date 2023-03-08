faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento.values())
print("\n")
for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado} - R${valor:.2f} ({percentual:.2f}%)")
print("\n")
