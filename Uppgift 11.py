
Frukter = [ "äpple", "banan", "päron" ]
print ("Här är våren lista med frukter:", Frukter)


Ny_frukt = input(" Vilken frukt vill du lägga till i listan? ")
while Ny_frukt in Frukter:
    print("Denna frukt finns redan i listan.")
    Ny_frukt = input(" Välj en annan frukt: ")
else:    
     Frukter.append(Ny_frukt)
     print("Här är din uppdaterade lista med frukter:", Frukter)

Ny_listan = input("Vilken frukt vill du ta bort från listan? ")
Frukter.remove(Ny_listan)

print("Här är din uppdaterade lista med frukter:", Frukter)
