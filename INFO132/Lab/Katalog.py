print("Dette er en personkatalog")
list = []

while True:
    name = input("Enter name and phone number: ")
    list.append(name)
    choice = input("Do you want to stop? Type Yes to stop or any key to continue: ")
    if choice == "Yes":
        break

print("Names added to the catalogue are", list)  
