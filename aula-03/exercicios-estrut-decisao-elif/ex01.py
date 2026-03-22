'''
Escreva um programa que pergunte em qual mês estamos (1-12) e ao final utilize uma estrutura de decisão por seleção para escrever o nome do mês por extenso na tela.
'''

mes = int(input("Digite o mes atual: "))

if mes >= 1 and mes <= 12:
    if mes == 1:
        print("O mes atual é Janeiro.")
    elif mes == 2:
        print("O mes atual é Fevereiro.")
    elif mes == 3:
        print("O mes atual é Março.")
    elif mes == 4:
        print("O mes atual é Abril.")
    elif mes == 5:
        print("O mes atual é Maio.")
    elif mes == 6:
        print("O mes atual é Junho.")
    elif mes == 7:
        print("O mes atual é Julho.")
    elif mes == 8:
        print("O mes atual é Agosto.")
    elif mes == 9:
        print("O mes atual é Setembro.")
    elif mes == 10:
        print("O mes atual é Outubro.")
    elif mes == 11:
        print("O mes atual é Novembro.")
    elif mes == 12:
        print("O mes atual é Desembro.")
else:
     print("O mes digitado não existe")