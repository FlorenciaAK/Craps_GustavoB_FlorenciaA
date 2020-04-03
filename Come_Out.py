print ("{}Fase Come Out (1ª fase){}".format('\033[1;31m','\033[m'))

        aposta_plb = 0
        aposta_f = 0
        aposta_ac = 0
        aposta_t = 0

        while not jogar_dados:
            tipo_aposta = input("Qual aposta você deseja realizar? pass line bet (plb) / field(f) / any craps (ac) / twelve(t) / jogar os dados (j): ")
            if tipo_aposta=="plb":
                aposta_plb += int(input("Qual o valor da sua aposta pro Pass Line Bet?: "))
            if tipo_aposta=="f":
                aposta_f += int(input("Qual o valor da sua aposta pro Field?: "))
            if tipo_aposta=="ac":
                aposta_ac += int(input("Qual o valor da sua aposta pro Any Craps?: "))
            if tipo_aposta=="t":
                aposta_t += int(input("Qual o valor da sua aposta pro Twelve?: "))
            if tipo_aposta=="j":
                jogar_dados=True

        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma_co = dado1+dado2 #soma come out
        
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
        
        #twelve no come out
        if soma_co == 12 and (aposta_t > 0):
            #jogador ganha twelve
            fichas = fichas + 30 * aposta_t
            print ("Você acertou o Twelve! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        elif soma_co != 12 and (aposta_t > 0):
            #jogador perde twelve
            fichas = fichas - aposta_t
            print ("Você perde o Twelve. A soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))

        #any craps no come out
        if (soma_co == 2 or soma_co == 3 or soma_co == 12) and (aposta_ac > 0):
            #jogador ganha any craps
            fichas = fichas + 7 * aposta_ac
            print ("Você acertou o Any Craps! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        elif (soma_co != 2 or soma_co != 3 or soma_co != 12) and (aposta_ac > 0):
            #jogador perde any craps
            fichas = fichas - aposta_ac
            print ("Você perde o Any Craps. A soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        
        #Pass Line Bet
        if (soma_co == 7 or soma_co == 11) and (aposta_plb > 0):
            #jogador ganha pass line bet
            fichas = fichas + aposta_plb
            print ("Você acertou o Pass Line Bet! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))

        elif (soma_co == 2 or soma_co == 3 or soma_co == 12) and (aposta_plb > 0):
            #jogador perde pass line bet
            fichas = fichas - aposta_plb
            print ("Você perdeu o Pas Line Bet! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co, fichas))

        elif (soma_co == 4 or soma_co == 5 or soma_co == 6 or soma_co == 8 or soma_co == 9 or soma_co == 10) and (aposta_plb > 0):
            point = soma_co 
            print ("A soma dos dados é {0}, o jogo passa para a fase Point (2ª fase) e a sua aposta permanece p/ o PSL. Fichas disponíveis = {1}".format(point,fichas))