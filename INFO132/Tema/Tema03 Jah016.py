#Oppgave 1
x1=9
y1=66
print("Oppgave 1a\n")
print("9!=7 and 66 <= 50")
print(x1!=7 and y1 <= 50,"\n")
print("(x>7 or y<66) and (x>y or y<100)")
print(x1>7 or y1<66) and (x1>y1 or y1<100)
#Oppgave 1b
print("Ekvivialent uttrykk:")
#(7=!x and 50 >=y)
#print(66>y1 or 7<x1) and (y1<x1 or 100>y1)
#Oppgave 2
bystyret = 5
ordfører = 9
print("Oppgave 2\n")
x = int(input("Hvor gammel er du: "))  
y = int(input("Hvor mange år har du bodd i Tulleby: "))
#If-statement for ordfører/bystyret
if x >= 30 and y >= 9:
        print("Du kan bli ordfører eller sitte i bystyret.")
elif x >=30 and y >=5 <= 9:
        print("Du kan sitte i bystyret, prøv igjen om", 9-y, "år for å kunne bli ordfører.")
elif x >= 25 and y >= 5:
        print("Du kan sitte i bystyret. prøv igjen om", 30-x, "år for å bli ordfører")
elif x < 25:
        print("prøv igjen om", 30-x, "år for å sitte i bystyret.", 30-x, "år for å bli ordfører.")
elif x >= 30 and y <9 and y>5:
        print("Du kan sitte i bystyret, prøv igjen om", 9-y, "for å bli ordfører.")
elif x>=30 and y < 5:
        print("Du må bo i Tulleby i", 9-y, "år for å bli ordfører.", 5-y, "år for å sitte i bystyret.")
elif x<30 and y >= 5:
        print("Du kan sitte i bystyret, men", 30-y, "år for å kunne bli ordfører")
elif x<30 and y<5:
        print("Du må vente i", 9-y, "år for å bli ordfører",5-y, "år for å sitte i bystyret")
#Oppgave 3
print("Oppgave 3\n")
x=int(input('Tall: '))
if x>5 and x < 10:
        print("6,7 ,8 eller 9")
elif x >= 10:
        print("Minst 10")
else:
        print ("Maks 5")
