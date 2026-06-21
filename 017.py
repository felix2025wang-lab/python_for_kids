a = float(input("Bitte geben Sie die erste Seitenlaenge ein: "))
b = float(input("Bitte geben Sie die zweite Seitenlaenge ein: "))
c = float(input("Bitte geben Sie die drite Seitenlaenge ein: "))
if a + b > c and a + c > b and b + c > a:
    print("Dreieck")
if a + b <= c or a + c <= b or b + c <= a:
    print("Kein Dreieck")