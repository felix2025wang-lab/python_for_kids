temp = float(input("Temperatur"))
speed = float(input("Geschwindigkeit"))
if temp >= 25:
    if speed >= 8:
        print("warm")
    else:
        print("cool")
if temp < 25:
    if speed >= 8:
        print("kalt")
    else:
        print("scheisse")