#Dictionaries består av key:value par. Disse må separeres i en definert dictionary ved bruk av :. 
#En dictionary defineres som en liste, men med curly brackets istedet for vanlige. Eks: dict = {}
#En dictionary er unordered, kan endres.

student = {"Navn": "Sondre Faanes", "Alder": 20,
           "Fag": ["INFO132", "INFO100", "EXPHIL"]}
#Godkjente nøkler kan være string og integer

# student["Hei"] = "Hallooooo"
#Her setter vi/oppdaterer en ny nøkkel og gir den en verdi. Dette finnes flere måter å gjøre på, som .update() (Kommer senere)

#print(student["Fag"])
#For å hente frem en verdi, må man hente ut nøkkel fra dictionary. Man kan også bruke .get() som vi ser under.

# print(student.get("Hei","Not Found"))
#.get returnerer None istedet for en error hvis vi forsøker å hente ut en nøkkel som ikke er i dictionary.
#Her setter vi andre argument som "Not Found". Så dermed vil vi få "Not Found" som output hvis vi leter etter en nøkkel som ikke fins

#Update metoden, tar dictionary som input. Må skrive ({Key:value}) Ellers vil ingenting skje/feilmelding.
# student.update({"Navn":"Sondre Høybakk Faanes", "Alder": 21})
# print(student)

#Kan slette element i dictionary med del student["Alder"]
#Kan "ta tak i" elementer vi skal slette med .pop() metoden.'
Alder = student.pop("Alder")
print(student)
print(Alder)

#Hvordan se keys i dict:
# print(len(student))

# #Hvordan se alle keys i dict:
# print(student.keys())

# #Hvordan se values i dict:
# print(student.values())

# #Se keys og values:
# print(student.items())

for key, value in student.items():
    if key =="Alder":
        print("Alder: ", value)

# #Kopiere dictionary:
# kopi_student = dict(student)

# kopi_student.update({"Studieretning" : "Informasjonsvitenskap"})
# print(kopi_student)