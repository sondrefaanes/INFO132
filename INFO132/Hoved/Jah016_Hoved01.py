#Hovedoppgave 1 - Sondre Faanes
#Oppgave 1 - rett oppgave
import math
math.pi
def pi_funksjon(desimal):
    a = round(math.pi, desimal)
    if desimal >=2:
        return round(math.pi, desimal)
    elif desimal >= 15:
        return "For mange desimaler"
    elif 0 < desimal < 16:
        return('%.2f' % math.pi)

#Oppgave 2
def convert_temp(scale, source_temp=None):
    if scale == "F":
        return 'C', (source_temp - 32.0) * (5.0/9.0)
    elif scale == "C":
        return 'F', (source_temp * (9.0/5.0)) + 32.0
    else:
        return 'C', (source_temp - 32.0) * (5.0/9.0)
#Oppgave 3A
saldo = 500
rentesats = 0.01

def innskudd(innskudd):
    global saldo
    global rentesats
    saldo += innskudd
    if saldo-innskudd < 1000000 and saldo > 1000000:
        print("Du har fått bonusrente")
        rentesats = 0.02

def uttak(uttak):
    global saldo    
    global rentesats
    saldo = saldo-uttak
    if uttak > saldo:
        return("Overtrekk")
    elif saldo < 1000000 and saldo <= 1000000:
        print("Du har ordinær rentesats")
        rentesats = 0.01

def beregn_rente():
    print(saldo*rentesats)

def renteoppgjør():
    global saldo
    global rentesats
    saldo += saldo*rentesats

#Oppgave 3B/3C
#Oppgavene er gjort samtidig så det ikke ble så mye kluss.
logliste = ["Ingen tidligere endringer", "Ingen tidligere endringer", "Ingen tidligere endringer"]

def velg():
    global saldo
    global rentesats
    global logliste
    print("_______________ ")
    print("1 - vis saldo   ")
    print("2 - innskudd    ")
    print("3 - uttak       ")
    print("4 - renteoppgjør")
    print("5 - siste endringer")
    print("_______________ ")
    a = int(input("Velg: "))
    if a == 1:
        print(saldo)
    elif a == 2:
        b = int(input("Beløp: "))
        innskudd(b)
        logliste += ["-"+str(b)]
    elif a == 3:
        c = int(input("Uttak: "))
        uttak(c)
        print(saldo)
        logliste  += ["-"+str(c)]
    elif a == 4:
        renteoppgjør()
        logliste += ["+"+str(saldo*rentesats)]

    elif a == 5:
        print(logliste[-3])
        print(logliste[-2])
        print(logliste[-1])
        print("Din saldo er nå", saldo)
velg()
#Oppgave 4
import random
def tre_tilfeldige():
    x = random.randint(1,9)
    y = random.randint(1,9)
    z = random.randint(1,9)
    tilfeldige = [x, y, z]
    tilfeldige.sort()
    print (tilfeldige)