from tkinter import Tk, Label, RAISED, Button
#Grafiske brukergrensesnitt - GUI
#Konsollgrensesnitt - Terminalen vi får output
#Event-driven programming
#Reagerer på hendelser
rotvindu = Tk()

hei = Label(rotvindu, text="Hei",
width=5,
height=5,
bd=8,
relief=RAISED,
fg="Blue",
bg="Yellow"
)
hei.pack()
hei.grid(row=1,column=0)
#plasserer i hendhold til et rutenett
def lukk_vindu():
    print("Du har trykket på lukkeknappen")
    rotvindu.destroy()
#metode for å lukke programvinduet

knapp = Button(rotvindu,
text="lukk",
command=lukk_vindu,
width=20,
height=20,
relief=RAISED,
fg="Green",
bg="Red",
bd=5
)
knapp.grid(row=5,column=5)
#Lager en knapp med teksten lukk, bredde og høyde 20, ser "løftet" ut, skriftfarge grønn og bakgrunnsfarge rød, border på knappen er 5 pixler
#Command tilsier vilken hendelse som skal kjøre, i dette tilfellet er det lukk_vindu, en brukerdefinert funksjon som lukker vinduet.

# knapp.config()
#Config sier egenskaper som størrelser, farger, rammer og mer
rotvindu.mainloop()


# rotvindu.destroy()