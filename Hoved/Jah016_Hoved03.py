import random
# import json
SPAR_SYMBOL = '\u2660'
RUTER_SYMBOL = '\u2666'
KLØVER_SYMBOL = '\u2663'
HJERTER_SYMBOL = '\u2665'
kortstokk = []


bunke1 = []
bunke2 = []
bunke3 = []
bunke4 = []
bunke5 = []
bunke6 = []
bunke7 = []
bunke8 = []

bunker = [bunke1, bunke2, bunke3, bunke4, bunke5, bunke6, bunke7, bunke8]
for kort in range(7, 15):
    kortstokk.append(f'\u2660{kort}')
    kortstokk.append(f'\u2666{kort}')
    kortstokk.append(f'\u2663{kort}')
    kortstokk.append(f'\u2665{kort}')


def del_ut():
    random.shuffle(kortstokk)
    for j in range(4):
        for i in range(8):
            if i == 0:
                bunke1.append(kortstokk.pop())
            elif i == 1:
                bunke2.append(kortstokk.pop())
            elif i == 2:
                bunke3.append(kortstokk.pop())
            elif i == 3:
                bunke4.append(kortstokk.pop())
            elif i == 4:
                bunke5.append(kortstokk.pop())
            elif i == 5:
                bunke6.append(kortstokk.pop())
            elif i == 6:
                bunke7.append(kortstokk.pop())
            elif i == 7:
                bunke8.append(kortstokk.pop())


def tap():
    # Start spillet på nytt med input eller gå til meny med annen input
    pass


def seier():
    print("Du vant")


def lagre():
    # global bunker
    # fil = open("kortspill.json","w")
    # json.dump(bunker, fil)
    # fil.close()
    # Lagre fil
    # Finn ut hvilket format som skal brukes ved lagring av fil for spillet
    pass


def last_inn():
    pass


def spill():
    del_ut()
    while True:
        if len(bunke1) == 0:
            print("A: Bunken er tom")
        else:
            print("A: ", bunke1[-1], "-", (len(bunke1)))

        if len(bunke2) == 0:
            print("B: Bunken er tom")
        else:
            print("B: ", bunke2[-1], "-", (len(bunke2)))

        if len(bunke3) == 0:
            print("C: Bunken er tom")
        else:
            print("C: ", bunke3[-1], "-", (len(bunke3)))

        if len(bunke4) == 0:
            print("D: Bunken er tom")
        else:
            print("D: ", bunke4[-1], "-", (len(bunke4)))

        if len(bunke5) == 0:
            print("E: Bunken er tom")
        else:
            print("E: ", bunke5[-1], "-", (len(bunke5)))

        if len(bunke6) == 0:
            print("F: Bunken er tom")
        else:
            print("F: ", bunke6[-1], "-", (len(bunke6)))

        if len(bunke7) == 0:
            print("G: Bunken er tom")
        else:
            print("G: ", bunke7[-1], "-", (len(bunke7)))

        if len(bunke8) == 0:
            print("H: Bunken er tom")
        else:
            print("H: ", bunke8[-1], "-", (len(bunke8)))

        bunkesum = 0
        for bunke in bunker:
            if len(bunke) == 0:
                bunkesum += 1
            if bunkesum == 8:
                seier()
                
        velg_kort()


def velg_kort():

    inp = input("velg to bunker: ")
    input1 = inp.upper()
    endre = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    if len(input1) == 2:
        a1 = endre[input1[0]]
        a2 = endre[input1[1]]
        fjern_kort(a1, a2)
    elif input1 == "lagre":
        lagre()
    elif len(input1) == "avslutt":
        pass
    if input1 == "lagre":
        lagre()


def fjern_kort(a1, a2):
    if a1 != a2:
        bunker[a1].pop()
        bunker[a2].pop()


def meny():
    while True:
        print("-------------------")
        print("1 - Start spill")
        print("2 - Last inn spill")
        print("3 - Avslutt")
        print("-------------------")

        valg = int(input("velg: "))

        if valg == 1:
            valg2 = int(
                input("trykk 1 for å starte nytt spill, 2 for å laste inn gammelt spill: "))
            if valg2 == 1:
                # while True:
                spill()

            elif valg2 == 2:
                last_inn()
                # Laster inn forrige spill.
            else:
                print("Ugyldig valg")
                pass
        elif valg == 2:
            last_inn()
        elif valg == 3:
            break
        else:
            print("Ugyldig input, skriv inn et tall fra 1-3.")
            continue


meny()

# Spørsmål:
# Hvordan fikse loop så jeg kan ha break i en funksjon som går for en while true som ikke er i funksjonen
# Hvordan spille når bunker er tomme
# Hvilken "Approach" skal jeg ha til lagring
