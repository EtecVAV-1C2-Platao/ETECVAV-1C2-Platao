def media(v):
    if v == []:
        
        print("A lista está vazia.")

    elif len(v) == 1:
        print("Só tem um número. A média é:", v[0])

    else:
        soma = 0
        for numero in v:
            soma = soma + numero
        resultado = soma / len(v)
        print("A média é:", resultado)

resp = "sim"

while resp == "sim":
    entrada = input("Digite os números separados por espaço: ")
    lista = [float(x) for x in entrada.split()]
    media(lista)
    resp = input("\nDeseja continuar? (sim/não) ")