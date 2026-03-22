'''
Crie um menu com 4 opções (vide abaixo), que devem ser executadas com 2 números inteiros informados pelo usuário. As opções são as seguintes:

Opcao = 1: verificar qual é o maior número.

Opcao = 2: verificar se o primeiro número é par ou ímpar.

Opcao = 3: verificar qual é o menor número.
'''

num_1 = int(input("Digite um Numero Inteiro: "))
num_2 = int(input("Digite um Numero Inteiro: "))


print("Selecione uma opção para:")
print("------- 1 - Verificar qual é o maior ------------------------")
print("------- 2 - verificar se primeiro numero é par ou impar------")
print("------- 3 - Verificar qual é o menor ------------------------")
print("------- 4 - verificar se segundo numero é par ou impar-------")

options = int(input("Escolha uma das opções: "))

if options >= 1 and options <= 4:
    match options:
        case 1:
            if num_1 > num_2:
                print(f"{num_1} é maior que {num_2}.")
            else:
                print(f"{num_2} é maior que {num_1}.")
        case 2:
            if num_1 % 2 == 0:
                print(f"{num_1} é par")
            else:
                print(f"{num_1} é impar")
        case 3:
            if num_1 > num_2:
                print(f"{num_2} é menor que {num_1}.")
            else:
                print(f"{num_1} é menor que {num_2}.")
        case 4:
            if num_2 % 2 == 0:
                print(f"{num_2} é par")
            else:
                print(f"{num_2} é impar")
else:
    print("Opção Inexistente")