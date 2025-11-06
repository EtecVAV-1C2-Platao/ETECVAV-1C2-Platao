while True:
    def soma(n):
        total = 0
        for i in range(n + 1):
            total += i
        return total

    print("Vamos calcular a soma de 0 até o número que você quiser.")
    numero = int(input("Digite um número inteiro: "))

    resultado = soma(numero)

    print("A soma de 0 até", numero, "é", resultado)

    R = input("Deseja continuar (S/N)?: ").upper()
    if R != 'S':
        break
