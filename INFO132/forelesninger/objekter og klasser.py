handleliste = []

while True:
    vare = input("Hvilken vare vil du legge til: ")
    handleliste.append(vare)
    if vare == "stopp":
        break

print(handleliste)

class Person:
    navn = None
    telefon = None
    adresse = None
    nasjonalitet = "norsk"

    def skriv_ut(self):
        print(self.navn, "er", self.nasjonalitet,
        "og har telefonnummer", self.telefon, 
        "og adresse", self.adresse, end=".\n")
        
        
kari = Person()
kari.navn = "Kari Nordmann"
kari.telefon = "12345678"
kari.adresse = "Tullevei 12, 5007 Bergen"

class Navn:
    fornavn = None
    etternavn = None

class Adresse:
    gateadresse = None
    poststed = None

class Person:
    navn = Navn()
    telefon = None
    adresse = Adresse()
    nasjonalitet = "Norsk"
    
    def skriv_ut(self):
        print(self.navn.fornavn, self.navn.etternavn, 'er',
        self.nasjonalitet, 'og har telefonnummer', self.telefon,
        'og addresse', self.adresse.gateadresse, self.adresse.poststed,
        end='.\n')

kari = Person()
kari.navn.fornavn = 'Kari'
kari.navn.etternavn = 'Normann'
kari.telefon = 98765432
kari.adresse.gateadresse = 'Tullevei 9'
kari.adresse.poststed = '9876 Tøysedal'
kari.skriv_ut()