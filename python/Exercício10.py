resp = "sim"

while resp == "sim":

    entrada = input("Digite os números inteiros separados por espaço: ")
    lista = [int(x) for x in entrada.split()]

    C = int(input("Digite o número C: "))

    encontrou = False

    for i in range(len(lista)):

        for j in range(i + 1, len(lista)):

            if lista[i] * lista[j] == C:

                print("Resultado:", lista[i], "e", lista[j])
                encontrou = True
                break

        if encontrou:
            break

    if not encontrou:
        print("não existem tais números.")

    resp = input("\n\nDeseja continuar? (sim/não) ")
