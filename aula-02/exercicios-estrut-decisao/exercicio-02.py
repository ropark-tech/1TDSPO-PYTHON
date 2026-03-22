bloco = int(input("Digite o seu bloco: "))


if bloco >= 1 and bloco <= 20:
    if bloco >= 1 and bloco <=10:
        print("Seu bloco é administrado pelo sindico Sr. José.")
    else:
        print("Seu bloco é administrado pelo sindico Sr. Hamilton.")
else:
    print("O Bloco indicado não existe")