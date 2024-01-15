notasAlunosimpares = []
notasAlunosPares = []

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES\n")
for i in range(1, 50, 2):
    notaImpar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    while notaImpar != "":
        notasAlunosimpares.append(notaImpar)
        break




print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES\n")
for i in range(2,50,2):
    notaPar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    notasAlunosPares.append(notaPar)


mediaImpares = sum(notasAlunosimpares) / len(notasAlunosimpares)
mediaPares = sum(notasAlunosPares) / len(notasAlunosPares)

if mediaImpares > mediaPares:
    maiorMetade = "impares"
    maiorMedia = mediaImpares
elif mediaPares > mediaImpares:
    maiorMetade = "Pares"
    maiorMedia = mediaPares
else:
    maiorMetade = "Nenhuma"
    maiorMedia = mediaImpares

# Exibir os resultados
print("\nMédia das notas dos alunos ímpares:", mediaImpares)
print("Média das notas dos alunos pares:", mediaPares)

if maiorMetade != "nenhuma":
    print(f"A metade dos alunos com notas {maiorMetade} teve a maior média: {maiorMedia}")
else:
    print("Ambas as metades têm a mesma média.")

