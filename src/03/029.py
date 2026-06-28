list = [76, 68, 88, 44, 96, 81, 36, 80, 54, 47]
sum = 0
i = 0
for score in list:
    if score < 80:
        continue
    else:
        sum += score
        i += 1
print("durchschnit",sum/i)