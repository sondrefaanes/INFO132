#Temaoppgave 2
print("Oppgave 1\n")
import math
r = float(input("Radius :"))
areal = math.pi * r * r
print("arealet til en sirkel med ", r, "er = %.3f" %areal)

print("Oppgave 2 \n")
setning = input("Skriv inn setning: ")
antall = int(len(setning))
gjetning = int(input("gjett lengde: "))
print("That's ", antall==gjetning, "!!")

print("Oppgave 3\n")
import random
x = str(input("Skriv inn et tall: "))
y = str(random.randint(0,9))
variabel = int(x)
nytall = int(x+y)
print(nytall,"/", variabel, "=", nytall/variabel)