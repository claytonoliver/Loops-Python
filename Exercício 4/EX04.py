minutos = int(input("Digite os minutos atuais: "))

fatorial = 1
for i in range(1, minutos + 1):
    fatorial *= i

fatorial_minutos = fatorial

senha = "LIBERDADE" + str(fatorial_minutos)

print("A senha necessária para desbloqueio é: {}".format(senha))