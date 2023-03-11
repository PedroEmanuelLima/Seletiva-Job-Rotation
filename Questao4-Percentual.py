# Valores mensais de faturamento de cada estado
sp = 67.83643
rj = 36.67866
mg = 29.22988
es = 27.16548
outros = 19.84953

# Valor total mensal
valor_total_mensal = sp + rj + mg + es + outros

# Percentual de representação de cada estado
percentual_sp = (sp / valor_total_mensal) * 100
percentual_rj = (rj / valor_total_mensal) * 100
percentual_mg = (mg / valor_total_mensal) * 100
percentual_es = (es / valor_total_mensal) * 100
percentual_outros = (outros / valor_total_mensal) * 100

print("Percentual de representação de cada estado:")
print("São Paulo: R${:.2f}%".format(percentual_sp))
print("Rio de Janeiro: R${:.2f}%".format(percentual_rj))
print("Minas Gerais: R${:.2f}%".format(percentual_mg))
print("Espírito Santo: R${:.2f}%".format(percentual_es))
print("Outros estados: R${:.2f}%".format(percentual_outros))