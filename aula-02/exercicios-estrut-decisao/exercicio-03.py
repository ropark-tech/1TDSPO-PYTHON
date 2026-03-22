valor_merc = float(input("Insira o valor da compra: "))

valor_user = float(input("Insira o valor presente na carteira: "))

if valor_user >= valor_merc:
    print("Voce consegue comprar")
else:
    print("Voce nao consegue comprar")
