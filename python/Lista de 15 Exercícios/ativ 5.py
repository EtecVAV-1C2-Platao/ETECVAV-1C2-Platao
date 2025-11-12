while True:
    n = int(input("Digite um número: "))

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != "s":
        print("Programa encerrado.")
        break
