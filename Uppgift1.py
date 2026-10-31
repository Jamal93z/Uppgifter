class bok:
    def __init__(self, titel):
        self.titel = titel  
        self.utlånad = False

   
class läsare:
    def __init__(self, namn):
        self.namn = namn

    def låna_bok(self, bok):
        if bok.utlånad:
            print("Boken är utlånad")
        else:
            bok.utlånad = True
            print(self.namn, "lånad", bok.titel)

    def lämna_bok(self, bok):
        bok.utlånad = False
        print(self.namn, "lämnad tillbaka", bok.titel)

bok1 = bok("Utvandrarna")
bok2 = bok("Flätan")

Jamal = läsare("Jamal")
Karen = läsare("Karen")

Jamal.låna_bok(bok1)
Karen.låna_bok(bok1)
Karen.låna_bok(bok2)
Jamal.lämna_bok(bok1)
Karen.låna_bok(bok1)