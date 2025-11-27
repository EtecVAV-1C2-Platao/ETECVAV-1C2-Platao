
import random #biblioteca para sortear as questões

def Mostrar_Regras():
    print("============================================================================")
    print("||           REGRAS                                                       ||")
    print("||========================================================================||")
    print("||1. O quiz será composto por perguntas de múltipla escolha sobre Arduino.||")
    print("||2. Cada questão é de múltipla escolha, tendo apenas uma correta (A-E).  ||")
    print("||3. Cada questão vale 0,5 pontos.                                        ||")
    print("||4. A nota máxima é 10,0 pontos.                                         ||")
    print("||5. É proibido consultar material externo durante o quiz.                ||")
    print("============================================================================")
   

def Mostrar_Informacoes():
    print("=====================================================================================")
    print("||           INFORMAÇÕES                                                           ||")
    print("||=================================================================================||")
    print("||Este é um Quiz com o tema centrado no Arduino, abrangendo os seguintes tópicos:  ||")
    print("|| 1. Histórico e origem do projeto                                                ||")
    print("|| 2. Modelos e famílias de placas (Uno, Mega, Nano, etc.)                         ||")
    print("|| 3. Componentes e arquitetura básica                                             ||")
    print("|| 4. Conexões, portas e sinais (digitais, analógicos, PWM)                        ||")
    print("|| 5. Estrutura de código (setup, loop, funções, bibliotecas)                      ||")
    print("|| 6. Principais comandos e funções da IDE Arduino                                 ||")
    print("|| 7. Sensores, atuadores e shields                                                ||")
    print("|| 8. Comunicações: Serial, I2C, SPI, Bluetooth, Wi-Fi                             ||")
    print("|| 9. Boas práticas e segurança elétrica                                           ||")
    print("|| 10. Casos de uso e aplicações práticas                                          ||")
    print("=====================================================================================")

def embaralhar_alternativas(perguntas):
    for pergunta in perguntas:
        alternativas = pergunta["alternativas"]
        
        # Encontra a resposta correta atual (texto)
        resposta_correta_atual = pergunta["correta"]
        
        # Desmembra alternativas
        itens_alternativas = []
        for alt in alternativas:
            partes = alt.split(") ", 1)
            if len(partes) == 2:
                letra = partes[0]
                texto = partes[1]
                itens_alternativas.append((letra, texto))
        
        # Embaralha as alternativas (mantendo letra e texto juntos)
        random.shuffle(itens_alternativas)
        
        # Reconstrói as alternativas embaralhadas
        alternativas_embaralhadas = []
        for letra, texto in itens_alternativas:
            alternativas_embaralhadas.append(f"{letra}) {texto}")
            
            # Se este texto era o correto, atualiza a letra correta
            if texto == resposta_correta_atual:
                pergunta["correta"] = letra
        
        pergunta["alternativas"] = alternativas_embaralhadas
    
    return perguntas

def Sortear_perguntas(perguntas, quantidade=20):
    return random.sample(perguntas, quantidade)
 

def Exibir_pergunta(pergunta):
    print("\n" + pergunta["questao"])
    for alternativa in pergunta["alternativas"]:
        print(alternativa)


def Verificar_Resposta(pergunta, resposta):
    resposta_usuario = resposta.strip().upper().split()[0] if resposta else ""
    
    if resposta_usuario == pergunta["correta"]:
        print("✅ Acertouuu!\n")
        return True
    else:
        print(f"❌ Errouuu! A resposta correta era: {pergunta['correta']}\n")
        return False


perguntas_embaralhadas = [
    {
        "questao": "Quem foi o principal inventor do Arduino?",
        "alternativas": [
            "A) Bruce Willis", 
            "B) Mark Zuckerberg", 
            "C) William Shakespeare", 
            "D) Massimo Banzi", 
            "E) David Mellis"
        ],
        "correta": "Massimo Banzi"
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
        "correta": "pinMode()"
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
        "correta": "2005"
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
        "correta": "Uma plataforma que possibilita o desenvolvimento de projetos eletrônicos. Em outras palavras, é uma plataforma de prototipagem eletrônica."
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
        "correta": "Integrated Development Environment"
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
        "correta": ".ino"
    },
    {
       "questao": "Quantos pinos digitais o Arduino Mega possui?",
       "alternativas": [
            "A) 54",
            "B) 20",
            "C) 32",
            "D) 14",
            "E) 40",
       ],
        "correta": "54"
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
        "correta": "14"
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
        "correta": "ATmega328P"
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
        "correta": "1 (TX)"
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
        "correta": "Serial.print()"
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
        "correta": "5V"
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
        "correta": "Para o programa por 1 segundo"
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
        "correta": "DHT11"
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
        "correta": "analogRead()"
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
        "correta": "char"
    },
    {
        "questao": "O pino VIN do Arduino Uno serve para: ",
        "alternativas": [
            "A) Comunicação SPI",
            "B) Reset externo",
            "C) Alimentar com 7–12V",
            "D) Ajuste de clock",
            "E) Programação ICSP",
         ],
        "correta": "Alimentar com 7–12V"
    },
    {
        "questao": "Qual é a função do resistor?",
        "alternativas": [
            "A) Armazenar energia",
            "B) Controlar a corrente elétrica",
            "C) Converter energia em calor",
            "D) Aumentar a tensão",
            "E) Medir a resistência"
        ],
        "correta": "Controlar a corrente elétrica"
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
        "correta": "Executa uma vez ao iniciar o programa"
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
        "correta": "Repete o código continuamente"
    }
]

# Aplica o embaralhamento uma vez no início
perguntas_embaralhadas = embaralhar_alternativas(perguntas_embaralhadas)
      
while True:
    print("=============================")
    print("||        QUIZ ARDUINO     ||")
    print("=============================")
    print("|| [1] ▶ Iniciar Quiz      ||")
    print("|| [2] ▶ Regras            ||")
    print("|| [3] ▶ Informações       ||")
    print("|| [4] ▶ Sair              ||")
    print("=============================")

    opcao = input("Selecione uma opção: ")
    
    if opcao == "1":
        print("\nIniciando Quiz...")
        perguntas_sorteadas = Sortear_perguntas(perguntas_embaralhadas, 10)
        pontuacao = 0
        
        for i, pergunta in enumerate(perguntas_sorteadas, 1):
            print("==========================")
            print(f"||--- Pergunta {i}/10 ---||")
            print("==========================")
            Exibir_pergunta(pergunta)
            resposta = input("Resposta: ").upper()

            if Verificar_Resposta(pergunta, resposta):
                pontuacao += 0.5

        print("===============================================")
        print(f"||              FIM DO QUIZ                  ||")
        print("||===========================================||")
        print(f"||Sua pontuação final: {pontuacao}/5.0               ||")
        print("==============================================")
        
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
