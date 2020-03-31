fichas = 50 #por exemplo já que a gente decide
fichas_suficientes = fichas>0 


import random


print ("Você está jogando")

while fichas_suficientes==True:
    fichas_disponíveis = print ("Você possui {0} fichas".format(fichas))
    continuar = input("Você deseja continuar ou abandonar o jogo? (escolher entre continuar ou abandonar ou consultar regras: ")
    while continuar == "continuar":
        tipo_aposta = input("Qual aposta voce deseja realizar? pass line bet/field/any craps/twelv/nehuma")
         def pass_line_bet(dado1,dado2):
            aposta_plb= int(input("Qual o valor da sua aposta?: "))
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
                            point = False
                            fichas = fichas + aposta
                            return fichas
                            print ("Você acertou! Fichas disponíveis = {0}".format(fichas))
                        elif soma == 7:
                            #jogador perde tudo, jogo acaba
                            point = False
                            fichas = fichas - fichas
                            return fichas
                            print ("Você perde tudo! Game over")
                            fichas_suficientes=False
                        else: 
                            while soma!= point and soma != 7:
                                dado1 = random.randint(1,6)
                                dado2 = random.randint(1,6)
                                point (dado1,dado2)

