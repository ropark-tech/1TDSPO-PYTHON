'''
Exemplo 3, em um campionato de natação a idade irá decidir a liga que o atleta ira participar,

retire - 65 - +
Senior - 19 - 64 anos;
juvenil 11 - 18 anos;
junior 5 - 10 anos;

'''

idade = int(input("Digite sua idade: "))

if idade >=5 and idade <= 10:
    print("A sua liga é a Junior")
elif idade >= 11 and idade <= 18:
    print("A sua liga é a Juvenil")
elif idade >= 19 and idade <= 65:
    print("A sua liga é a Senior")
else:
    print("A sua liga é retire")