# esta aposta pode ser feita em qualquer fase do jogo 
import random
def field(dado1, dado2):
    aposta_field = int(input("Qual o valor da sua aposta pro Field?: "))
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado1 + dado2
    if soma == 12:
        #jogador ganha
        fichas = fichas + 3*aposta_field
        return fichas
    elif soma == 2:
         #jogador ganha
        fichas = fichas + 2*aposta_field
        return fichas
    elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
         #jogador ganha
        fichas = fichas + aposta_field
        return fichas
    else:
        #jogador perde tudo, jogo acaba
        fichas = fichas - fichas
        return fichas
        print ("Você perde tudo! Game over")
        fichas_suficientes=False