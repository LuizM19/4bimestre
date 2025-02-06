valores = []
for i in range(10):
    valor_unitario = float(input("Digite a numero do aluno: "))

    valores.append(valor_unitario)

    posicao = 0

for i in range(10):
    if valores[posicao] < valores[i]:
        posicao = i

print(f"Maior valor: {valores[posicao]}")
print(f"Posição do maior valor: {posicao}")