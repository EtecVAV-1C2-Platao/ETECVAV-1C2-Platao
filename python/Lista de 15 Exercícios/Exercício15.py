resp = "sim"

while(resp=="sim"):
    ano = int(input("Digite um ano: "))

    if ano % 400 == 0:
        print("O ano " + str(ano) + " é bissexto.")
    elif ano % 100 == 0:
        print("O ano " + str(ano) + " não é bissexto.")
    elif ano % 4 == 0:
        print("O ano " + str(ano) + " é bissexto.") 
    else:
        print("O ano " + str(ano) + " não é bissexto.")  

    resp = input("Deseja continuar? \n\n(Sim/Não) ")   
