           print ("Fase Point (2ª fase)")

            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            soma_p = dado1+dado2 #soma point
            
            while soma_p != point and soma_p != 7 and fichas > 0:
                while not jogar_dados:
                    tipo_aposta = input("Qual aposta você deseja realizar? field(f) / any craps (ac) / twelve(t) / jogar os dados (j)")
                    if tipo_aposta=="f":
                        aposta_f += int(input("Qual o valor da sua aposta pro Field?: "))
                    if tipo_aposta=="ac":
                        aposta_ac += int(input("Qual o valor da sua aposta pro Any Craps?: "))
                    if tipo_aposta=="t":
                        aposta_t += int(input("Qual o valor da sua aposta pro Twelve?: "))
                    if tipo_aposta=="j":
                        jogar_dados=True

                #field no point
                if soma_p == 12 and (aposta_f > 0):
                    #jogador ganha o field
                    fichas = fichas + 3 * aposta_f
                    print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if soma_p == 2 and (aposta_f > 0):
                    #jogador ganha o field
                    fichas = fichas + 2 * aposta_f
                    print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if (soma_p == 3 or soma_p == 4 or soma_p == 9 or soma_p == 10 or soma_p == 11) and (aposta_f > 0):
                    #jogador ganha o field
                    fichas = fichas + aposta_f
                    print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if (soma_p == 5 or soma_p == 6 or soma_p == 7 or soma_p == 8) and (aposta_f > 0):
                    #jogador perde tudo, jogo acaba
                    fichas = fichas - fichas
                    print ("A soma dos dados foi = {0}. Você perde tudo! Game over. Fichas disponíveis = {1}".format(soma_p,fichas))
                    fichas_suficientes=False
                    break
                
                #twelve no point
                if soma_p == 12 and (aposta_t > 0):
                    #jogador ganha twelve
                    fichas = fichas + 30 * aposta_t
                    print ("Você acertou o Twelve! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if soma_p != 12 and (aposta_t > 0):
                    #jogador perde twelve
                    fichas = fichas - aposta_t
                    print ("A soma dos dados foi = {0}. Você perde o Twelve. Fichas disponíveis = {1}".format(soma_p,fichas))

                #any craps no point
                if (soma_p == 2 or soma_p == 3 or soma_p == 12) and (aposta_ac > 0):
                    #jogador ganha any craps
                    fichas = fichas + 7 * aposta_ac
                    print ("Você acertou o Any Craps! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
                if (soma_p != 2 or soma_p != 3 or soma_p != 12) and (aposta_ac > 0):
                    #jogador perde any craps
                    fichas = fichas - aposta_ac
                    print ("A soma dos dados foi = {0}. Você perde o Any Craps. Fichas disponíveis = {1}".format(soma_p,fichas))
                
                
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
            
            #field 
            if soma_p == 12 and (aposta_f > 0):
                #jogador ganha o field
                fichas = fichas + 3 * aposta_f
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if soma_p == 2 and (aposta_f > 0):
                #jogador ganha o field
                fichas = fichas + 2 * aposta_f
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if (soma_p == 3 or soma_p == 4 or soma_p == 9 or soma_p == 10 or soma_p == 11) and (aposta_f > 0):
                #jogador ganha o field
                fichas = fichas + aposta_f
                print ("Você acertou o Field! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if (soma_p == 5 or soma_p == 6 or soma_p == 7 or soma_p == 8) and (aposta_f > 0):
                #jogador perde tudo, jogo acaba
                fichas = fichas - fichas
                print ("A soma dos dados foi = {0}. Você perde tudo! Game over. Fichas disponíveis = {1}".format(soma_p,fichas))
                fichas_suficientes=False
                break
            
            #twelve
            if soma_p == 12 and (aposta_t > 0):
                #jogador ganha twelve
                fichas = fichas + 30 * aposta_t
                print ("Você acertou o Twelve! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if soma_p != 12 and (aposta_t > 0):
                #jogador perde twelve
                fichas = fichas - aposta_t
                print ("A soma dos dados foi = {0}. Você perde o Twelve. Fichas disponíveis = {1}".format(soma_p,fichas))

            #any craps
            if (soma_p == 2 or soma_p == 3 or soma_p == 12) and (aposta_ac > 0):
                #jogador ganha any craps
                fichas = fichas + 7 * aposta_ac
                print ("Você acertou o Any Craps! Soma dos dados foi = {0}. Fichas disponíveis = {1}".format(soma_p,fichas))
            if (soma_p != 2 or soma_p != 3 or soma_p != 12) and (aposta_ac > 0):
                #jogador perde any craps
                fichas = fichas - aposta_ac
                print ("A soma dos dados foi = {0}. Você perde o Any Craps. Fichas disponíveis = {1}".format(soma_p,fichas))
                
            print ("O point foi acertado, você volta para o Come Out (1ª fase)")
