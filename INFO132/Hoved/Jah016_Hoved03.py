import random
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
bunker = bunke1, bunke2, bunke3, bunke4, bunke5, bunke6, bunke7, bunke8


def stokk():
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


def lagre():
    with open("spill.txt", "w", encoding="UTF-8") as f:
        for bunke in bunker:
            ferdigstreng = str(bunke)
            for tekst in ["[", "]", "'", ","]:
                ferdigstreng = ferdigstreng.replace(tekst, " ")
            f.write(ferdigstreng+"\n")


def last_inn():
    with open("spill.txt", "r", encoding="UTF-8") as f:
        pass


def spill():
    global spillSeier, spillTap
    kanSpille = True
    while kanSpille:
        print("__________")
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
        print("__________")
        print("Skriv lagre for å lagre. ")
        print("Skriv avslutt for å avslutte")
        inp = input("velg to bunker: ")
        input1 = inp.upper()
        endre = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        if len(input1) == 2:
            a1 = endre[input1[0]]
            a2 = endre[input1[1]]
            fjern_kort(a1, a2)
        elif inp == "lagre":
            lagre()
            kanSpille = False
        elif inp == "avslutt":
            kanSpille = False

        sisteTegn = []
        for bunke in bunker:
            if len(bunke) > 0:
                sisteTegn.append(bunke[-1][-1])
        if len(set(sisteTegn)) == len(sisteTegn):
            kanSpille = False

        bunkesum = 0
        for bunke in bunker:
            if len(bunke) == 0:
                bunkesum += 1
            if bunkesum == 8:
                print("Du vant")
                kanSpille = False


def fjern_kort(a1, a2):
    if a1 != a2 and bunker[a1][-1][-1] == bunker[a2][-1][-1]:
        bunker[a1].pop()
        bunker[a2].pop()
    else:
        print("Ugyldig input")


def meny():
    while True:
        print("-------------------")
        print("1 - Nytt spill")
        print("2 - Last inn spill")
        print("3 - Historikk")
        print("4 - Avslutt")
        print("-------------------")
        valg = int(input("velg: "))

        if valg == 1:
            stokk()
            del_ut()
            spill()
        elif valg == 2:
            last_inn()
            # Lagringsfunksjon funker ikke.
            # kan fikse på egenretting.
        elif valg == 3:
            break
        else:
            print("Ugyldig input, skriv inn et tall fra 1-3.")
            continue


meny()
