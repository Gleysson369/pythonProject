import random

def jogar():

    print("#################################")
    print("Bem vindo no jogo de Adivinhação!")
    print("#################################")

    numero_secreto = random.randrange(1,101)
    totalDeTentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível"))

    if(nivel == 1):
        totalDeTentativas = 20
    elif(nivel == 2):
        totalDeTentativas = 10
    else:
        totalDeTentativas = 5

    for rodada in range(1,totalDeTentativas + 1):
        print("Tentativas {} de {}".format(rodada,totalDeTentativas))
        chute_str = input("Digite o seu numero entre 1 e 100: ")
        print("Você digitou" , chute_str)
        chute = int(chute_str)

        if( chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        errouParaCima = chute > numero_secreto
        errouParaBaixo = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(errouParaCima):
                print("Você errou! seu chute foi maior do que numero secreto.")
            elif(errouParaBaixo):
                print("Você errou! seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


        print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()