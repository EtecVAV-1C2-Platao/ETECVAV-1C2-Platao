import random #pelo o que eu entendi, isso serve para sortear as paradas, não sei se vamos ou não usar isso

def Mostrar_Regras():
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

def Mostrar_Informacoes():
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

def Sortear_perguntas(perguntas, quantidade=20):
    return random.sample(perguntas, quantidade)

def Exibir_pergunta(pergunta):
    print("\n" + pergunta["questao"])
    for alternativa in pergunta["alternativas"]:
        print(alternativa)

def Verificar_Resposta(pergunta, resposta):
    if resposta == pergunta["correta"]:
        print("✅ Acertouuu!\n")
        return True
    else:
        print(f"❌ Errouuu! A resposta correta era: {pergunta['correta']}\n")
        return False
perguntas = [
            {
                "questao": "Quem foi o principal inventor do Arduino?",
                "alternativas": [
                    "A) Bruce Willis", 
                    "B) Mark Zuckerberg", 
                    "C) William Shakespeare", 
                    "D) Massimo Banzi", 
                    "E) David Mellis"
                ],
                "correta": "D"
            },
            {
                "questao": "Qual função é usada para configurar pinos no Arduino?",
                "alternativas": [
                    "A) pinMode()", 
                    "B) digitalWrite()", 
                    "C) analogRead()", 
                    "D) setup()", 
                    "E) loop()"
                ],
                "correta": "A"
            },
            {
                "questao": "Em que ano a plataforma do Arduino foi iniciada?",
                "alternativas": [
                    "A) 1986", 
                    "B) 2011", 
                    "C) 1930", 
                    "D) 2010", 
                    "E) 2005"
                ],
                "correta": "E"
            },
            {
                "questao": "O que é o Arduino?",
                "alternativas": [
                    "A) Uma plataforma que possibilita o desenvolvimento de projetos eletrônicos. Em outras palavras, é uma plataforma de prototipagem eletrônica.",
                    "B) Um monumento da arquitetura moderna, baseado em artes antigas e inspirado na filosofia do platonismo.",
                    "C) Um software de código aberto utilizado para criação de aplicativos interativos e sistemas embarcados.",
                    "D) Um conjunto de ferramentas destinado à simulação de circuitos elétricos em ambiente virtual.",
                    "E) Um microcontrolador utilizado para o controle e automação de dispositivos eletrônicos."
                ],
                "correta": "A"
            },
            {
                "questao": "O que significa IDE no contexto do Arduino?",
                "alternativas": [
                    "A) Integrated Development Environment", 
                    "B) Input Device Emulator",
                    "C) Internal Debug Engine", 
                    "D) Intelligent Digital Editor", 
                    "E) Internet Device Emulator"
                ],
                "correta": "A"
            },
            {
                "questao": "Qual extensão de arquivo é usada nos projetos do Arduino?",
                "alternativas": [
                    "A) .ino", 
                    "B) .exe",  
                    "C) .cpp", 
                    "D) .py", 
                    "E) .txt"
                ],
                "correta": "A"
            },
            {
               # "questao": "Qual componente é usado para armazenar carga elétrica?",
                #"alternativas": [
                 #   "A) Resistor",
                 #   "B) Diodo",
                 #   "C) Capacitor",
                 #   "D) Transistor",
                  #  "E) Indutor"
               # ],
                #"correta": "C"
            },
            {
                "questao": "Quantos pinos digitais possui o Arduino Uno?",
                "alternativas": [
                    "A) 8",
                    "B) 10",
                    "C) 12",
                    "D) 14",
                    "E) 16"
                ],
                "correta": "D"
            },
            {
                "questao": "Qual é o microcontrolador usado no Arduino Uno?",
                "alternativas": [
                    "A) ATmega16",
                    "B) ATmega32",
                    "C) ATmega328P",
                    "D) ATmega2560",
                    "E) PIC16F877A"
                ],
                "correta": "C"
            },
            {
                "questao": "Qual pino do Arduino é usado para enviar dados via comunicação serial?",
                "alternativas": [
                    "A) 0 (RX)",
                    "B) 1 (TX)",
                    "C) 2",
                    "D) 13",
                    "E) A0"
                ],
                "correta": "B"
            },
            {
                "questao": "Qual comando é usado para imprimir informações no monitor serial?",
                "alternativas": [
                    "A) Serial.begin()",
                    "B) Serial.print()",
                    "C) Serial.end()",
                    "D) Serial.read()",
                    "E) Serial.write()"
                ],
                "correta": "B"
            },
            {
                "questao": "Qual a voltagem operacional do Arduino Uno?",
                "alternativas": [
                    "A) 3.3V",
                    "B) 5V",
                    "C) 9V",
                    "D) 12V",
                    "E) 7.5V"
                ],
                "correta": "B"
            },
            {
                "questao": "O que faz a função delay(1000) no código do Arduino?",
                "alternativas": [
                    "A) Para o programa por 1000 microssegundos",
                    "B) Para o programa por 1 segundo",
                    "C) Reinicia o loop após 1 segundo",
                    "D) Cria uma pausa indefinida",
                    "E) Interrompe a alimentação"
                ],
                "correta": "B"
            },
            {
                "questao": "Qual destes sensores mede temperatura?",
                "alternativas": [
                    "A) LDR",
                    "B) DHT11",
                    "C) HC-SR04",
                    "D) MPU6050",
                    "E) MQ-2"
                ],
                "correta": "B"
            },
            {
                "questao": "Qual comando é usado para ler o valor de um sensor analógico?",
                "alternativas": [
                    "A) analogRead()",
                    "B) digitalRead()",
                    "C) analogWrite()",
                    "D) digitalWrite()",
                    "E) sensorRead()"
                ],
                "correta": "A"
            },
            {
                "questao": "Qual tipo de variável pode armazenar valores como 'a', 'b', 'c'?",
                "alternativas": [
                    "A) int",
                    "B) float",
                    "C) bool",
                    "D) char",
                    "E) string"
                ],
                "correta": "D"
            },
            {
                #"questao": "Qual destes componentes converte energia elétrica em luz?",
                #"alternativas": [
                #    "A) LDR",
                 #   "B) LED",
                  #  "C) Potenciômetro",
                   # "D) Servo motor",
                    #"E) Buzzer"
                #],
                #"correta": "B"
            },
            {
               # "questao": "Qual é a função do resistor?",
                #"alternativas": [
                 #   "A) Armazenar energia",
                  #  "B) Controlar a corrente elétrica",
                   # "C) Converter energia em calor",
                    #"D) Aumentar a tensão",
                    #"E) Medir a resistência"
                #],
                #"correta": "B"
            },
            {
                "questao": "O que o comando 'setup()' faz em um programa Arduino?",
                "alternativas": [
                    "A) Repete o código continuamente",
                    "B) Executa uma vez ao iniciar o programa",
                    "C) Configura pinos analógicos",
                    "D) Reinicia o microcontrolador",
                    "E) Lê entradas digitais"
                ],
                "correta": "B"
            },
            {
                "questao": "O que o comando 'loop()' faz em um programa Arduino?",
                "alternativas": [
                    "A) Executa apenas uma vez",
                    "B) Define o início do programa",
                    "C) Repete o código continuamente",
                    "D) Configura pinos digitais",
                    "E) Envia dados para o serial"
                ],
                "correta": "C"
            },
            {
                "questao": "Qual comando é usado para acender um LED?",
                "alternativas": [
                    "A) digitalWrite(pino, HIGH)",
                    "B) digitalRead(pino)",
                    "C) analogRead(pino)",
                    "D) pinMode(pino, INPUT)",
                    "E) delay(1000)"
                ],
                "correta": "A"
            },
            {
         #       "questao": "Qual sensor é usado para medir distância?",
          #      "alternativas": [
           #         "A) DHT11",
            #        "B) HC-SR04",
             #       "C) LDR",
              #      "D) BMP280",
               #     "E) MQ-135"
                #],
                #"correta": "B"
            },
            {
                "questao": "Qual protocolo é usado para comunicação sem fio com o módulo ESP8266?",
                "alternativas": [
                    "A) SPI",
                    "B) I2C",
                    "C) UART",
                    "D) Wi-Fi",
                    "E) Bluetooth"
                ],
                "correta": "D"
            },
            {
                "questao": "Qual componente é usado para controlar motores de forma precisa?",
                "alternativas": [
                    "A) LED",
                    "B) Servo motor",
                    "C) Potenciômetro",
                    "D) Resistor",
                    "E) Buzzer"
                ],
                "correta": "B"
            },
            {
                "questao": "Qual biblioteca é usada para controlar servos no Arduino?",
                "alternativas": [
                    "A) Wire.h",
                    "B) Servo.h",
                    "C) SPI.h",
                    "D) Motor.h",
                    "E) PWM.h"
                ],
                "correta": "B"
            },
            {
                "questao": "O que significa PWM no Arduino?",
                "alternativas": [
                    "A) Power With Motion",
                    "B) Pulse Width Modulation",
                    "C) Programmed Wire Mode",
                    "D) Peripheral Write Method",
                    "E) Power Wave Management"
                ],
                "correta": "B"
            },
            {
                "questao": "Qual comando inicializa a comunicação serial no Arduino?",
                "alternativas": [
                    "A) Serial.begin(9600)",
                    "B) Serial.start(9600)",
                    "C) Serial.print(9600)",
                    "D) Serial.read(9600)",
                    "E) Serial.connect(9600)"
                ],
                "correta": "A"
            },
            {
                "questao": "Qual comando é usado para definir um pino como saída?",
                "alternativas": [
                    "A) pinMode(pino, OUTPUT)",
                    "B) digitalWrite(pino, HIGH)",
                    "C) digitalRead(pino)",
                    "D) analogRead(pino)",
                    "E) setup(pino)"
                ],
                "correta": "A"
            },
            {
                "questao": "O que a função 'analogWrite()' faz?",
                "alternativas": [
                    "A) Lê um valor analógico",
                    "B) Escreve um valor analógico (PWM)",
                    "C) Define o modo de pino",
                    "D) Envia dados para o serial",
                    "E) Reinicia o programa"
                ],
                "correta": "B"
            },
            {
                "questao": "Qual pino é geralmente usado para o LED embutido no Arduino Uno?",
                "alternativas": [
                    "A) 7",
                    "B) 9",
                    "C) 10",
                    "D) 13",
                    "E) A0"
                ],
                "correta": "D"
            },
            {
                "questao": "Em que país o projeto Arduino foi criado?",
                "alternativas": [
                    "A) Estados Unidos",
                    "B) Itália",
                    "C) Alemanha",
                    "D) Japão",
                    "E) França"
                ],
                "correta": "B"
            },
            {
                "questao": "O nome 'Arduino' foi inspirado em:",
                "alternativas": [
                    "A) Um tipo de microcontrolador",
                    "B) Uma placa protótipo antiga",
                    "C) Um bar na Itália frequentado pelos criadores",
                    "D) O nome do primeiro computador usado no projeto",
                    "E) O sobrenome de um dos fundadores"
                ],
                "correta": "C"
            },
            {
                "questao": "Qual é a principal diferença entre o Arduino Uno e o Arduino Mega?",
                "alternativas": [
                    "A) O Mega possui mais pinos e memória",
                    "B) O Uno é mais rápido que o Mega",
                    "C) O Mega é menor que o Uno",
                    "D) O Uno possui Wi-Fi integrado",
                    "E) O Mega não possui portas analógicas"
                ],
                "correta": "A"
            },
            {
                "questao": "Qual modelo de Arduino é mais indicado para projetos compactos?",
                "alternativas": [
                    "A) Arduino Mega",
                    "B) Arduino Due",
                    "C) Arduino Nano",
                    "D) Arduino Uno",
                    "E) Arduino Leonardo"
                ],
                "correta": "C"
            },
            {
                "questao": "Qual componente é considerado o 'cérebro' do Arduino?",
                "alternativas": [
                    "A) O cristal oscilador",
                    "B) O microcontrolador",
                    "C) O conector USB",
                    "D) O regulador de tensão",
                    "E) O botão de reset"
                ],
                "correta": "B"
            },
            {
                "questao": "O pino 'GND' em uma placa Arduino serve para:",
                "alternativas": [
                    "A) Fornecer tensão positiva",
                    "B) Regular corrente",
                    "C) Conectar ao terra (referência elétrica)",
                    "D) Enviar dados seriais",
                    "E) Controlar PWM"
                ],
                "correta": "C"
            },
            {
                "questao": "Qual pino é usado para entradas analógicas no Arduino Uno?",
                "alternativas": [
                    "A) 0–13",
                    "B) A0–A5",
                    "C) 2–7",
                    "D) 8–13",
                    "E) 14–19"
                ],
                "correta": "B"
            },
            {
                "questao": "O que significa PWM nos pinos digitais do Arduino?",
                "alternativas": [
                    "A) Permitir leituras analógicas",
                    "B) Controlar tensão constante",
                    "C) Simular sinais analógicos via modulação de pulso",
                    "D) Gerar sinais seriais",
                    "E) Limitar corrente de entrada"
                ],
                "correta": "C"
            },
            {
                "questao": "Qual função do Arduino é executada apenas uma vez ao iniciar o programa?",
                "alternativas": [
                    "A) loop()",
                    "B) setup()",
                    "C) start()",
                    "D) begin()",
                    "E) main()"
                ],
                "correta": "B"
            },
            {
                "questao": "O comando 'digitalRead(pino)' serve para:",
                "alternativas": [
                    "A) Ler um valor analógico",
                    "B) Definir um pino como saída",
                    "C) Ler se um pino digital está em nível alto ou baixo",
                    "D) Enviar dados pela porta serial",
                    "E) Ligar o LED interno"
                ],
                "correta": "C"
            },
            {
             #   "questao": "Qual biblioteca é necessária para usar comunicação I2C?",
             #   "alternativas": [
              #      "A) SPI.h",
               #     "B) Servo.h",
                #    "C) Wire.h",
                 #   "D) WiFi.h",
                  #  "E) Serial.h"
               # ],
                #"correta": "C"
            },
            {
                "questao": "Qual função inicializa a comunicação I2C?",
                "alternativas": [
                    "A) Wire.begin()",
                    "B) I2C.start()",
                    "C) Serial.begin()",
                    "D) SPI.begin()",
                    "E) i2c.init()"
                ],
                "correta": "A"
            },
            {
           #     "questao": "Qual dispositivo é um exemplo de atuador?",
          #      "alternativas": [
           #         "A) Sensor de temperatura",
            #        "B) Sensor de luz LDR",
             #       "C) Servo motor",
              #      "D) Sensor ultrassônico",
               #     "E) Módulo Wi-Fi"
                #],
                #"correta": "C"
            },
            {
            #    "questao": "Qual é a função de um shield Ethernet?",
            #    "alternativas": [
             #       "A) Controlar motores",
              #      "B) Conectar o Arduino à internet por cabo",
               #     "C) Medir temperatura ambiente",
                #    "D) Armazenar dados em cartão SD",
                 #   "E) Aumentar a potência elétrica da placa"
               # ],
                #"correta": "B"
            },
            {
                "questao": "Qual destes modos de comunicação permite conectar o Arduino ao computador?",
                "alternativas": [
                    "A) SPI",
                    "B) Bluetooth",
                    "C) Serial (USB)",
                    "D) Wi-Fi",
                    "E) I2C"
                ],
                "correta": "C"
            },
            {
                "questao": "Qual destes é um exemplo de boa prática ao ligar componentes ao Arduino?",
                "alternativas": [
                    "A) Ligar LEDs sem resistor",
                    "B) Usar fios desencapados para conexão direta",
                    "C) Verificar a polaridade e tensão antes de ligar",
                    "D) Alimentar o Arduino com 12V direto no pino 5V",
                    "E) Soldar os componentes direto na placa"
                ],
                "correta": "C"
            },
            {
                "questao": "Qual é o risco de conectar sensores de 5V em placas de 3.3V sem adaptação?",
                "alternativas": [
                    "A) A leitura ficará imprecisa",
                    "B) O sensor pode funcionar em baixa tensão",
                    "C) Pode danificar a placa controladora",
                    "D) Nenhum, é compatível automaticamente",
                    "E) O sensor não enviará dados"
                ],
                "correta": "C"
            },
            {
                "questao": "Um exemplo comum de aplicação prática do Arduino é:",
                "alternativas": [
                    "A) Controle de temperatura com ventilador automático",
                    "B) Renderização de vídeos 3D",
                    "C) Compilação de código em servidores",
                    "D) Criação de sistemas operacionais",
                    "E) Desenvolvimento de jogos AAA"
                ],
                "correta": "A"
            },
            {
                "questao": "Qual comando é usado para limpar o monitor serial?",
                "alternativas": [
                    "A) Serial.clear()",
                    "B) Serial.flush()",
                    "C) Serial.reset()",
                    "D) Serial.clean()",
                    "E) Serial.stop()"
                ],
                "correta": "B"
            },
            {
                "questao": "Qual destes sensores é usado para detectar luminosidade?",
                "alternativas": [
                    "A) DHT11",
                    "B) LDR",
                    "C) HC-SR04",
                    "D) MQ-7",
                    "E) DS18B20"
                ],
                "correta": "B"
            }
        ]
      
while True:
    print("\n============================")
    print("        QUIZ ARDUINO        ")
    print("============================")
    print("[1] ▶ Iniciar Quiz")
    print("[2] ▶ Regras")
    print("[3] ▶ Informações")
    print("[4] ▶ Sair")
    print("============================")

    opcao = input("Selecione uma opção: ")
    
    if opcao == "1":
        print("\nIniciando Quiz...")
        perguntas_sorteadas = Sortear_perguntas(perguntas, 20)
        pontuacao = 0
        
        for i, pergunta in enumerate(perguntas_sorteadas, 1):
            print(f"\n--- Pergunta {i}/20 ---")
            Exibir_pergunta(pergunta)
            resposta = input("Resposta: ").upper()
            if Verificar_Resposta(pergunta, resposta):
                pontuacao += 0.5
        
        print(f"\n=== FIM DO QUIZ ===")
        print(f"Sua pontuação final: {pontuacao}/10.0")
        
        R = input("Deseja continuar (S/N)?: ").upper()
        if R != "S":
            break
            
    elif opcao == "2":
        Mostrar_Regras()
        
    elif opcao == "3":
        Mostrar_Informacoes()
        
    elif opcao == "4":
        print("Encerrando programa...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")