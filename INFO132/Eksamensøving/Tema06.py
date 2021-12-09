def antallVokaler(tekst):
    antall_vokaler = 0
    vokaler = ("AaEeIiOoUuYyÆæØøÅå")
    for c in tekst:
        if c in vokaler:
            antall_vokaler+=1
    print(antall_vokaler)
antallVokaler("Tre små kinesere på høybro plass")

#Oppgave 2?
