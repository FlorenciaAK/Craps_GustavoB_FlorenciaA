#pode ser feita no COME OUT e no POINT

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
                break
            else: 
                while soma!= point and soma != 7:
                    dado1 = random.randint(1,6)
                    dado2 = random.randint(1,6)
                    point (dado1,dado2)

print (pass_line_bet)
