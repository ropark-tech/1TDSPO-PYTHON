horas_estab = int(input("Insrira o horario de permanencia no estacionamento: "))
valor_pagar = horas_estab * 5

if valor_pagar <= 35:
    print(f"O valor a pagar é de R${valor_pagar}")
else:
    print("O valor a pagar é de R$ 35,00")