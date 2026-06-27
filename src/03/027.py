money = float(input("Geld: "))
for i in range(10):
    y = i + 1
    f = money * (1 + 0.05) ** y
    print("Investieren %d Jahre: "%y, round(f,2))