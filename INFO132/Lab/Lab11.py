from tkinter import *
rotvindu = Tk()

def dna_streng():
    pass

def tell():
    antall = DNA_sekvens.get("1.0", "end")
    print(antall)
    A = antall.count("A")
    T = antall.count("T")
    C = antall.count("C")
    G =antall.count("G")
    print("Antall A:", A, "Antall T:",T,"Antall C:",C,"Antall G:",G)
    return("Antall A:", A, "Antall T:",T,"Antall C:",C,"Antall G:",G)

def lukk_vindu():
    print("Du har trykket på lukkeknappen")
    rotvindu.destroy()
    
teller = Button(rotvindu,
text="Tell",
width=4,
height=2,
bd=2,
command= tell,
relief=GROOVE,
fg="Black",
bg="White"
)
teller.grid(row=2, column=1)

DNA_sekvens=Text(
rotvindu,
height=20,
width=40,
relief=GROOVE
)
DNA_sekvens.grid(row=1, column=1)

knapp = Button(rotvindu,
text="lukk",
command=lukk_vindu,
width=4,
height=2,
relief=GROOVE,
fg="White",
bg="Red",
bd=2
)
knapp.grid(row=4,column=1)
output_teller = Label(rotvindu,
text=tell(),
width=40,
height=3,
bd=2,
relief=GROOVE
)
output_teller.grid(row=3,column=1)
rotvindu.mainloop()

