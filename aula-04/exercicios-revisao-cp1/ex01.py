'''
A jornada de trabalho semanal de um funcionário é de 40 horas. Considerando 
que o mês possua 4 semanas, o funcionário que trabalhar mais de 160 horas 
receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo 
de 50%. Escreva um algoritmo que solicite o número de horas trabalhadas em 
um mês, o salário por hora e escreva o salário total do funcionário, que deverá 
ser acrescido das horas extras, caso tenham sido trabalhadas. 
'''

horas_trabalhadas = float(input("Insira o total de horas trabalhadas no periodo de 1 mes: "))
valor_hora = float(input("Insira o valor recebido por hora trabalhada: "))

if horas_trabalhadas > 160:
    salario_n_std = valor_hora * horas_trabalhadas + ((horas_trabalhadas - 160) * valor_hora * 0.50)
    print(f"Esse mes vc receberá R${salario_n_std:.2f}")
else:
    salario_std = valor_hora * horas_trabalhadas
    print(f"Esse mes vc receberá R${salario_std:.2f}")


'''
horas_trabalhadas = float(input("Insira o total de horas trabalhadas no periodo de 1 mes: "))
valor_hora = float(input("Insira o valor recebido por hora trabalhada: "))

if horas_trabalhadas > 160:
    horas_extra = horas_trabalhadas - 160
    valor_hora_extra = valor_hora * 1.5
    salario_n_std = (160 * valor_hora) + (horas_extra * valor_hora_extra)
    print(f"Esse mes vc receberá R${salario_n_std:.2f}")
else:
    salario_std = valor_hora * horas_trabalhadas
    print(f"Esse mes vc receberá R${salario_std:.2f}")
'''