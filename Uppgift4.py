lösenord = ("")
while lösenord != "kod123":
    lösenord = input("Ange lösenord:")
    if lösenord == "kod123":
       print("välkommen!")
    else:
       print("fel lösenord")
