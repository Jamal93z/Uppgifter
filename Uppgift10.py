
Barn = "50 sek"
Vuxen = "100 sek"
Pensionär = "70 sek"

Biljetter = input(" Vilken biljettkategori har du? (Barn, Vuxen, Pensionär) ")

if Biljetter == "Barn":
    print("Din biljett kostar: ", Barn)
elif Biljetter == "Vuxen":
    print("Din biljett kostar: ", Vuxen)
elif Biljetter == "Pensionär":
    print("Din biljett kostar: ", Pensionär)
else:
    print("Ogiltig biljettkategori")