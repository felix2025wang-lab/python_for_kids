import random
n = random.randint(0,100)
while True:
    ni = int(input("zahl: "))
    if ni > n:
        print("zu gross")
        continue
    elif ni> n:
        print("zu klein")
        continue
    else:
        print("richtig")
        break