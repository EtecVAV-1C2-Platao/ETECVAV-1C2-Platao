def eh_primo(n):
    if n < 1:
        return None
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    N = int(input("Digite um número: "))
    resultado = eh_primo(N)

    if resultado is None:
        print("Somente números maiores que 1\n")
    elif resultado:
        print("O número", N, "é primo")
    else:
        print("O número", N, "não é primo")

    R = input("Deseja continuar (S/N)?: ").upper()
    if R != "S":
        break
