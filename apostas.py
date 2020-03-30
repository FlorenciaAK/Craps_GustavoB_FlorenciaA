print ("Você está jogando")

while continuar and fichas_suficientes:
    if continuar=="continuar":
        continuar=True
        if fichas>0:
            fichas_suficientes=True
        else:
            fichas_suficientes=False
    else:
        continuar=False