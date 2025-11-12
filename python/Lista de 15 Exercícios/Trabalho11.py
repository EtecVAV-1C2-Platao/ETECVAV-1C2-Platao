numero = 1

while numero <= 8:
    if numero == 1:
        num1 = int(input("Digite o 1º número: "))
        numero += 1
    elif numero == 2:
        num2 = int(input("Digite o 2º número: "))
        numero += 1
    elif numero == 3:
        num3 = int(input("Digite o 3º número: "))
        numero += 1
    elif numero == 4:
        num4 = int(input("Digite o 4º número: "))
        numero += 1
    elif numero == 5:
        num5 = int(input("Digite o 5º número: "))
        numero += 1
    elif numero == 6:
        num6 = int(input("Digite o 6º número: "))
        numero += 1
    elif numero == 7:
        num7 = int(input("Digite o 7º número: "))
        numero += 1
    elif numero == 8:
        num8 = int(input("Digite o 8º número: "))
        numero += 1

positivos = []
negativos = []

numero = 1
while numero <= 8:
    if numero == 1:
        if num1 >= 0:
            positivos.append(num1)
        else:
            negativos.append(num1)
        numero += 1
    elif numero == 2:
        if num2 >= 0:
            positivos.append(num2)
        else:
            negativos.append(num2)
        numero += 1
    elif numero == 3:
        if num3 >= 0:
            positivos.append(num3)
        else:
            negativos.append(num3)
        numero += 1
    elif numero == 4:
        if num4 >= 0:
            positivos.append(num4)
        else:
            negativos.append(num4)
        numero += 1
    elif numero == 5:
        if num5 >= 0:
            positivos.append(num5)
        else:
            negativos.append(num5)
        numero += 1
    elif numero == 6:
        if num6 >= 0:
            positivos.append(num6)
        else:
            negativos.append(num6)
        numero += 1
    elif numero == 7:
        if num7 >= 0:
            positivos.append(num7)
        else:
            negativos.append(num7)
        numero += 1
    elif numero == 8:
        if num8 >= 0:
            positivos.append(num8)
        else:
            negativos.append(num8)
        numero += 1

print("\nVetor de números positivos:", positivos)
print("Vetor de números negativos:", negativos)