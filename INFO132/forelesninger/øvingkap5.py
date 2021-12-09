#øving klasser og objekter
class Bil:
    merke =  None
    modell = None
    toppfart = 0
    kapasitet = 5
    lillebror = None

    def __init__(self, merke, modell, toppfart):
        self.merke = merke
        self.modell = modell
        self.toppfart = toppfart
    
    def skriv(self):
        print("Bil av merke " + self.merke)
        print("Modell: " + self.modell)
        print("Plass til " + str(self.kapasitet) + " med toppfart " + str(self.toppfart))
        print("Lillebror: ")
        if self.lillebror is not None:
            self.lillebror.skriv()

audi = Bil("Audi", "A4", 200)
a3 = Bil("Audi", "A3", 240)
a2 = Bil("Audi", "A2", 180)
a1 = Bil("Audi", "A1", 175)

audi.lillebror =  a3
a3.lillebror = a2
a2.lillebror = a1

audi.skriv()

class Varebil():
    merke =  None
    modell = None
    toppfart = 0
    kapasitet = 3

    def __init__(self, merke, modell, toppfart):
        self.merke = merke
        self.modell = modell
        self.toppfart = toppfart

    def skriv(self):
        print("Bil av merke " + self.merke)
        print("Modell: " + self.modell)
        print("Plass til " + str(self.kapasitet) + " med toppfart " + str(self.toppfart))

Transporter = Varebil("Ford", "Transporter", 160)
Zavala = Varebil("Titan","Striker", 160 )

Zavala.skriv()
