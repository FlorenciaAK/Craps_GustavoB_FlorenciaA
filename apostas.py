print ("Você está jogando")

while fichas_suficientes==True:
    fichas_disponíveis = print ("Você possui {0} fichas".format(fichas))
    continuar = input("Você deseja continuar ou abandonar o jogo? (escolher entre continuar ou abandonar ou consultar regras: ")
    while continuar == "continuar":
        tipo_aposta = input("Qual aposta voce deseja realizar? pass line bet/field/any craps/twelv/nehuma")
