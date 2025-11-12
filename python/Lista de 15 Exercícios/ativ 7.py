seq1 = list(map(int, input("Primeira sequência: ").split()))
seq2 = list(map(int, input("Segunda sequência: ").split()))

n = len(seq1)
m = len(seq2)
contador = 0


for i in range(m - n + 1):
    if seq2[i:i + n] == seq1:
        contador += 1

print("Resultado:", contador)
