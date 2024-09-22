n = int(input("digite um numero inteiro e positivo: "))

if n < 0:
    print("digite um numero inteiro e positivo")
else:
    fatorial = 1
    if n > 0:
        for i in range(1, n + 1):
            fatorial *= i
print("o fatorial é: ", fatorial)