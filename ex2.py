for i in range(20):
    valor = float(input("digite os valores: "))

    if i == 0:
        maior = valor
        menor = valor

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print("numero maior: ", maior)
print("numero menor: ", menor)