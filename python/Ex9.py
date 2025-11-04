
sequencia1 = list(map(int, input("Digite números da primeira sequência separados por espaço: ").split()))
sequencia2 = list(map(int, input("Digite números da segunda sequência separados por espaço: ").split()))

i = 0
j = 0
resultado = []

while i < len(sequencia1) and j < len(sequencia2):
    if sequencia1[i] < sequencia2[j]:
        resultado.append(sequencia1[i])
        i += 1
    else:
        resultado.append(sequencia2[j])
        j += 1

while i < len(sequencia1):
    resultado.append(sequencia1[i])
    i += 1

while j < len(sequencia2):
    resultado.append(sequencia2[j])
    j += 1

print("A sequência resultante é:", resultado)
