'''
Considerando o IMC (índice de massa corpórea), calculado como peso/(altura*altura), exiba a situação da pessoa com base na seguinte tabela:

<= 18.5 = abaixo do peso
>18.5 e <=24.9 = Peso ideal
>24.9  = Acima do peso
'''

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("Voce esta abaixo do peso ideal")
elif imc > 18.5 and imc <= 24.9:
    print("Voce esta no peso ideal")
else:
    print("Voce esta acima no peso ideal")