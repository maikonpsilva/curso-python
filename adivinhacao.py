import random

def jogar():

    print("***********************************")
    print("Bem vindo ao jogo de adivinhação!!!")
    print("***********************************")

    #numero_secreto = round(random.random() * 100) Inutilizado pois dessa forma é necessário arredondar o resultado.
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    #rodada = 1 #Necessário apenas se utilizar o while ao inves de for

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #print(numero_secreto)

    #while(rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        # chute = int(input("Digite o seu numero: "))
        # print("Tentativa", rodada, "de", total_de_tentativas)
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #String interpolation (Interpolação)

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        #rodada = rodada + 1 #Necessário apenas se utilizar o while

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()