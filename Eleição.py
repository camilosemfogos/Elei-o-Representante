print("ELEIÇÂO DO REPRESENTANTE")
A = 0
ANA = 0
BRUNO = 0
CARLOS = 0
BRANCO = 0
while A == 0:
    print("1 - Votar em Ana")
    print("2 - Votar em Bruno")
    print("3 - Votar em Carlos")
    print("4 - Votar em Branco")
    print("5 - Exibir resultado parcial")
    print("6 - Finalizar eleição")
    B = int(input("Escolha uma opção :"))
    if B ==1:
        print("Voto em Ana Registrado")
        ANA += 1
    elif B==2:
        print("Voto em Bruno Registrado")
        BRUNO += 1
    elif B==3:
        print("Voto em Carlos Registrado")
        CARLOS += 1
    elif B==4:
        print("Voto em Branco Registrado")
        BRANCO += 1
    elif B==5:
        print("Ana está com {} votos".format(ANA))
        print("Bruno está com {} votos".format(BRUNO))
        print("Carlos está com {} votos".format(CARLOS))
        print(" A eleição está com {} votos em branco".format(BRANCO))
    elif B==6:
        print("Finalizar")
        A = 1
    else:
        print("Voto invalido (Adicionado ao Branco)")
        BRANCO += 1
if ANA > BRUNO and ANA > CARLOS:
        print("Ana venceu as eleições")
elif BRUNO > ANA and BRUNO > CARLOS:
        print("Bruno venceu as eleições")
elif CARLOS > ANA and CARLOS > BRUNO:
        print("Carlos venceu as eleições")
elif ANA == CARLOS and ANA == BRUNO and BRUNO == CARLOS:
        print("A eleição empatou de forma tripla")
else:
        print("A eleição terminou empatada")
        if ANA > BRUNO and ANA > CARLOS:
            print("Ana venceu as eleições")
        elif BRUNO > ANA and BRUNO > CARLOS:
            print("Bruno venceu as eleições")
        elif CARLOS > ANA and CARLOS > BRUNO:
            print("Carlos venceu as eleições")
print("Ana terminou com {} votos".format(ANA))
print("Bruno terminou com {} votos".format(BRUNO))
print("Carlos terminou com {} votos".format(CARLOS))









