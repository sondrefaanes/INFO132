emner = ["INFO100", "INFO132", "INFO125","ECON110","GEO130"]
karakterer = {
    "INFO100" : "B",
    "INFO125" : "C",
    "GEO130"  : "D",
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

# def snittkalkulator():
#     for karakter in karakterer:
def sjekk_emner(fag, nivå):
    nivå == fag[-3]
    if fag[0:3]=="INFO" and nivå==1:
       print(emner.starstwith("INF"))
    elif fag[0:3]=="ECON" and nivå==1:
        print(emner.startswith("ECO"))
    elif fag[0:2] == "GEO" and nivå==1:
        print(emner.startswith("GEO"))
    else:
        print("Ugyldig fagområde")
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

        valg = int(input("Velg handling (0 for meny)> "))
        if valg == 0:
            continue
        if valg == 1:
            fag = input("Fagområde: ")
            nivå = input("Nivå: ")
            
            sjekk_emner(fag,nivå)
            # for element in emner:
            #     if element in karakterer.keys():
            #         print(element,":", karakterer[element]) 
            #     else:
            #         print(element)
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
            continue

        elif valg == 5:
            break
start()