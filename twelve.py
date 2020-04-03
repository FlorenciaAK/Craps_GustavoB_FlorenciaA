# esta aposta pode ser feita em qualquer fase do jogo 

#twelve no come out
        if soma_co == 12 and (aposta_t > 0):
            #jogador ganha twelve
            fichas = fichas + 30 * aposta_t
            print ("Você acertou o Twelve! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        elif soma_co != 12 and (aposta_t > 0):
            #jogador perde twelve
            fichas = fichas - aposta_t
            print ("Você perde o Twelve. A soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))

#twelve no point
            if soma_p == 12 and (aposta_t2 > 0):
                #jogador ganha twelve
                fichas = fichas + 30 * aposta_t2
                print ("Você acertou o Twelve! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            elif soma_p != 12 and (aposta_t2 > 0):
                #jogador perde twelve
                fichas = fichas - aposta_t2
                print ("Você perde o Twelve. A soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))