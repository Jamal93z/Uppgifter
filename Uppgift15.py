print("Hej! Och välkommen till vårt program!")

while True:
    print("1. Addera tal")
    print("2. Subtrahera tal")
    print("3. Multiplicera tal")
    print("4. Avsluta programmet")

    val = input("Välj ett alternativ: ")

    if val == "1":
        tal1 = float(input("Ange det första talet: "))
        tal2 = float(input("Ange det andra talet: "))
        resultat = tal1 + tal2
        print("Resultatet av additionen är:", resultat)

    elif val == "2":
        tal1 = float(input("Ange det första talet: "))
        tal2 = float(input("Ange det andra talet: "))
        resultat = tal1 - tal2
        print("Resultatet av subtraktionen är:", resultat)

    elif val == "3":
        tal1 = float(input("Ange det första talet: "))
        tal2 = float(input("Ange det andra talet: "))
        resultat = tal1 * tal2
        print("Resultatet av multiplikationen är:", resultat)

    elif val == "4":
        print("Tack för att du använde vårt program. Programmet avslutas.")
        break
    else:
        print("Ogiltigt alternativ. Försök igen.")        