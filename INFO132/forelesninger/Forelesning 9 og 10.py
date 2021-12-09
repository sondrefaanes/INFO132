#Liste - en sekvens av elementer, kan være string, bool, integer eller en nøstet liste. En nøstet liste er en liste i en annen liste

Liste_eksempel = [1,2,3]
Liste_eksempel2 = ["En","To","Tre"]

#Range - gir en sekvens fra m til n, f eks: range(1,5) vil gi oss 1,2,3,4.
#Kan indeksere og segmentere en liste.

#For å indeksere skriver vi liste[posisjon]
#Segmentere: liste[x:y] 
#Første posisjon i liste er 0, siste er -1
print(Liste_eksempel[0:2])
print(Liste_eksempel2[-1])

#kan bruke * og + for kopiere eller konkatonere.

#Eks:
print(Liste_eksempel*3)
print(Liste_eksempel2+Liste_eksempel)

#For å hente et element fra den nøstede listen må vi først hente den nøstede, så deretter posisjonen på det ømnskede elementet i den nøstede lsiten.

#Eks
Liste_eksempel3 = [1,2,3,[4,"Fem"]]
print(Liste_eksempel3[3][1])

len(Liste_eksempel) 
#Len gir antall elementer i gitt sekvens, trenger ikke være en liste!
cheeses = ["Cheddar","Edam","Norwegia"]

#Tabeller (matriser)
tabell =[[1,2,3],[4,5,6,],[7,8,9],[10,11,12]]
print(tabell,sep="\n")
print(*Liste_eksempel,sep="\n")

for element in tabell:
    print(element, sep=" ")

#liste.append(element) legger til et gitt element i slutten av en liste

#liste1.extend(liste2) legger til liste 2 på slutten av liste 1. Listen blir utvidet.
#Elemtentet i extend blir uendret. elementet før .extend endres

Liste_eksempel.reverse()
#snur hele listen.

Liste_eksempel2.sort()
#sorter unicode

# sorted(Liste_eksempel3)

#Med * eller + kan man returnere en ny versjon av listen, men den endrer ikke den oprinnelige lsiten.
navneliste = ["Ola","Jens","Peder"]
def snu(liste):
    resultat = []
    for element in liste:
        resultat = [element] + resultat
    return resultat
print(snu(navneliste))

#DEL 2 - Dictionaries
#Fortegnelser

#Brukes for å assosiere data med hverandre. F eks. Fag og eksamenskarakter.
#Bruker Key og value. KEY: VALUE
#En dictionary er en samling av par bestående av key og value.
# Feks
emne_og_karakter = {
    "INFO132" : "A",
    "INFO100" : "B",
    "INFO125" : "D",
    "INFO104" :"",
}
#Dictionary som holder fag og deres respektive karakter
#Dictionaries inneholder som oftest samme verdier, feks bare float, bare bool, bare int eller bare string.
# print(emne_og_karakter["INFO100"])

#Kan sette verdi for udefinert key, men kan ikke hente ut verdi for udefinert nøkkel.
#Kan endre verdi for definert nøkkel, dermed overskrives, ikke duplikat med ny verdi.

for nøkkel in emne_og_karakter:
    print(nøkkel,":", emne_og_karakter[nøkkel])

#"==" sjekker ekvivialens
# "is" sjekker objektilikhet
#!= sjekker ikke verdlikhet
#"not is" sjekker at to variabler ikke har objektlikhet

#Ingen klar rekkefølge i dictionary
#Nøklene er ikke posisjoner
#På norsk er dictionary "Fortegnelse"
#Slå opp i fortegnelse ved å bruke fortegnelse[key]
#Eks:
# emne_og_karakter[1]
#Kan ikke slå opp på verdier, kun nøkler/keys. Får ellers KeyError
#Tilordne verdi til en key ved:
# emne_og_karakter[3] = "C"

liste = [1,1,2,4,3,4,5]
uten_duplikat = set(liste)
print(uten_duplikat)
type(set)

#Tupler
#Uforanderlige lister
#Skrevet med ("","")
tuppel = tuple([1,2,3,4,5])
print(tuppel)
id(tuppel)

#Indeksere og ta utsnitt
#In-tester
#Løkke
# tuppel.count()

#Paranteser
#Sekvens av verdier skilt av komma
#Parantesene er ofte ikke nødvendige

#Konvertering og sortering
tuppel1 = (1,2,3,4,5,6,7,8)
tuppel2 = (1,2,3,4,5,6,7,8)
tuppel1 == tuppel2

#tuple(sekvens) - konverterer til tuppel
#sortet(tuppel) #returnerer en sortert liste
#sort funker ikke fordi den forandrer tupplet, men sorted gir en ny sortert temporary tuppel

from statistics import mean


emner = ["INFO100", "INFO132", "INFO125","ECON100","ECON211"]
karakterer = {
    "INFO100" : "B",
    "INFO125" : "C",
}

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

        

# def last_data():
#     pass
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
            else:    
                print("Avslutter")
                break


        elif valg == 6:
            lagre()
        else:
            print("Ugyldig valg.")
try:
    karakterer = eval(open('karakterfil.txt').read())
except:
    karakterer = {}
    print('Lagre for å opprette filene')

try:
    emneliste = eval(open('emnefil.txt').read())
except:
    emneliste = []
start()