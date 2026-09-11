summa = 0

while summa < 100:

    tal = int(input("Ange ett tal: "))
    summa = summa + int(tal)
    print ("summa är: ", summa)

    if summa >= 100:
        print ("summan är mer än 100")

print ("summan är: ", summa)