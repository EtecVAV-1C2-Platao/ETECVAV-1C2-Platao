num1 = float(input("Digite o primeiro numero da equacao: "))
num2 = float(input("Digite o segundo numero da equacao: "))
tipo = input("Digite qual o tipo de operacao deseja realizar (+, -, *, /): ")

if tipo == "+":
    resultado = num1 + num2
elif tipo == "-":
        resultado = num1 - num2
elif tipo == "*":
        resultado = num1 * num2
elif tipo == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Nao e possivel realizar uma divisao por 0"
else:
        resultado = "Tipo de operacao invalido"
        
print ("\nresultado:", resultado)