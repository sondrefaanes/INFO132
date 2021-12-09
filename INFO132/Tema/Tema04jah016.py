# # #Oppgave 1
# def siste(sekvens):
#     siste = sekvens[-1]
#     print(siste)

# siste("python")
# siste("1,2,3,4,5")

# #Oppgave 2
# def skriv_sekvens(sekvens):
#     for x in sekvens:
#         print(x, sep=" ", end=" ")
#     print("\n")
# skriv_sekvens(range(90,100))

# # #Oppgave 3
# startbeløp = int(input("Startbeløp: "))
# rentesats = int(input("Rentesats:"))
# ønsket_beløp = int(input("Ønsket beløp: "))

# år = 1
# beløp = startbeløp
# while beløp < ønsket_beløp:
#     beløp = beløp + (rentesats/100)*beløp
#     print("år", år, ":", round(beløp, 2))
#     år+=1

#Oppgave 4
def gangetabell():
    for x in range(1,10):
        print("\n")
        for y in range(1,10):
            result = x*y
            if result < 10:
                result = " "+str(result)
            print(result, sep=" ", end= " ")          
gangetabell()   