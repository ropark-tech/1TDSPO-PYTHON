bloco = int(input("Digite o seu bloco: "))

if bloco >= 1 and bloco <= 4 :
    if(bloco % 2 == 0):
       print("Seu bloco é abastecido pela Caixa A")
    else:
       print("seu bloco é abastecido pela Caixa B")
else:
    print("O bloco inserido não existe")