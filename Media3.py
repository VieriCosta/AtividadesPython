notas = input().split(" ")

nota1, nota2, nota3, nota4 = notas

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / 10

print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")

    exame = float(input())
    print("Nota do exame: %.1f" % exame)

    mediaFinal = (exame + media) / 2

    if mediaFinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: %.1f" % mediaFinal)
elif media < 5.0:
    print("Aluno reprovado.")