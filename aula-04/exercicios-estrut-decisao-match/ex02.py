'''
Baseado em um número real X (float) digitado pelo usuário, utilize o desvio condicional de múltipla escolha e faça as seguintes operações:


Opcao = 1: adicione 5 ao valor de X e exiba na tela.

Opcao = 2: subtraia 4 ao valor de X e exiba na tela.

Opcao = 3: dobre o valor de X e exiba na tela.
'''

print("Selecione uma opção para realizar uma operação matematica:")
print("------- 1 - Somar 5 -------------")
print("------- 2 - Subtrair 4 ----------")
print("------- 3 - mutiplicar pro 2 ----")

options = int(input("Escolha uma das opções: "))

if options >= 1 and options <= 3: 
    num_real = float(input("Digite um numero real: "))
    match options:
        case 1:
            num_op1 = num_real + 5
            print(num_op1)
        case 2:
            num_op2 = num_real - 4
            print(num_op2)
        case 3:
            num_op3 = num_real * 2
            print(num_op3)
else:
    print("Opção Inexistente")