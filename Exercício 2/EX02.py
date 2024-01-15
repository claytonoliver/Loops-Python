diasSemana = ["Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira"]
votos = [0,0,0,0,0]
notaMaxima = 0

for i in range(5):
    votos[i] = int(input(f"Digite a quantidade de votos para {diasSemana[i]}: "))
    if votos[i] > notaMaxima:
        notaMaxima = votos[i]
        diaEscolhido = diasSemana[i]
        
print("O dia escolhido para a realização das lives é: {}.".format(diaEscolhido))





