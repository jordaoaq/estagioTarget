def calcular_percentual_estados(faturamento):

  faturamento_total = sum(faturamento.values())

  percentuais = {}
  for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    percentuais[estado] = percentual

  return percentuais

faturamento = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

percentuais = calcular_percentual_estados(faturamento)

for estado, percentual in percentuais.items():
  print(f"{estado}: {percentual:.2f}%")