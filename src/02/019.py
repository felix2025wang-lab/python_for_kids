num = int(input("Bitte geben Sie eine Zahl ein: "))
num_r = str(num) [::-1]
print(str(num), num_r)
if str(num) == num_r:
    print("Ja")
if str(num) != num_r:
    print("Nein")