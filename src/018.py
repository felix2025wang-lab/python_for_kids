name_1 = input("Gebe Felix money ein: ")
name_1 = float(name_1)
name_2 = input("Gebe Tao money ein: ")
name_2 = float(name_2)
if name_1 > name_2:
    print("Felix ist reicher.")
if name_1 < name_2:
    print("Tao ist reicher.")
if name_1 == name_2:
    print("Felix und tao sind gleich reich.")