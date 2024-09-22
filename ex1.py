contagem = 0
for i in range (10):
    valores = float(input("escreva os numeros: "))
    if valores < 0:
        contagem += 1
print("numero de negativos: ",contagem)