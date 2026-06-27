h_1 = int(input("Bitte geben Sie die 1. Groesse ein: "))
n_1 = input("Bitte geben Sie den 1. Namen ein: ")
h_2 = int(input("Bitte geben Sie die 2. Groesse ein: "))
n_2 = input("Bitte geben Sie den 2. Namen ein: ")
h_3 = int(input("Bitte geben Sie die 3. Groesse ein: "))
n_3 = input("Bitte geben Sie den 3. Namen ein: ")
max_h = h_1
max_n = n_1
if h_2 > max_h:
    max_h = h_2
    max_n = n_2
if h_3 > max_h:
    max_h = h_3
    max_n = n_3
print("Das groesste kind ist", max_n, "mit", max_h ,"cm.")