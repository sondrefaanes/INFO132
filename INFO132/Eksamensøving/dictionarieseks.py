

karakterer = {}
emneliste = ["ECON100", "ECON125", "INFO263", "INFO284"]

Info = []
Econ = []
Mat = []


def settkarakter(fag, karakter):
    if karakter is not None:
        karakterer.update({fag: karakter})
        for element in emneliste:
            if element == fag:
                emneliste.remove(element)
    elif karakter is None and fag in emneliste:
        karakterer.pop(str(fag))


def lagre():
    with open("karakterer.txt", "w") as f:
        f.write(str(karakterer))
    with open("emnefil.txt", "w") as g:
        g.write(str(emneliste))


# def snitt(studieretning):
#     karaktererINFO = []
#     karaktererECO = []
#     karaktererMAT = []
#     global karakterer
#     alleKarakterer = karakterer.keys()
#     if studieretning.lower() == "info" or "informasjonsvitenskap":
#         for i in karakterer:
#             if i[0:3] == "INF":
#                 karaktererINFO.append(i)

# snitt()


def meny():
    aktiv = True
    while aktiv == True:
        print("Karakterverktøy")
        print("---------------")
        print("1 - Emneliste")
        print("2 - Legg til emne")
        print("3 - Sett karakter")
        print("4 - snittkalkulator")
        print("5 - Avslutt")
        print("6 - Lagre")
        print("---------------")
        inp = int(input("Velg handling: "))
        if inp == 1:
            retning = input("retning: ")
            # nivå = input("Nivå: ")
            if retning == "":
                print("Emner: ")
                print(*emneliste, sep="\n")
                for key, value in karakterer.items():
                    print(key, ":", value)
            if retning.lower() == "info":
                for i in emneliste:
                    if i[0:3] == "INF":
                        Info.append(i)
                print(Info)
            if retning.lower() == "mat":
                for i in emneliste:
                    if i[0:3] == "MAT":
                        Mat.append(i)
                print(Mat)
            if retning.lower() == "econ":
                for i in emneliste:
                    if i[0:3] == "ECO":
                        Econ.append(i)
                print(Econ)
        if inp == 2:
            while True:
                nyttFag = input("Legg til fag:")
                emneliste.append(nyttFag)
                if nyttFag == "":
                    emneliste.pop()
                    print(emneliste)
                    break

        if inp == 3:
            while True:
                print(emneliste)
                emne = input("Emne: ")
                karakter = input("Karakter: ")
                if emne not in karakterer and emne in emneliste:
                    settkarakter(emne, karakter)
                    for x in karakterer.items():
                        print(f'Fag: {x[0]} || Resultat: {x[1]}')
                if emne == "":
                    break

        if inp == 4:
            # studieretning = input("studieretning: ")
            # snitt(studieretning)
            continue

        if inp == 5:
            aktiv = False

        if inp == 6:
            inp = input("Vil du lagre?(ja/nei): ")
            if inp == "ja":
                lagre()
                aktiv = False
            elif inp == "nei":
                continue


try:
    karakterer = eval(open("karakterer.txt").read())
except:
    karakterer = {}
try:
    emner = eval(open("emnefil.txt").read())
except:
    emneliste = []
meny()
