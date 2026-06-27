height = float(input("Groesse eingeben"))
weight = float(input("Gewicht eingeben"))
bmi = weight / height ** 2
print("bmi:", bmi)
if bmi < 18.5:
    print("duenn")
elif 18.5 <= bmi < 24:
    print("normal")
elif 24 <= bmi < 28:
    print("dick")
else:
    print("fett")