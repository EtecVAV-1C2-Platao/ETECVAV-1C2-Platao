import math
numero = 1

while numero <= 5:
    if numero == 1:
        num1 = int(input ("Digite o primeiro numero desejado: "))
        numero += 1
    elif numero == 2:
        num2 = int(input ("Digite o segundo numero desejado: "))
        numero += 1
    elif numero == 3:
        num3 = int(input ("Digite o terceiro numero desejado: "))
        numero += 1
    elif numero == 4:
        num4 = int(input ("Digite o quarto numero desejado: "))
        numero += 1
    elif numero == 5:
        num5 = int(input ("Digite o quinto numero desejado: "))
        numero += 1
        
numero = 1        
while numero <= 5:
    if numero == 1:
        fato1 = math.factorial (num1)
        numero += 1
    elif numero == 2:
        fato2 = math.factorial (num2)
        numero += 1
    elif numero == 3:
        fato3 = math.factorial (num3)
        numero += 1
    elif numero == 4:
        fato4 = math.factorial (num4)
        numero += 1
    elif numero == 5:
        fato5 = math.factorial (num5)
        numero += 1

soma = fato1+fato2+fato3+fato4+fato5
print ("o resultado e: ", soma)