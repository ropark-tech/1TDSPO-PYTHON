'''
Escreva um programa que receba o nome e salário bruto de um funcionário. 
Calcule o valor do desconto do INSS com base na tabela abaixo: 
'''

nome = str(input("Digite o seu nome: "))
salario = float(input("Digite o seu salario: "))

if salario <= 1100:
    desconto_1 = salario * 0.075
    print(f"Voce terá um desconto de R${desconto_1:.2f}")
elif salario > 1100 and salario <= 2230.48:
    desconto_2 = salario * 0.09
    print(f"Voce terá um desconto de R${desconto_2:.2f}")
elif salario > 2203.48 and salario <= 3305.22:
    desconto_3 = salario * 0.12
    print(f"Voce terá um desconto de R${desconto_3:.2f}")
# elif salario > 2203.48 and salario <= 3305.22:
    # desconto_3 = salario * 0.12
    # print(f"Voce terá um desconto de R${desconto_3:.2f}")
else:
    desconto_4 = salario * 0.14
    print(f"Voce terá um desconto de R${desconto_4:.2f}")
