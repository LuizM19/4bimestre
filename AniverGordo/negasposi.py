numero=[]
for i in range(10):
  numerounitario = float(input("digite a nota do aluno:"))
  numero.append(numerounitario)

  quantidade_nega = 0
  soma_posi = 0

  for numerounitario in numero: 
    if numerounitario < 0:
      quantidade_nega += 1
    if numerounitario > 0:
        soma_posi += numerounitario

print(f"Quantidade de numeros negativos é:{quantidade_nega}, e soma dos positivos:{soma_posi}")


