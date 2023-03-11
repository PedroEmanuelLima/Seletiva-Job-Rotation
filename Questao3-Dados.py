import json

# Lê o arquivo JSON
with open("dados.json", "r") as file:
    dados = json.load(file)

# Calcula o menor e maior valor de faturamento
menor = min(d["valor"] for d in dados)
menor_dias_uteis = min(d["valor"] for d in dados if d["valor"] > 0.0)
maior = max(d["valor"] for d in dados)

# Calcula a média mensal e o número de dias em que o valor de faturamento diário foi superior.
soma_faturamento = sum(d["valor"] for d in dados if d["valor"] > 0.0)
num_dias_com_faturamento = sum(1 for d in dados if d["valor"] > 0.0)
media_mensal = soma_faturamento / num_dias_com_faturamento
dias_acima_da_media = sum(d["valor"] > media_mensal for d in dados if d["valor"] > 0.0)

# Imprime os resultados
print("Menor valor de faturamento: R$", menor)
print("Menor valor de faturamento contando apenas dias úteis: R$", menor_dias_uteis)
print("Maior valor de faturamento: R$", maior)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)