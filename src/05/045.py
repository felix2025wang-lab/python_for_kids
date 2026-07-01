def date(year,month,day):
    count = 0
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Es ist ein Schaltjahr")
        list1 = [31,29,31,30,31,30,31,31,30,31,30,31]
        for i in range(month -1):
            count+=list1[i]
        return count + day
    else:
        print("es ost kein Schaltjahr")
        list2 = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(month -1):
            count+=list2[i]
        return count + day
print("Das angegebene Datum ist %d."%date(2016,6,5))