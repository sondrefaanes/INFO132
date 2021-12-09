#Oppgave 1
def antall_vokaler(setning):
    vokal = ["a","A", "e","E", "i","I", "o","O", "u","U", "y","Y", "æ","Æ", "ø","Ø", "å","Å"]
    antall = 0
    for bokstav in setning:
        if bokstav in vokal:
            antall += 1
    return antall

print(antall_vokaler("Hei hvordan går det"))

#Oppgave 2
TV = '''\
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
'''
def verv(navn):
    liste = TV.split("\n")
    verv_person = []
    for verv in liste:
        if navn in verv:
            pos_verv = verv.find(": ")
            jobb = verv[0:pos_verv]
            verv_person.append(jobb)
    return verv_person
print(verv("Kari"))




