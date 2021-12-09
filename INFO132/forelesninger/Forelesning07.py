#Forelesning 7. Tegnstrenger
#Kapittel 6, Python for everybody
tegnstreng = "Hei dette er en finfin tegnstreng"
print(tegnstreng)

print("Lorem Ipsum Kotoma".split())
#Internasjonalt kodespråk er unicode

print("Jens" == "jens")
#Store bokstaver kommer før små i Python

jj = "Juba Juba"

jj[0]
#Indeksering. bruker brackets for å finne og returnere en verdi inne i en streng, må være i strengens indeks!

jj[0:4]
#Gjør her en slice. Velger å ta ut element 0 til 4 fra variabelets definerte. 
#Indeksen er slik: 0,1,2,3,4. Starter alltid på null. -1 er det siste i indeksen, dermed er -2 den nest siste.
#Sluttindeks - startindeks = lengde på indeks

jj[0:10:2]
#Den siste i bracketsene sier at vi skal ta annenhvert tall

"!" in jj
#Tester for å se om "!" er en del av tegnstrenger jj. Returnerer "True" eller "False"

#str.endswidth("")/str.startswith("")
#Ser om en string starter eller slutter med din bestemte input

"Tranversering av tegnstreng"
t = "Det er også mulig å skrive en tekst som strekker seg over flere linjer."

for linje in t.split("\n"):
    print(linje)
#Denne metoden funker ikke^^^

print("Tegnstrenger er uforanderlige")
#Verdien til et tekstobjekt kan ikke modifiseres(Muteres)
#Strengoperatorer endres ikke, de bare lager nye

#print(dir(str))
#Brukes for å se alt som påvirker string eller brukes for string

#Find kan brukes for å finne hvor en delstreng begynner i en streng

#streng.find(delstreng) 
#returnerer første posisjon i teksten der delstrenger begynner
#Hvis delstreng ikke finnes, returneres "-1"

tekst = "Juba Juba, danser som en snegle"
print(tekst.find("danser"))

def finn_alle(tekst, delstreng):
    liste = []
    pos = 0
    while True:

        pos = tekst.find(delstreng, pos+1)
        if pos != -1:
            break
        list.append(pos)
    return liste
finn_alle("akkarkabaret", "k")
