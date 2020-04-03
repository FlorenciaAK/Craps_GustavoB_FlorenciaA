# No inicio do jogo 
while fichas>0:
    fichas_disponíveis = print ("Você possui {0} fichas".format(fichas))
    continuar = input("Você deseja continuar ou abandonar o jogo? (escolher entre continuar (c) ou abandonar (a): ")
    jogar_dados = False
    if continuar == "a":
        break
    else:
        #avisa o comeco da primera fase       
        aposta_plb = 0
        aposta_f = 0
        aposta_ac = 0
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

#Durante o Jogo (loop Point)
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


# dados no come out 
  dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma_co = dado1+dado2 #soma come out

#dados no poit 
  dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma_p = dado1+dado2 #soma point