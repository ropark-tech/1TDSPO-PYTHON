# Exemplo 2, verficiar se o aluno foi aprovado, reprovado ou esta de exme

# aprovado >= 7
# exame entre 4 e 6.0
# reprovado < 4.0

media = float(input("insira o valor da Media: "))

if media >= 0 and media <= 10:
    if media >= 7:
        print("Aluno aprovado")
    elif media >= 4 and media <= 7:
        print("Aluno de exame")
    else:
        print("Aluno reprovado")
else:
    print("media invalida")