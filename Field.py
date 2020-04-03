# esta aposta pode ser feita em qualquer fase do jogo 
#field no point
if soma_p == 12 and (aposta_f2 > 0):
                #jogador ganha o field
                fichas = fichas + 3 * aposta_f2
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            elif soma_p == 2 and (aposta_f2 > 0):
                #jogador ganha o field
                fichas = fichas + 2 * aposta_f2
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            elif (soma_p == 3 or soma_p == 4 or soma_p == 9 or soma_p == 10 or soma_p == 11) and (aposta_f2 > 0):
                #jogador ganha o field
                fichas = fichas + aposta_f2
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            elif (soma_p == 5 or soma_p == 6 or soma_p == 7 or soma_p == 8) and (aposta_f2 > 0):
                #jogador perde tudo, jogo acaba
                fichas = fichas - fichas
                print ("Você perde tudo. Game over. A soma dos dados no Field foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                fichas_suficientes=False
                break
            


#field no come out
        if soma_co == 12 and (aposta_f > 0):
            #jogador ganha o field
            fichas = fichas + 3 * aposta_f 
            print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        elif soma_co == 2 and (aposta_f > 0):
            #jogador ganha o field
            fichas = fichas + 2 * aposta_f
            print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        elif (soma_co == 3 or soma_co == 4 or soma_co == 9 or soma_co == 10 or soma_co == 11) and (aposta_f > 0):
            #jogador ganha o field
            fichas = fichas + aposta_f
            print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        elif (soma_co == 5 or soma_co == 6 or soma_co == 7 or soma_co == 8) and (aposta_f > 0):
            #jogador perde tudo, jogo acaba
            fichas = fichas - fichas
            print ("Você perde tudo. Game over. A soma dos dados no Field foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
            fichas_suficientes=False
            break
        