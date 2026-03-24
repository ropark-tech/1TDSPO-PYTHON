'''
Um grupo de amigos resolveu fazer um happy hour em um bar após o horário 
de trabalho. Na ocasião eles pediram porções de batatas fritas, pastéis e 
cervejas para acompanhar. Escreva um programa em Python que calcule o total 
do pedido baseado nas quantidades de porções e cervejas consumidas tendo 
como referência a tabela abaixo. Além disso, calcule o valor individual da conta 
de acordo com o número de amigos.
    - 
'''

nro_amigos = int(input("Insira a quantidade de pessoas presentes: "))
quant_cerveja = int(input("Insira a quantidade de Cervejas consumidas: "))
quant_porcao_fritas = int(input("Insira a quantidade de Fritas consumidas: "))
quant_porcao_pasteis = int(input("Insira a quantidade de pasteis consumidas: "))

comanda = quant_cerveja * 18 + quant_porcao_fritas * 35 + quant_porcao_pasteis * 25
comanda_indiv = comanda / nro_amigos

print(f"O total a pagar é R${comanda:.2f}")
print(f"Cada um terá que pagar R${comanda_indiv:.2f}")