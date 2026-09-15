
Kontakter = {}

while True:
    print("1. Lägg till kontakt")
    print("2. Sök en kontakt")
    print("3. Ta bort kontakt")
    print("4. Avsluta")

    val = input("Välj ett alternativ: ")

    if val == "1":
        Namn = input("Ange kontaktens namn: ")
        Telefonnummer = input("Ange kontaktens telefonnummer: ")
        Kontakter[Namn] = Telefonnummer
        print("Kontakten har lagts till.")
        

    elif val == "2":
        Sök_naman = input("Skriv namnet på kontakten du vill söka efter: ")
        print ( "Du har skrivit in:", Sök_naman)
      
        if Sök_naman in Kontakter:
            print("Telefonnummer för", Sök_naman, "är:", Kontakter[Sök_naman])
        else:
                 print("Kontakten hittades inte.")
        

    elif val == "3":
        Namn = input("Ange namnet på kontakten du vill ta bort: ")

        if Namn in Kontakter:
         del Kontakter[Namn]
         print("Kontakten har tagits bort.")
        else:                                
         print("Kontakten hittades inte.")      

    elif val == "4":
        print("programmet Avslutar.")

        break
    else:
        print("Ogiltigt alternativ. Försök igen.")