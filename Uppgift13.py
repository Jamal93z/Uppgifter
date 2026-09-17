Användarnamn = set()

while True:
    print("1. Lägg till ett användarnamn")
    print("2. Visa alla användarnamn")
    print("3. Avsluta")

    val = input("Välj ett alternativ: ")

    if val == "1":
        Namn = input("Ange användarnamn: ")
        Användarnamn.add(Namn)

    elif val == "2":
        print("Alla användarnamn:")
        print(Användarnamn)

    elif val == "3":
        print("Programmet avslutas.")
        break