total = 0
grid = 1
num = 1
while grid <= 64:
    total += num
    num *= 2
    grid += 1
print(total)