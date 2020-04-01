#pode ser feita no COME OUT e no POINT

def pass_line_bet (dado1,dado2):
        aposta_plb= int(input("Qual o valor da sua aposta?: "))
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma_plb = dado1 + dado2
        if soma_plb == 7 or soma_plb == 11:
            #jogador ganha
            fichas = fichas + aposta
            return fichas
            print ("Você acertou! Fichas disponíveis = {0}".format(fichas))
        elif soma_plb == 2 or soma_plb == 3 or soma_plb == 12:
        #jogador perde
            fichas = fichas - aposta
            return fichas
            print ("Você acertou! Fichas disponíveis = {0}".format(fichas))
        else:
            soma_plb=point
            print ("A soma dos dados é {0}, o jogo passa para a fase Point (2ª fase).".format(point))
            
            #jogo muda pra POINT (2ª fase)
        
            def point (dado1,dado2):
                input ("Você deseja realizar mais alguma aposta?: s/n")
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                soma_p = dado1 + dado2
                if soma_p == point:
                    #jogador ganha
                    fichas = fichas + aposta
                    return fichas
                    print ("Você acertou! Fichas disponíveis = {0}".format(fichas))
                elif soma_p == 7:
                    #jogador perde tudo, jogo acaba
                    fichas = fichas - fichas
                    return fichas
                    print ("Você perde tudo! Game over")
                    fichas_suficientes=False
                else: 
                    while soma_p != point and soma_p != 7:
                        dado1 = random.randint(1,6)
                        dado2 = random.randint(1,6)
                        return point (dado1,dado2) 