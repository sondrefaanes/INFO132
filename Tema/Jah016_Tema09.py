
from tkinter import *
rotvindu = Tk()
rotvindu.geometry("350x350")
rotvindu.title("Tellelek med knapp")


def lukk_vindu():
    print("Du har trykket på lukkeknappen")
    rotvindu.destroy()


tell_antall_klikk = 0


def trykk():
    global tell_antall_klikk
    tell_antall_klikk += 1
    knapp2.config(text=tell_antall_klikk)


knapp = Button(rotvindu,
               text="Farvel",
               command=lukk_vindu,
               width=20,
               height=20,
               bg="Green",
               bd=5,
               fg="Black"
               )
knapp.grid(row=0, column=0)

rotvindu.geometry("350x350")
rotvindu.title("Tellelek med knapp")

knapp2 = Button(text=tell_antall_klikk,
                command=trykk,
                fg="darkgreen",
                bg="white",
                width=20,
                height=20,
                bd=5
                )
knapp2.grid(row=0, column=1)
rotvindu.mainloop()
