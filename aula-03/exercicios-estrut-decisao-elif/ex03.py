'''
Uma livraria resolveu fazer uma promoção, com os seguintes critérios:
o Livros com preços até R$ 10,00 - desconto de 8%
o Livros com preços de R$ 10,01 até R$ 60,00 - desconto de 10%
o Livros com preços acima de R$ 60,00 - desconto de 20%
Escreva um algoritmo que leia o preço do livro e mostre o valor do desconto oferecido, em reais.
'''

preco = float(input("Digite o preço do livro: "))

if preco <= 10:
    desconto = preco * 0.08
    preco_final = preco - desconto
    print(f"O livro custa R$ {preco_final:.2f}")
elif preco > 10 and preco <= 60:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print(f"O livro custa R$ {preco_final:.2f}")
else:
    desconto = preco * 0.60
    preco_final = preco - desconto
    print(f"O livro custa R$ {preco_final:.2f}")