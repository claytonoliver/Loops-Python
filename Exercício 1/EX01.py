# Entrada de dados Assinatura

 
tiposAssinatura = ["Basic", "Silver", "Gold", "Platinum"]

while True:
    print("Escolha sua assinatura")
    for i in range(len(tiposAssinatura)):
        print(f"{i + 1}-{tiposAssinatura[i]}")



    assinatura = int(input("Digite o numero referente a sua assinatura: "))

    if assinatura >= 1 and assinatura <= 4:
        break
    else:
        print("\n**** Escolher de 1 a 4 ****\n")

    # Entrada de dados faturamento
faturamento = float(input("Informe Seu faturamento: "))

#Validação de assinatura e calculo sobre faturamento
if (assinatura == 1):
    bonus = faturamento * 0.30

elif assinatura == 2:
    bonus = faturamento * 0.20

elif assinatura == 3:
    bonus = faturamento * 0.10

else:
    bonus = faturamento * 0.05

# Print para o usuário
print("O valor a pagar referente a assinatura {}, é de R$: {:.2f}".format(tiposAssinatura[assinatura -1], bonus ))


