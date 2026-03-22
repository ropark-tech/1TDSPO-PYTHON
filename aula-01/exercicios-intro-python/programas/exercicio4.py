peso_pessoa = float(input("digite o peso da peso: "))
altura_pessoa = float(input("digite a altura da pessoa: "))

imc = peso_pessoa / altura_pessoa ** 2
print(f"o imc da pessoa é: {imc:.2f}")