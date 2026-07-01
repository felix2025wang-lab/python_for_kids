import time
b = input("bitte geben sie ihr geburtsdatum ein, z.B. (20060101):")
x = time.mktime(time.strptime(b,"%Y%m%d"))
a = time.time()
c = a-x
m=c/60
h = m/60
d = h/24
y = d/365
print("du lebst schon\n",int(c),"sekunden\n",int(m),"minuten\n",int(h),"stunden\n",int(d),"tage\n", round(y, 2),"Jahre")
