#Oppgave 1

#for loop for fakultet
def fak(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    return m

print(fak(4))

# while loop for fakultet
def fak2(y):
    n = 1
    while y > 0:
        n = y*n
        y-= 1
    return(n)

print(fak2(3))
#Oppgave 2
class Monark:
    etterfølger = None

    def __init__(self, navn, nasjon, tiltredelse):
        self.navn = navn
        self.nasjon = nasjon
        self.tiltredelse = tiltredelse
    
    def skriv(self):
        print ("Kong " + self.navn + " av " + self.nasjon + " tiltro i " + str(self.tiltredelse))
        if self.etterfølger is not None:
            self.etterfølger.skriv()

    def sett_etterfølger(self, neste):
        self.etterfølger = neste
        

haakon7 = Monark("Haakon VII", "Norge", 1905)
olav5 = Monark("Olav V", "Norge", 1937)
harald5 = Monark("Harald V", "Norge", 1991)

kongerekke = haakon7

haakon7.sett_etterfølger(olav5)
olav5.sett_etterfølger(harald5)

kongerekke.skriv()



