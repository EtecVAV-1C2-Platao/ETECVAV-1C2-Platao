def primo(n):
    if n >= 2:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False
    
repetir = "s"

while repetir == "s":
    n = int(input("Digite um número: "))


    if primo(n):

        maior = n + 1
        while not primo(maior):
            maior += 1

        menor = n - 1
        while menor > 2 and not primo(menor):
            menor -= 1
    


        print(f"Maior primo menor ou igual a {n} é: {menor}")
        print(f"Menor primo maior ou igual a {n} é: {maior}")

        repetir = input("Deseja tcontinuar? (s/n): ").strip().lower()

    else:
        print(f"{n} não é primo. ")

        repetir = input("Deseja tcontinuar? (s/n): ").strip().lower()
    if repetir != "s":
        print("Encerrando o programa...")
       
