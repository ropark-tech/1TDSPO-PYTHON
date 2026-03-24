'''
Uma empresa decidiu dar um bônus aos salários dos funcionários de acordo 
com o total vendido por cada um. Nesse sentido, solicite ao usuário o salário de 
um desses funcionários e qual o total de vendas que ele efetuou. Caso o total 
vendido pelo funcionário seja até R$5000.00, então o bônus será de 10%; caso 
contrário, o bônus será de 20%. Por fim, exiba o salário do funcionário com o 
bônus.
'''

salario = float(input("Insira o seu salario: "))
vendas = float(input("Insira a quantidade de vendas realizada: "))

if vendas <= 5000:
    bonus_10 = salario * 0.10
    salario_10 = bonus_10 + salario
    print(f"Voce receberá R${salario_10:.2f}")
else:
    bonus_20 = salario * 0.20
    salario_20 = bonus_20 + salario
    print(f"Voce receberá R${salario_20:.2f}")