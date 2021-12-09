eksamen = {
    'INFO100': 'C', 'INFO104': 'B', 'INFO116': 'E',
    'INFO180': 'A', 'INFO201': 'F', 'INFO280': 'C',
    'GEO101': 'D', 'GEO110': 'B', 'ADM101': 'A',
    'ECON100': 'B', 'ECON201': 'C', 'GEO210': 'C',
    'FAIL101': 'F'
}

def karakterfrekvenser(dict):
    frekvens = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' :  0, 'F' : 0}
    for a in dict.values():
        if a == 'A':
            frekvens['A'] += 1
        elif a == 'B':
            frekvens['B'] += 1
        elif a == 'C':
            frekvens['C'] += 1
        elif a == 'D':
            frekvens['D'] += 1
        elif a == 'E':
            frekvens['E'] += 1
        elif a == 'F':
            frekvens['F'] += 1
    print(frekvens)
    return frekvens
print()
a= karakterfrekvenser(eksamen)     
a

def histogram(frekvens):
    print('A', frekvens['A']*'*')
    print('B', frekvens['B'] * '*')
    print('C', frekvens['C'] * '*')
    print('D', frekvens['D'] * '*')
    print('E', frekvens['E'] * '*')
    print('F', frekvens['F'] * '*')
histogram(a)
#Oppgave 2A)
engelske_siffer = {
 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}
print()
def sort(dictionary):
    for element in dictionary:
        if element in dictionary.keys():
            print(element,":", dictionary[element]) 
sort(engelske_siffer)
print()
#Oppgave 2B)
def snu_fortegnelse(old_dict):
    new_dict = dict([(value, key) for key, value in old_dict.items()])
    for i in new_dict:
        print(i, ":", new_dict[i])
snu_fortegnelse(engelske_siffer)
print()
#Oppgave 2C
def flip_fortegnelse(fortegnelse):
    for i in sorted(fortegnelse.keys(), reverse=True):
        print(i,engelske_siffer[i]) 
flip_fortegnelse(engelske_siffer)