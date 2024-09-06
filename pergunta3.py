import json

def carregar_dados(arquivo):

    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

def calcular_menor_faturamento(dados):

  faturamentos = [item['valor'] for item in dados if item['valor'] > 0]
  return min(faturamentos) if faturamentos else None

def calcular_maior_faturamento(dados):

  faturamentos = [item['valor'] for item in dados if item['valor'] > 0]
  return max(faturamentos) if faturamentos else None

def calcular_dias_acima_da_media(dados):

  faturamentos = [item['valor'] for item in dados if item['valor'] > 0]
  media = sum(faturamentos) / len(faturamentos)
  return sum(1 for valor in faturamentos if valor > media)

arquivo = "faturamento.json"
dados = carregar_dados(arquivo)

menor_valor = calcular_menor_faturamento(dados)
maior_valor = calcular_maior_faturamento(dados)
dias_acima_media = calcular_dias_acima_da_media(dados)

if menor_valor is not None:
  print(f"Menor valor de faturamento: {menor_valor}")
  print(f"Maior valor de faturamento: {maior_valor}")
  print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
else:
  print("Não há dados de faturamento válidos.")