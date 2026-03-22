macas = int(input("insira a quantidades de maçãs desejadas: "))



if macas < 12:
    custo_1 = macas * 1.3
    print(f"O Valor a pagar é R$ {custo_1:.2f}")
else:
    custo_2 = macas * 1.0
    print(f"O Valor a Pagar é R$ {custo_2:.2f}")