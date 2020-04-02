fichas = 50 #por exemplo já que a gente decide

jogar_dados = False

aposta_plb = 0
aposta_f = 0
aposta_ac = 0
aposta_ac = 0
aposta_t = 0

fichas_suficientes = (fichas>0) 

import random
print ("Você está jogando")

while fichas_suficientes==True:
    fichas_disponíveis = print ("Você possui {0} fichas".format(fichas))
    continuar = input("Você deseja continuar ou abandonar o jogo? (escolher entre continuar (c) ou abandonar (a): ")
    while continuar == "c":
        print ("Fase Come Out (1ª fase)")
        while not jogar_dados:
            tipo_aposta = input("Qual aposta você deseja realizar? pass line bet (plb) / field(f) / any craps (ac) / twelve(t) / jogar os dados (j): ")
            if tipo_aposta=="plb":
                aposta_plb= aposta_plb + int(input("Qual o valor da sua aposta pro Pass Line Bet?: "))
            if tipo_aposta=="f":
                aposta_f= aposta_f + int(input("Qual o valor da sua aposta pro Field?: "))
            if tipo_aposta=="ac":
                aposta_ac= aposta_ac + int(input("Qual o valor da sua aposta pro Any Craps?: "))
            if tipo_aposta=="t":
                aposta_t= aposta_t + int(input("Qual o valor da sua aposta pro Twelve?: "))
            if tipo_aposta=="j":
                jogar_dados=True

        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma_co = dado1+dado2 #soma come out
        
        #Pass Line Bet
        if soma_co == 7 or soma_co == 11 and aposta_plb > 0:
            #jogador ganha pass line bet
            fichas = fichas + aposta_plb
            print ("Você acertou o Pass Line Bet! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co,fichas))
        if soma_co == 2 or soma_co == 3 or soma_co == 12 and aposta_plb > 0:
            #jogador perde pass line bet
            fichas = fichas - aposta_plb
            print ("Você perdeu o Pas Line Bet! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_co, fichas))
        if soma_co == 4 or soma_co == 5 or soma_co == 6 or soma_co == 8 or soma_co == 9 or soma_co == 10 and aposta_plb > 0:
            point = soma_co 
            print ("A soma dos dados é {0}, o jogo passa para a fase Point (2ª fase) e a sua aposta permanece. Fichas disponíveis = {1}".format(point,fichas))
            
            print ("Fase Point (2ª fase")

            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            soma_p = dado1+dado2 #soma point
            
            while soma_p != point and soma_p != 7:
                while not jogar_dados:
                    tipo_aposta = input("Qual aposta você deseja realizar? field(f) / any craps (ac) / twelve(t) / jogar os dados (j)")
                    if tipo_aposta=="f":
                        aposta_f= aposta_f + int(input("Qual o valor da sua aposta pro Field?: "))
                    if tipo_aposta=="ac":
                        aposta_ac= aposta_ac + int(input("Qual o valor da sua aposta pro Any Craps?: "))
                    if tipo_aposta=="t":
                        aposta_t= aposta_t + int(input("Qual o valor da sua aposta pro Twelve?: "))
                    if tipo_aposta=="j":
                        jogar_dados=True
                #field
                if soma_p == 12 and aposta_f > 0:
                    #jogador ganha o field
                    fichas = fichas + 3 * aposta_f
                    print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if soma_p == 2 and aposta_f > 0:
                    #jogador ganha o field
                    fichas = fichas + 2 * aposta_f
                    print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if soma_p == 3 or soma_p == 4 or soma_p == 9 or soma_p == 10 or soma_p == 11 and aposta_f > 0:
                    #jogador ganha o field
                    fichas = fichas + aposta_f
                    print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if soma_p == 5 or soma_p == 6 or soma_p == 7 or soma_p == 8 and aposta_f > 0:
                    #jogador perde tudo, jogo acaba
                    fichas = fichas - fichas
                    print ("A soma dos dados foi = {0}. Você perde tudo! Game over".format(soma_p))
                    fichas_suficientes=False
                
                #twelve
                if soma_p == 12 and aposta_t > 0:
                    #jogador ganha twelve
                    fichas = fichas + 30 * aposta_t
                    print ("Você acertou o Twelve! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if soma_p != 12 and aposta_t > 0:
                    #jogador perde twelve
                    fichas = fichas - aposta_t
                    print ("A soma dos dados foi = {0}. Você perde o Twelve.Fichas disponíveis = {1}".format(soma_p,fichas))

                #any craps
                if soma_p == 2 or soma_p == 3 or soma_p == 12 and aposta_ac > 0:
                    #jogador ganha any craps
                    fichas = fichas + 7 * aposta_ac
                    print ("Você acertou o Any Craps! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if soma_p != 2 or soma_p != 3 or soma_p != 12 and aposta_ac > 0:
                    #jogador perde any craps
                    fichas = fichas - aposta_ac
                    print ("A soma dos dados foi = {0}. Você perde o Any Craps.Fichas disponíveis = {1}".format(soma_p,fichas))
                
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
                    print ("Você perde tudo! Soma dos dados foi = {0}. Game over.Fichas disponíveis = {1}".format (soma_p, fichas))
                    fichas_suficientes=False
            
            #field
            if soma_p == 12 and aposta_f > 0:
                #jogador ganha o field
                fichas = fichas + 3 * aposta_f
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if soma_p == 2 and aposta_f > 0:
                #jogador ganha o field
                fichas = fichas + 2 * aposta_f
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if soma_p == 3 or soma_p == 4 or soma_p == 9 or soma_p == 10 or soma_p == 11 and aposta_f > 0:
                #jogador ganha o field
                fichas = fichas + aposta_f
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if soma_p == 5 or soma_p == 6 or soma_p == 7 or soma_p == 8 and aposta_f > 0:
                #jogador perde tudo, jogo acaba
                fichas = fichas - fichas
                print ("A soma dos dados foi = {0}. Você perde tudo! Game over".format(soma_p))
                fichas_suficientes=False
            
            #twelve
            if soma_p == 12 and aposta_t > 0:
                #jogador ganha twelve
                fichas = fichas + 30 * aposta_t
                print ("Você acertou o Twelve! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if soma_p != 12 and aposta_t > 0:
                #jogador perde twelve
                fichas = fichas - aposta_t
                print ("A soma dos dados foi = {0}. Você perde o Twelve. Fichas disponíveis = {1}".format(soma_p,fichas))

            #any craps
            if soma_p == 2 or soma_p == 3 or soma_p == 12 and aposta_ac > 0:
                #jogador ganha any craps
                fichas = fichas + 7 * aposta_ac
                print ("Você acertou o Any Craps! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if soma_p != 2 or soma_p != 3 or soma_p != 12 and aposta_ac >0:
                #jogador perde any craps
                fichas = fichas - aposta_ac
                print ("A soma dos dados foi = {0}. Você perde o Any Craps.Fichas disponíveis = {1}".format(soma_p,fichas))
                
            print("O point foi acertado, você volta para o Come Out (1ª fase)")

        #field
        if soma_p == 12 and aposta_f > 0:
            #jogador ganha o field
            fichas = fichas + 3 * aposta_f
            print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
        if soma_p == 2 and aposta_f > 0:
            #jogador ganha o field
            fichas = fichas + 2 * aposta_f
            print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
        if soma_p == 3 or soma_p == 4 or soma_p == 9 or soma_p == 10 or soma_p == 11 and aposta_f > 0:
            #jogador ganha o field
            fichas = fichas + aposta_f
            print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
        if soma_p == 5 or soma_p == 6 or soma_p == 7 or soma_p == 8 and aposta_f > 0:
            #jogador perde tudo, jogo acaba
            fichas = fichas - fichas
            print ("A soma dos dados foi = {0}. Você perde tudo! Game over".format(soma_p))
            fichas_suficientes=False
        
        #twelve
        if soma_p == 12 and aposta_t > 0:
            #jogador ganha twelve
            fichas = fichas + 30 * aposta_t
            print ("Você acertou o Twelve! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
        if soma_p != 12 and aposta_t > 0:
            #jogador perde twelve
            fichas = fichas - aposta_t
            print ("A soma dos dados foi = {0}. Você perde o Twelve.Fichas disponíveis = {1}".format(soma_p,fichas))

        #any craps
        if soma_p == 2 or soma_p == 3 or soma_p == 12 and aposta_ac > 0:
            #jogador ganha any craps
            fichas = fichas + 7 * aposta_ac
            print ("Você acertou o Any Craps! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
        if soma_p != 2 or soma_p != 3 or soma_p != 12 and aposta_ac >0:
            #jogador perde any craps
            fichas = fichas - aposta_ac
            print ("A soma dos dados foi = {0}. Você perde o Any Craps.Fichas disponíveis = {1}".format(soma_p,fichas))


print ("Obrigado por jogar, volte sempre!")
