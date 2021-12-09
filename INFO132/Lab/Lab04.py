#Oppgave 1
import random as rnd

def oppgave1():
    alder = int(input("Hvor gammel er du?: "))
    def myndig_void(alder):
        if alder <18: 
            print("Du er ikke ikke myndig")
        else:
            print("Du er myndig")

    def myndig_resultat(alder):
        if alder <18: 
            return False
        else:
            return True
    myndig_void(alder)
    print(myndig_resultat(alder))
oppgave1()

def oppgave2():
    def fullt_navn(fornavn, etternavn, mellomnavn =""):
        if mellomnavn !="":
            return fornavn + " " + mellomnavn + " " + etternavn + " "
        else:
            return fornavn + "" + etternavn

    print(fullt_navn("Sondre", "Faanes"))
oppgave2()

def oppgave3():
    SPAR = '\u2660'
    RUTER = '\u2666'
    KLØVER = '\u2663'
    HJERTER = '\u2665'

    def tilfeldig_kort(farge=None):
        if farge is None:
            farge = rnd.choice(seq=[SPAR, RUTER, KLØVER, HJERTER])
          
        tall= rnd.randint(1, 13)
        
        if tall == 1:
            print(farge + "A")
        elif tall == 11:
            print(farge + "J")
        elif tall == 11:
            print(farge + "Q")
        elif tall == 11:
            print(farge + "K")
        else:
            print(farge + str(tall))

    tilfeldig_kort()
    tilfeldig_kort(RUTER)
    tilfeldig_kort(SPAR)

oppgave3()

def oppgave4():
    def siffer_fra_høyre(tall, n):
        tall = str(tall)
        print(tall[-n])

    siffer_fra_høyre(34621, 3)

    def siffer_fra_venstre(tall, n):
        tall = str(tall)
        print(tall[n -1])

    siffer_fra_venstre(57431, 2)

oppgave4()

def oppgave6():
    def sorter_tre_tall(minst, midten, størst):
        if minst > midten:
            temp = minst
            minst = midten
            midten = temp
        
        if  midten > størst:
            temp = midten
            midten = størst
            størst = temp

        if midten < minst:
            temp = midten
            midten = minst
            minst = temp

        print(minst, midten, størst)
    sorter_tre_tall(123, 1005, 70)

oppgave6()
