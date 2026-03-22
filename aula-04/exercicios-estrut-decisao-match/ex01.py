'''
Pela tabela a seguir, mostre a descrição e o preço do produto após a digitação do código pelo usuário. Se o produto não estiver cadastrado, emitir mensagem avisando. OBS: utilizar o Desvio Condicional de Múltipla Escolha.
'''
print("Selecione o produto desejado para consultar o preço:")
print("---- 1 - Caneta -----")
print("---- 2 - Lapis ------")
print("---- 3 - Caderno ----")
print("---- 4 - Borracha ---")
print("---- 5 - Regua ------")


produto = int(input("Digite o Codigo do produto: "))

if produto >=1 and produto <=5:
    match produto:
        case 1:
            print("Produto - Caneta")
            print("valor = R$ 1,20")
        case 2:
            print("Produto - Lapis")
            print("valor = R$ 0,80")
        case 3:
            print("Produto - Caderno")
            print("valor = R$ 4,50")
        case 4: 
            print("Produto - Borracha")
            print("valor = R$ 1,00")
        case 5:
            print("Produto - Regua")
            print("valor = R$ 1,50")
else:
    print("Produto Inexistente")