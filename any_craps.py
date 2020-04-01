# esta aposta pode ser feita em qualquer fase do jogo 
import random
def any_craps(dado1, dado2):
    aposta_ac = int(input("Qual o valor da sua aposta pro Any Craps ? "))
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma_ac = dado1 + dado2
    if soma_ac == 2 or soma_ac == 3 or soma_ac == 12 :
        #jogador ganha
        fichas = fichas + 7*aposta_ac
        return fichas
    else: 
        #jogador perde
        fichas = fichas - aposta_ac
        return fichas
            
