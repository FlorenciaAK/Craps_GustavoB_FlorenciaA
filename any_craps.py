# esta aposta pode ser feita em qualquer fase do jogo 

#any craps no come out
        if (soma_co == 2 or soma_co == 3 or soma_co == 12) and (aposta_ac > 0):
            #jogador ganha any craps
            fichas = fichas + 7 * aposta_ac
            print ("Você acertou o Any Craps! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        elif (soma_co != 2 or soma_co != 3 or soma_co != 12) and (aposta_ac > 0):
            #jogador perde any craps
            fichas = fichas - aposta_ac
            print ("Você perde o Any Craps. A soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))

#any craps no point
            if (soma_p == 2 or soma_p == 3 or soma_p == 12) and (aposta_ac2 > 0):
                #jogador ganha any craps
                fichas = fichas + 7 * aposta_ac2
                print ("Você acertou o Any Craps! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            elif (soma_p != 2 or soma_p != 3 or soma_p != 12) and (aposta_ac2 > 0):
                #jogador perde any craps
                fichas = fichas - aposta_ac2
                print ("Você perde o Any Craps. A soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))