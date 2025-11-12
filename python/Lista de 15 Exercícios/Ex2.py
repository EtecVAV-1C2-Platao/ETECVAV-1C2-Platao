
tipo = input("Digite a unnidade da temperatura , C para Celsius e F para Fahrenheit :")
temperatura = float(input("Digite a quantidade da temperatura :"))

if tipo == 'C':
    celsius = 5/9 * temperatura - 32
    print("A temperatura em celsius é de",celsius,"  C°")

elif tipo == 'F':
    fahrenheit = 9/5 * temperatura + 32
    print("O valor da temperatura em fahrenheit é de ",fahrenheit,"F° ")

else:
    print("Digite somente F ou C")