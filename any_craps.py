# esta aposta pode ser feita em qualquer fase do jogo 
import random
def any_craps(dado1, dado2):
    aposta_ac = int(input("Qual o valor da sua aposta pro Any Craps ? "))
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado1 + dado2
    if soma == 2 or soma == 3 or soma == 12 :
        #jogador ganha
        fichas = fichas + 7*aposta_ac
        return fichas
    else: 
        #jogador perde
        fichas = fichas - aposta_ac
        return fichas
            
