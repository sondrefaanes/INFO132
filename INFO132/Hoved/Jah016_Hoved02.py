from statistics import mean

emner = []
karakterer = {}

def valg_validator():
    godkjente_valg = ["0","1","2","3","4","5"]
    while True:    
        valg = input("Valg: ")
        if valg in godkjente_valg:
            return valg
        else:
            print("Du har gjort et ugyldig valg")

def sett_karakter(emne, karakter):
    if karakter is not None:
        karakterer.update({emne: karakter})
    elif karakter is None and emne in karakterer:
        karakterer.pop(str(emne))
    else:
        print('Oppdatering feilet!')

def snitt_desimal_kalulator(karakter):
    liste = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 0,
    }
    if karakter in liste:
        return liste[karakter]

def desimal_til_bokstav(snitt):
    if snitt >= 4.5:
        return "A"
    elif 3.5 <= snitt < 4.5:
        return "B"
    elif 2.5 <= snitt < 3.5:
        return "C"
    elif 1.5 <= snitt < 2.5:
        return "D"
    elif 0.5 <= snitt < 1.5:
        return "E"
    else:
        return "F"

def snitt(studie_retning):
    alle_karakterer = karakterer.items()
    if studie_retning.lower() == 'informasjonsvitenskap' or studie_retning.lower() == 'info':
        informasjonsvitenskap = []
        for i in alle_karakterer:
            if (i[0][0:3]) == 'INF':
                informasjonsvitenskap.append(snitt_desimal_kalulator(i[1]))
        gj_snitt = desimal_til_bokstav(round(mean(informasjonsvitenskap), 2))
        return f'\nSnitt for {studie_retning.upper()}: {gj_snitt}'

    if studie_retning.lower() == 'økonomi' or studie_retning.lower() == 'econ':
        økonomi = []
        for i in alle_karakterer:
            if (i[0][0:3]) == 'ECO':
                økonomi.append(snitt_desimal_kalulator(i[1]))
        gj_snitt = desimal_til_bokstav(round(mean(økonomi), 2))
        return f'\nSnitt for {studie_retning.upper()}: {gj_snitt}'

    if studie_retning.lower() == 'geografi' or studie_retning.lower() == 'geo':
        geografi = []
        for i in alle_karakterer:
            if (i[0][0:3]) == 'GEO':
                geografi.append(snitt_desimal_kalulator(i[1]))
        gj_snitt = desimal_til_bokstav(round(mean(geografi), 2))
        return f'\nSnitt for {studie_retning.upper()}: {gj_snitt}'
    else:
        if len(list(karakterer)) > 0:
            totalt_snitt = []
            for i in alle_karakterer:
                totalt_snitt.append(snitt_desimal_kalulator(i[1]))
            gj_snitt = desimal_til_bokstav(round(mean(totalt_snitt), 2))
            return f'\nTotalt snitt: {gj_snitt}'
        else:
            return f'\nDu har ikke lagt inn noen karakterer enda.\n'

emne = []
def emne_valg(fag="", nivå=""):
    if fag.lower() =="informasjonsvitenskap" or fag.lower() == "info":
        for i in emner:
            if i[0:3] == "INF" and i[-3] == nivå:
                emne.append(i)
            elif i[0:3] == "INF" and nivå == "":
                emne.append(i) 
        return emne
    elif fag.lower() =="økonomi" or fag.lower() =="econ":
        for i in emner:
            if i [0:3] == "ECO" and i[-3] == nivå:
                emne.append(i)
            elif i[0:3] == "ECO" and nivå == "":
                emne.append(i) 
        return emne
    elif fag.lower() =="geografi" or fag.lower() == "geo":
        for i in emner:
            if i [0:3] == "GEO" and i[-3] == nivå:
                emne.append(i)
            elif i[0:3] == "GEO" and nivå == "":
                emne.append(i) 
        return emne
def lagre():
    global karakterer
    global emner
    with open("data.txt", "w") as data:
        data.seek(0)
        data.truncate(0)
        data.write(str(karakterer))

    with open('emnefil.txt', 'w') as file:
        file.seek(0)
        file.truncate(0)
        file.write(str(emner))

def start():
    while True:
        global emner
        global karakterer
        print("--------------------")
        print("1 Emneliste")
        print("2 Legg til emne")
        print("3 Sett karakter")
        print("4 Karaktersnitt")
        print("5 Avslutt")
        print("6 Lagre")
        print("--------------------")

        valg = int(input("Velg handling (0 for meny)> "))
        if valg == 0:
            continue

        elif valg == 1:
            fag = input('Fag: ')
            nivå = input('Nivå: ')
            presentasjon_av_emner = emne_valg(fag, nivå)
            if presentasjon_av_emner is not None:
                print(f'\nRegistrerte emner ({len(presentasjon_av_emner)} av {len(emner)}):')
                for i in presentasjon_av_emner:
                    print(f'--{i}')
            elif presentasjon_av_emner is None:
                for element in emner:
                    if element in karakterer.keys():
                        print(element,":", karakterer[element]) 
                else:
                    print(element)
            else:
                print('Du har tastet inn ugyldig informasjon. \nFagkode eller nivå kan være feil')
    
        elif valg == 2:
            while True:
                nytt_emne = input("Legg til emne: ")
                emner.append(nytt_emne)
                if nytt_emne == "":
                    break

        elif valg == 3:
            while True:
                nyttemne = input("Emne: \n")
                nykarakter  =input("Karakter: \n")
                
                if nyttemne is not None and nyttemne in emner:
                        sett_karakter(nyttemne, nykarakter)
                        for x in karakterer.items():
                            print(f'Fag: {x[0]} || Resultat: {x[1]}')
                        break
                else:
                    print('Faget finnes ikke i faglisten.')
                    avslutt_loop = input('Skriv 0 for å gå til menyen eller (ENTER) for å prøve igjen. \n')
                    if avslutt_loop == '0':
                        break

        elif valg == 4:
            print(snitt(input("Retning: ")))

        elif valg == 5:
            avslutt = input("Skriv noe for å lagre: ")
            if avslutt != "":
                lagre()
                print("Lagrer... Avslutter.")
                break
            else:    
                print("Avslutter")
                break

        elif valg == 6:
            lagre()
        else:
            print("Ugyldig valg.")
try:
    karakterer = eval(open('data.txt').read())
except:
    karakterer = {}
    print('Lagre for å opprette filene')

try:
    emner = eval(open('emnefil.txt').read())
except:
    emner = []
start()


#TIl hoved3:
# Kilde:
# https://github.com/brusfest/Wish-Solitaire/blob/main/wish_solitaire.py (Hentet 24.November 2021)