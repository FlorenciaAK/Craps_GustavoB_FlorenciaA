#pode ser feita no COME OUT e no POINT

     print ("Fase Come Out (1ª fase)")

        #pode fazer outras apostas

         dado1 = random.randint(1,6)
         dado2 = random.randint(1,6)
        soma_co = dado1+dado2 #soma come out
        
        #Pass Line Bet
        if (soma_co == 7 or soma_co == 11) and (aposta_plb > 0):
            #jogador ganha pass line bet
            fichas = fichas + aposta_plb
            print ("Você acertou o Pass Line Bet! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))

        if (soma_co == 2 or soma_co == 3 or soma_co == 12) and (aposta_plb > 0):
            #jogador perde pass line bet
            fichas = fichas - aposta_plb
            print ("Você perdeu o Pas Line Bet! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co, fichas))

        if (soma_co == 4 or soma_co == 5 or soma_co == 6 or soma_co == 8 or soma_co == 9 or soma_co == 10) and (aposta_plb > 0):
            point = soma_co 
            print ("A soma dos dados é {0}, o jogo passa para a fase Point (2ª fase) e a sua aposta permanece p/ o PSL. Fichas disponíveis = {1}".format(point,fichas))
            
            print ("Fase Point (2ª fase)")
            while soma_p != point and soma_p != 7 and fichas > 0:
                #
                #Fica no loop do point ate acertar
                #pode fazer outras apostas 
                #
                print("O point não foi acertado, você permanece no Point (2ª fase)")

            #if soma_p == point ou soma_p == 7

            #point 
            if soma_p == point:
                #jogador ganha
                fichas = fichas + aposta_plb
                print ("Você acertou o Point! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format (soma_p, fichas))
            if soma_p == 7:
                #jogador perde tudo, jogo acaba
                fichas = fichas - fichas
                print ("Você perde tudo! Soma dos dados foi = {0}. Game over. Fichas disponíveis = {1}".format (soma_p, fichas))
                fichas_suficientes=False
                break        
            print ("O point foi acertado, você volta para o Come Out (1ª fase)")