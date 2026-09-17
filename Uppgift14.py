
print("Hej! Och välkommen till vårt program!")

while True:
    print("1. Hälsningar")
    print("2. Idags datum")
    print("3. Avsluta programmet")

    val = input("Välj ett alternativ: ")

    if val == "1":
        print("Hej och välkommen till vårt program!")

    elif val == "2":
        from datetime import date
        idag = date.today()
        print("Idag är det:", idag)

    elif val == "3":
        print("Tack för att du använde vårt program. Programmet avslutas.")
        break

    else:
        print("Ogiltigt alternativ. Försök igen.")