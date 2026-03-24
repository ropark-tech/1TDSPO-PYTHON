'''
Desenvolva um programa que receba os dados de duas pessoas: nome e altura. 
Exiba o nome da pessoa mais alta. 
'''

nome_pessoa_1 = str(input("Digite o seu nome: "))
altura_pessoa_1 = float(input("Digite a sua altura"))
nome_pessoa_2 = str(input("Digite o seu nome: "))
altura_pessoa_2 = float(input("Digite a sua altura"))

if altura_pessoa_1 > altura_pessoa_2:
    print(f"{nome_pessoa_1} é a pessoa mais alta.")
elif altura_pessoa_1 == altura_pessoa_2:
    print(f"{nome_pessoa_1} e {nome_pessoa_2} tem a mesma altura.")
else:
    print(f"{nome_pessoa_2} é a pessoa mais alta.")