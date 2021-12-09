#Lab oppgave 1
#oppgave 2
name = input("Enter your name:")
print("Hello " + name)

#Oppgave 3
hours = int(input("Enter Hours:"))
rate= float(input("Enter rate:"))
pay=hours * rate
print("Pay: ", pay)

#Oppgave 5
c=float(input("Enter celcius: "))
f= c * 1.8 +32
print("c = ", f, "farenheit")

#Lab oppgave 2


#Lab oppgave 3
import random
sekvens="?"*(random.randint(20,50))
print(sekvens)
lengde=len(sekvens)
gjetning=int(input("guess the number of ?'s: "))
print("That's "+str(gjetning==lengde)+"!")
print(lengde,"is the right answer.")

#Oppgave 4
import math
n=input("1. siffer:")
m=input("2. siffer:")
tall1=int(n+m)
tall2=int(m+n)
resultat=math.sqrt(tall1*tall2)
print("kvadratorten av",tall1,'*',tall2, "=",'%.2f'%resultat)

#Oppgave 5
n = int(input("skriv inn et tresifret tall:"))
s1=str(n//100)
rest1 = n % 100 
s2 = str(rest1 // 10) 
s3 = str(rest1 % 10) 
p1 = s1+s2+s3
p2 = s1+s3+s2
p3 = s2+s1+s3
p4 = s2+s3+s1
p5 = s3+s1+s2
p6 = s3+s2+s1
print('Permutajoner:',p1,p2,p3,p4,p5,p6)

#Oppgave 6
import random
