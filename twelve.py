# esta aposta pode ser feita em qualquer fase do jogo 
import random
def twelve(dado1, dado2):
    aposta_t = int(input("Qual o valor da sua aposta pro Twelve ? "))
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma_t = dado1 + dado2
    if soma_t == 12:
        #jogador ganha
        fichas = fichas + 30*aposta_t
        return fichas
    else: 
        #jogador perde
        fichas = fichas - aposta_t
        return fichas