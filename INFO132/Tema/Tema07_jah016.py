def add():
    with open("Telefon.txt", "a") as f:
        while True:
            navn = input("Name and number: ")
            f.write(navn + "\n")
            if navn == "":
                break
        
def read():        
    f = open("Telefon.txt", "r")
    print("".join(f.readlines()))

add()
read()

#Oppgave 2
with open("Telefon.txt", "r", encoding="UTF-8") as f:
    lines= f.readlines()
navn = input("Navn: ")
count = 0
for x in lines:
    if x.startswith(navn):
        y= x[len(navn)+1-1]
        print(y)
        NyttNummer = input("Nytt nummer: ")
        lines[count] = x.replace(y, NyttNummer)
        print(f"Nummer ble endret fra", y, "til", NyttNummer)
        break
    count += 1
with open("Telefon.txt", "w", encoding="UTF-8") as f:
    f.writelines(lines)
#Oppgave 3
def FjernVokaler(fil):
    with open(fil, "r", encoding="UTF-8") as f:
        vokal = ["a","A", "e","E", "i","I", "o","O", "u","U", "y","Y", "æ","Æ", "ø","Ø", "å","Å"]
        filnavn = f.read()
        for vokaler in filnavn:
            if vokaler in vokal:
                filnavn = filnavn.replace(vokaler, " ")
        print(filnavn)
    with open("Ny" + fil, "w", encoding="UTF-8") as f:   
        f.write(filnavn)
FjernVokaler("tresmåkinesere.txt") 