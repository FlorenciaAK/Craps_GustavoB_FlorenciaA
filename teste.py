fichas = 50 #por exemplo já que a gente decide
fichas_disponíveis = print ("Você possui {0} fichas".format(fichas))
continuar = input("Você deseja continuar ou abandonar o jogo? (escolher entre continuar ou abandonar ou consultar regras: ")
continuar = True
fichas_suficientes = fichas>0 
aposta = int(input("Qual o valor da sua aposta?: "))

import random


print ("Você está jogando")

while continuar and fichas_suficientes:
    if continuar=="continuar":
        continuar=True
        if fichas_suficientes==True:
            point = True
            def pass_line_bet(dado1,dado2):
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                soma = dado1 + dado2
                if soma == 7 or soma == 11:
                    #jogador ganha
                    fichas = fichas + aposta
                    return fichas
                    print ("Você acertou! Fichas disponíveis = {0}".format(fichas))
                elif soma == 2 or soma == 3 or soma == 12:
                    #jogador perde
                    fichas = fichas - aposta
                    return fichas
                    print ("Você acertou! Fichas disponíveis = {0}".format(fichas))
                else:
                    point=soma
                    print ("A soma dos dados é {0}, o jogo passa para a fase Point(2ª fase).".format(point))
                    #jogo muda pra POINT (2ª fase)
                    def point (dado1,dado2):
                        input ("Você deseja realizar mais alguma aposta?: s/n")
                        dado1 = random.randint(1,6)
                        dado2 = random.randint(1,6)
                        soma = dado1 + dado2
                        if soma == point:
                            #jogador ganha
                            fichas = fichas + aposta
                            return fichas
                            print ("Você acertou! Fichas disponíveis = {0}".format(fichas))
                        elif soma == 7:
                            #jogador perde tudo, jogo acaba
                            fichas = fichas - fichas
                            return fichas
                            print ("Você perde tudo! Game over")
                            fichas_suficientes=False
                        else: 
                            while soma!= point and soma != 7:
                                dado1 = random.randint(1,6)
                                dado2 = random.randint(1,6)
                                point (dado1,dado2)

        else:
            fichas_suficientes=False
            break
    else:
        continuar=False
        break