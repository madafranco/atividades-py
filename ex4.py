total_salario = 0.0
total_filhos = 0
contagem_pessoas = 0
maior_salario = 0.0
salarios_ate_mil = 0

salario = float(input("Digite o salário (ou um valor negativo para encerrar): "))

while salario >= 0.0:
   filhos = int(input("Número de filhos: "))
   while filhos < 0:
       filhos = int(input("Outro número de filhos: "))
       
   total_salario += salario
   total_filhos += filhos
   contagem_pessoas += 1

   if salario > maior_salario:
       maior_salario = salario

   if salario <= 1000:
       salarios_ate_mil += 1

   salario = float(input("Digite o próximo salário (ou um valor negativo para encerrar): "))

if contagem_pessoas > 0:
    media_salario = total_salario / contagem_pessoas
    media_filhos = total_filhos / contagem_pessoas
    percentual_salarios_ate_mil = (salarios_ate_mil / contagem_pessoas) * 100

    print("Média do salário da população: ", media_salario)
    print("Média do número de filhos: ", media_filhos)
    print("Maior salário: ", maior_salario)
    print("Percentual de pessoas com salário até R$1000,00: %", percentual_salarios_ate_mil)
else:
    print("Nenhuma pessoa foi registrada.")
