valor_cotacao = float(input("informe o valor do cotacao do dolar: "))
valor_dolar = float(input("informe a quantidade do dolar para converter em reais: "))

valor_real = valor_dolar * valor_cotacao

print(f"O valor em reais é: R${valor_real:.2f}")