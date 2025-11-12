import random #pelo o que eu entendi, isso serve para sortear as paradas, não sei se vamos ou não usar isso


def Regras():
    print("\n Regras \n")
    print("1. O banco de perguntas deve ter no mínimo 50 questões.")
    print("2. Cada questão é de múltipla escolha (A-E).")
    print("3. Cada questão vale 0,5 ponto.")
    print("4. A nota máxima é 10,0 pontos.")
    print("5. As perguntas e alternativas são sorteadas obrigatoriamente.")
    print("6. O código deve ser dividido em funções.")
    print("7. O código deve conter comentários explicativos.")
    print("8. O menu principal possui as opções: Responder, Regras e Encerrar.")
    print("9. O banco de perguntas deve estar embutido no código.")

def Informacoes():
    print("\n Informações do Quiz")
    print("""Este é um Quiz com o tema centrado no Arduino, abrangendo os seguintes tópicos:
1. Histórico e origem do projeto
2. Modelos e famílias de placas (Uno, Mega, Nano, etc.)
3. Componentes e arquitetura básica
4. Conexões, portas e sinais (digitais, analógicos, PWM)
5. Estrutura de código (setup, loop, funções, bibliotecas)
6. Principais comandos e funções da IDE Arduino
7. Sensores, atuadores e shields
8. Comunicações: Serial, I2C, SPI, Bluetooth, Wi-Fi
9. Boas práticas e segurança elétrica
10. Casos de uso e aplicações práticas\n""") 
# Meio que isso é o texto das informações do jogo e o de cima é sobre as regras, eu não sei se tenho \n
# que colocar as mesmas regras que o Ronildo postou no Teams, ou se tenho que rescrever elas. \n
# Me avisem se solberem da resposta


#Aqui começa o programa
while True:
    começar = input("Deseja iniciar o Quiz? Digite [S] para sim: ").upper()

    if começar == "S":
        print("Pronto para começar!\n")

        # Banco de perguntas (exemplo com 2, precisa ter 50!)
        perguntas = [
            {
                "questao": "Quem foi o principal inventor do Arduino?",
                "alternativas": ["A) Bruce Willis", "B) Mark Zuckerberg", "C) William Shakespeare", "D) Massimo Banzi", "E) David Mellis"],
            }
            {
                "questao": "Qual função é usada para configurar pinos no Arduino?",
                "alternativas": ["A) pinMode()", "B) digitalWrite()", "C) analogRead()", "D) setup()", "E) loop()"],
            }
        ]

        # Exemplo de execução simples
        for q in perguntas:
            print(q["questao"])
            for alt in q["alternativas"]:
                print(alt)
            resposta = input("Sua resposta: ").upper()
            if resposta == q["correta"]:
                print("✅ Acertouuu!\n")
            else:
                print("❌ Errouuu!\n")

    else:
        print("Opção inválida.\n")

    R = input("Deseja continuar (S/N)?: ").upper()
    if R != "S":
break