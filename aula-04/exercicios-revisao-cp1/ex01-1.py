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