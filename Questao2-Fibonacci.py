# Questão2-Fibonacci

# Define os primeiros dois números da sequência de Fibonacci
f1 = 0
f2 = 1

# Ler um valor do usuário
valorLido = int(input("Digite um valor inteiro: "))

# Definir uma flag para indicar se o valor foi encontrado na sequência
encontrado = False

# Verificar se o valorLido é igual a f1 ou f2
if valorLido == f1 or valorLido == f2:
    encontrado = True

# Verifica se o valorLido faz parte da sequência de Fibonacci
while f2 < valorLido:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    if valorLido == f2:
        encontrado = True
        break

# Imprimir o resultado
if encontrado:
    print("O valor", valorLido, "faz parte da sequência de Fibonacci.")
else:
    print("O valor", valorLido, "não faz parte da sequência de Fibonacci.")