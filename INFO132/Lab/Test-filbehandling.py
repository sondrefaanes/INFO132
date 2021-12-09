def arkiver():
    with open ("Arkivet.txt", "a") as f:
        while True:
            ny_innføring = input("Legg til: ")
            f.write("Entry: " + "\n" + ny_innføring + "\n")
            if ny_innføring == "":
                break

def åpne_arkivet():
    with open("Arkivet.txt", "r") as f:
        print("".join(f.readlines()))

arkiver()
åpne_arkivet()
