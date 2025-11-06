while True:
    n = int(input("Digite um número: "))

    anterior, proximo = 0, 1
    
    print("A sequência de Fibonacci até o", n, " é:")

    for i in range(n):
        print(anterior, end=" ")
        anterior, proximo = proximo, anterior + proximo

    print ()
    
    R = input ("Deseja continuar (S/N)?: ").upper()
    if R != "S":
     break