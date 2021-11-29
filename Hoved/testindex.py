import random
SPAR_SYMBOL = '\u2660'
RUTER_SYMBOL = '\u2666'
KLØVER_SYMBOL = '\u2663'
HJERTER_SYMBOL = '\u2665'
kortstokk = []


bunke1 = []
bunke2 = []
bunke3 = []
bunke4 = []
bunke5 = []
bunke6 = []
bunke7 = []
bunke8 = []
for kort in range(7, 15):
    kortstokk.append(f'\u2660{kort}')
    kortstokk.append(f'\u2666{kort}')
    kortstokk.append(f'\u2663{kort}')
    kortstokk.append(f'\u2665{kort}')

def del_ut():
    random.shuffle(kortstokk)
    for j in range(4):
        for i in range(8):
            if i == 0:
                bunke1.append(kortstokk.pop())
            elif i == 1:
                bunke2.append(kortstokk.pop())
            elif i == 2:
                bunke3.append(kortstokk.pop())
            elif i == 3:
                bunke4.append(kortstokk.pop())
            elif i == 4:
                bunke5.append(kortstokk.pop())
            elif i == 5:
                bunke6.append(kortstokk.pop())
            elif i == 6:
                bunke7.append(kortstokk.pop())
            elif i == 7:
                bunke8.append(kortstokk.pop())

bunke=bunke1,bunke2,bunke3,bunke4,bunke5,bunke6,bunke7,bunke8
def velg_kort2():
    
    inp = input("velg to bunker: ")
    endre = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    if len(inp)==2:
        a1 = endre[inp[0]]
        a2 = endre[inp[1]]
        fjern_kort1(a1,a2)

def tap(a1,a2):
    #If bunke[a1]==None: 
        #print("Du tapte")
        #break
        #Kjør spill2 på nytt.
    pass
def fjern_kort1(a1,a2):
    endre = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    # mulige_valg = ("ABCDEFGH")
    if a1 != a2:
        # and a1 in mulige_valg and a2 in mulige_valg
        bunke[a1].pop(-1)
        bunke[a2].pop(-1)

def spill2():
    while True:
        del_ut()
        print("A: ",[bunke1[-1]])
        print("B: ",[bunke2[-1]])
        print("C: ",[bunke3[-1]])
        print("D: ",[bunke4[-1]])
        print("E: ",[bunke5[-1]])
        print("F: ",[bunke6[-1]])
        print("G: ",[bunke7[-1]])
        print("H: ",[bunke8[-1]])
        velg_kort2()
    # print(bunke1)
    # print(bunke2)
    # print(bunke3)
    # print(bunke4)
    # print(bunke5)
    # print(bunke6)
    # print(bunke7)
    # print(bunke8)
spill2()



