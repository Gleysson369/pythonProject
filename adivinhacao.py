print("#################################")
print("Bem vindo no jogo de Adivinhação!")
print("#################################")

numero_secreto = 43
totalDeTentativas = 3

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
        print("Você acertou")
        break
    else:
        if(errouParaCima):
            print("Você errou! seu chute foi maior do que numero secreto.")
        elif(errouParaBaixo):
            print("Você errou! seu chute foi menor que o numero secreto.")


    print("Fim do Jogo")

