'''
Uma quitanda está vendendo frutas com a seguinte tabela de preços:
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

peso_morango = float(input("Insira o seu peso do morango: "))
peso_macas = float(input("Insira o seu peso do morango: "))
## devido a falta da tabela foi usado o valor do site:
## para maçãs https://www.agrolink.com.br/cotacoes/ceasa/ceagesp---sp/frutas/maca/
## para morangos https://www.agrolink.com.br/cotacoes/ceasa/ceagesp---sp/frutas/morango/
kg_morango = 29.34
kg_macas = 7.44

valor_morango = peso_morango * kg_morango
valor_macas = peso_macas * kg_macas
peso_total = peso_morango + peso_macas
valor_total = valor_morango + valor_macas


if valor_total > 25.00:
    valor = valor_total * 0.10
    print(f"Sua compra deu R$ {valor:.2f}")
elif peso_total > 8.00:
    valor = valor_total * 0.10
    print(f"Sua compra deu R$ {valor:.2f}")
else:
    print(f"Sua compra deu R$ {valor_total:.2f}")
