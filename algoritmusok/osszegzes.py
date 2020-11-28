#Adott egy "N" elemu "E" szamsorozat. Hatarozzuk meg az elemek osszeget! A vegredmenyt, az "S" tartalmazza.

# Adatok bekeresi (N)
n = int(input("Add meg hogy hany elembol aljon a sorozat."))

#Elemek generalasa, jelenleg 0-tol n-ig, egy listaba "list"

list = []

for i in range(n):
    list.append(i)
    
print(list)

s = 0
for i in range(n):
    s = s + list[i]
print("A sorozat elemeinek osszege:", s)
