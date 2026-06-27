price = 200
height = float(input(" Bitte geben sie die Groesse an:  "))
if height <= 1.4:
    save = price * 0.5
    print("Der  preiss ist: ", save)
else:
    save = price * (1 - 0.9)
    print("Der preis ist: ", save)
print("Sie sparen: ", price - save)