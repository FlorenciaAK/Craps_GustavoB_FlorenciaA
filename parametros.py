fichas = 50 #por exemplo já que a gente decide
fichas_disponíveis = print ("Você possui {0} fichas".format(fichas))
continuar = ("Você deseja continuar ou abandonar o jogo? (escolher entre continuar ou abandonar ou consultar regras: ")
continuar = True
fichas_suficientes = True #fichas disponíveis > 0 

import random
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)