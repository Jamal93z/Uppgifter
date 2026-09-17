
Kontakter = {}

while True:
    print("1. Lägg till en kontakt")
    print("2. Sök efter en kontakt")
    print("3. Avsluta programmet")

    val = input("Välj ett alternativ: ")

    if val == "1":
        print("Lägg till namn till kontakten")
        namn = input("Ange kontaktens namn: ")
        print("Lägg till telefonnummer till kontakten")
        telefonnummer = input("Ange kontaktens telefonnummer: ")
        Kontakter[namn] = telefonnummer
        print("Kontakten tillagd.")

    elif val == "2":
        print("Sök efter en kontakt")
        namn = input("Ange kontaktens namn: ")
        if namn in Kontakter:
            print("Telefonnummer för", namn, "är:", Kontakter[namn])
        else:
            print("Kontakten finns ej.")

    elif val == "3":
        print("Tack för att du använde vårt program. Programmet avslutas.")
        break

    else:
        print("Ogiltigt alternativ. Försök igen.")


    
