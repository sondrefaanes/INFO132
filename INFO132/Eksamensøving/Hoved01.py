# Hoved 01
# Bankooppgave
saldo = 500
rentesats = 0.01
# logliste = []


def vis_saldo():
    global saldo
    print(saldo)


def innskudd(b):
    global saldo
    global rentesats
    saldo += b
    if saldo >= 1000000:
        rentesats = 0.02
        print("Gratulerer: Du har bonusrente!")
        print("Ny saldo er nå:", saldo)
    elif saldo <= 1000000:
        print("Ny saldo er nå: ", saldo)


def uttak(c):
    global saldo
    global rentesats
    saldo = saldo - c
    if saldo >= 1000000:
        rentesats = 0.01
        print("Din saldo er nå", saldo, "Du har ordinær rentesats.")
    elif saldo <= 1000000:
        rentesats = 0.02
        print("Din saldo er nå", saldo, ".Du har ordinær bonusrente.")


def renteoppgjør():
    global saldo
    global rentesats
    ny_saldo = saldo * rentesats
    print("Etter oppgjør er din saldo", ny_saldo, "kr.")


def siste_endringer():
    pass


logliste = []


def bank():
    global logliste
    while True:
        print("-------------")
        print("1 - Vis saldo ")
        print("2 - innskudd")
        print("3 - Uttak ")
        print("4 - renteoppgjør")
        print("5 - siste endringer")
        print("0 - avslutt program")
        print("-------------")

        valg = int(input("Hva vil du gjøre? <0 for å avslutte>: "))
        if valg == 1:
            print("Saldo er nå:")
            vis_saldo()
            print("-------------")

        elif valg == 2:
            b = int(input("Gjør et innskudd i int format: "))
            innskudd(b)
            print("-------------")
            logliste += [("+"+str(b))]

        elif valg == 3:
            c = int(input("Hvor mye vil du ta ut: "))
            uttak(c)
            print("-------------")
            logliste += [("-"+str(c))]
        elif valg == 4:
            renteoppgjør()
            print("-------------")
            logliste += ["+"+str(saldo*rentesats)]
        elif valg == 5:
            print("--------------")
            print(logliste[-3])
            print(logliste[-2])
            print(logliste[-1])
            print("--------------")
        elif valg == 0:
            break
        else:
            print("Du har gjort et ugylidig valg, skriv inn int fra 0-5")
            continue


bank()
