import random
import datetime
import time
l = str(input("A feladat 200-ban maximalizalta az utasitas sorozatot, ki szeretned kapcsolni? (igen/nem)"))
available_instructions = ["E", "K", "D", "N"]
instruction_set = []
list = []

z = 0
if l == 'nem' and 4:
    n = int(input("Add meg hogy hany elembol aljon az utasitas sorozat:"))
    while n > 200:
        n = int(input("Mivel az elozo lepesnel azt valasztottad, hogy aktivalod a limitet, igy 200 alatti pozitiv egesz szamot kell valasztanod!"))
        z = z + 1
        if z == 5:
            n = int(input("Kerlek olvasd el figyelmesen a kiirt informaciokat! Ez az utolso elotti lehetoseged! Ha itt, illetve a kovetkezonel helytelenul adod meg az adatokat akkor a program le fog allni. Lehetoseged van ujra elinditani!"))
        if z == 6:
            exit("Inditsd ujra a prgramot")
    for i in range(n):
       k = random.choice(available_instructions)
       instruction_set.append(k)

elif l == 'igen':
    n = int(input("Add meg hogy hany elembol aljon az utasitas sorozat:"))
    for i in range(n):
       k = random.choice(available_instructions)
       instruction_set.append(k)
elif l != 'igen' or 'nem':
    exit("Nem megfelelo adatbevitel. Inditsd ujra a programot!")

kezdoido = datetime.datetime.now()

#Egyszerusiteshez hasznalt lista generalasa az eredeti listabol, ezt a listat fogja majd "csonkitani"
short_list = instruction_set.copy()

##0. feladat
# Kilistazza a generalt utasitaskeszletet.
print("A generalt utasitaskeszlet:\n",instruction_set)



##2-es feladat - Egyszerusitheto-e az utasitassorozat?
z = len(short_list)

i = 0
time.sleep(1)

while i+1 < z:
        #print("i ertek:", i)
        #print("z ertek:", z)
        if (short_list[i] == "K" and short_list[i+1] == "N") or (short_list[i] == "N" and short_list[i+1] == "K") or (short_list[i] == "E" and short_list[i+1] == "D") or (short_list[i] == "D" and short_list[i+1] == "E"):
        #if (short_list[i] == "K" and short_list[i+1] == "N") or (short_list[i] == "N" and short_list[i+1] == "K") or (short_list[i] == "E" and short_list[i+1] == "D") or (short_list[i] == "D" and short_list[i+1] == "E"):
        #if (instruction_set[i] == "K" and instruction_set[i+1] == "N") or (instruction_set[i] == "N" and instruction_set[i+1] == "K") or (instruction_set[i] == "E" and instruction_set[i+1] == "D") or (instruction_set[i] == "D" and instruction_set[i+1] == "E"):
           time.sleep(1)
           if i != len(short_list) -1:
                time.sleep(1)
                print("Egyszerusites talalat:", i)
                print("Egyszerusites talalat:", i + 1)
                short_list.pop(i) ; short_list.pop(i)
                time.sleep(1)
                time.sleep(1)
                print("Aktualis lista:", short_list)
                time.sleep(1)
                z = len(short_list)-1
                time.sleep(1)
                #print("z process utan:", z)
                time.sleep(1)
                time.sleep(1)
                i = 0
        i = i + 1
time.sleep(1)
if len(short_list) > 1:
    if ((short_list[0] == "N" and short_list[1] == "K") or (short_list[0] == "K" and short_list[1] == "N")) or ((short_list[0] == "E" and short_list[1] == "D") or (short_list[0] == "D" and short_list[1] == "E")):
        time.sleep(1)
        short_list.pop(0) ; short_list.pop(1)
        time.sleep(1)
print("Aktualis lista:", short_list)

##1-es feladat - Hany lepesbol all az utasitassorozat?
#debug print("INFO--> felsorolja az elemeket:", instruction_set)
print("1. Hany lepesbol all az utasítassorozat?", len(instruction_set), "lepesbol all!")

##2-es feladat - Egyszerusitheto-e az utasitas sorozat?
if len(instruction_set) - len(short_list) < len(instruction_set):
    print("2/a. Lehet-e egyszerusiteni az utasitas sorozatot? Igen lehet!")
    print("2/b. Mennyi lesz az egyszerusitett utasitas sorozat hossza?", len(short_list))
    print("2/c. Mennyivel lehetett egyszerusiteni(ennyi 'felesleges' utasitas van)?", type((int(len(instruction_set)) - int(len(short_list))) /int(2)),"darab egyszerusitheto part talaltam!")
else:
    print("2/a. Lehet-e egyszerusiteni az utasitas sorozatot? Sajnos nem lehet!")


## 3. feladat - Visszajuttatas "origoba"

#Összeszamolom, hogy egtajonkent osszesen hany lepes volt
db_e = 0
db_d = 0
db_k = 0
db_n = 0
for i in range(n):
    if instruction_set[i] == "E":
        db_e = db_e + 1
    if instruction_set[i] == "D":
        db_d = db_d + 1
    if instruction_set[i] == "K":
        db_k = db_k + 1
    if instruction_set[i] == "N":
        db_n = db_n + 1
#print("E =", db_e, "D =", db_d, "K =", db_k, "N =", db_n)


#Meghatarozom a "koordinatarendszerem" fuggoleges tengelyet. Fuggolegesen: eszak(+) del (-)
f = db_e - db_d

if f < 0:
    print("3/a. Visszajutas az origoba --> eszaki iranyban(fel):", (f*-1), "egyseg!")
else:
    print("3/a. Visszajutas az origoba --> deli iranyban(le):", f, "egyseg!")

#Meghatarozom a "koordinatarendszerem" vizszintes tengelyet. Vizszintesen: kelet(+) nyugat(-)
v = db_k - db_n

if v < 0:
    print("3/b. Visszajutas az origoba --> keleti iranyban(jobb):", (v * -1), "egyseg!")
else:
    print("3/b. Visszajutas az origoba --> nyugati iranyban(bal):", v, "egyseg!")

##4. feladat Mikor kerul a legtavolabb a robot legvonalban az "origotol"?
#Itt pitagorasz tetellel szamolok. Ki kell szamolnom az "x" es az "y" iranyu elmozdulasokat. Ezeket a kepletbol "a"-nak es "b"-nek feleltetem meg, es keresem "c".
#Vegig megyek az utasitas sorozaton es ket darabos blokkokra bontva kiszamolom minden ilyen esetnek a "c" erteket. Ezt az erteket egy "list" nevu listaba betoltom.
#A ciklus vege utan egy "max" fuggvennyel megkeresem a legnagyobb erteket, es "round" fuggvennyel kerekitem 3 tizedesre.
#A "print(list.index(max(list)))" ez a "list" lista-bol adja vissz azt, hogy mi az index szama annak az elemnek ami a legmagasabb volt a listaban.
db_x = 0
db_y = 0

for i in range(n):
    if instruction_set[i] == "K":
        db_x = db_x +1
    if instruction_set[i] == "N":
        db_x = db_x -1
    if instruction_set[i] == "E":
        db_y = db_y +1
    if instruction_set[i] == "D":
        db_y = db_y -1
    c = (((db_x**2) + (db_y**2)))**(1/2)
    list.append(c)
    #debug print("INFO-->", c)
    #debug print("INFO--> Pitagorasz eredmenyek:" , list)
#debug print("INFO-->", db_x)
#debug print("INFO-->", db_y)
if len(list) > 0:
    print("4/a. Hanyadik lepesnel kerul a legtavolabb a robot az 'origotol':", list.index(max(list)))
    print("4/b. Mekkora volt ez a tavolsag legvonalban, az origotol:", round((max(list)), 3))
else:
    print("4/a. Hanyadik lepesnel kerul a legtavolabb a robot az 'origotol': Nem tortent elmozdulas!")
    print("4/b. Mekkora volt ez a tavolsag legvonalban, az origotol': Nem tortent elmozdulas!")

##5. feladat Akkumulator felhasznalas kiszamitasa. Indulashoz 2 egyseg, irany valtas 2 egyseg, ha nincs iranyvaltas, akkor 1 egyseg. Akkumulator kapacitas: 100 illetve 1000 egyseg
#Itt meghatarozom, hogy mennyi egyseg energia fog elfogyni. "db4" 2-rol indul, igy az indulassal mar nem kell foglalkoznom. Ha ket egymas utani irany van, akkor az en ertelmezesem szerint nincs iranyvaltas,
#es 1 egyseg energia kell. Ha van iranyvaltas (i és i+1 nem azonos), akkor van iranyvaltas es 2 egyseg energia kell.
db4 = 2
for i in range(n-1):
    if instruction_set[i] == instruction_set[i+1]:
        db4 = db4 +1 + 1        # innen az utolso 1-es nem biztos hogy kell
    else:
        db4 = db4 +2 + 1       # innen az utolso 1-es nem biztos hogy kell
if len(list) > 0:
    if db4 <= 100:
        print("5/a. Az utasitas sorozat vegrehajtasahoz melyik akkumulatorra van szukseg? A 100 egysegnyi energiaju akkumulator is elegendo.")
        print("5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", db4)
    if 100 < db4 < 1000:
        print("5/a. Az utasitas sorozat vegrehajtasahoz melyik akkumulatorra van szukseg? A 1000 egysegnyi energiaju akkumulatorra van szukseg.")
        print("5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", db4)
    if 1000 < db4 < 1100:
        print("5/a. Az utasitas sorozat vegrehajtasahoz mind a 100 mind pedig az 1000 egysegnyi energiaju akkumulatorra szukseg van!")
        print("5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", db4)
    if db4 > 1100:
        print("5/a. Sem a 100 sem pedig az 1000 egysegnyi energiaju akkumulator nem elegendo az utasitas sorozat vegrehajtasahoz!")
        print("5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", db4)
else:
    print("5/a. Az utasitas sorozat vegrehajtasahoz melyik akkumulatorra van szukseg? Nem tortent elmozdulas!")
    print("5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", len(list))
db5 = 2
for i in range(len(short_list)-1):
    if short_list[i] == short_list[i+1]:
        db5 = db5 +1 + 1               # innen az utolso 1-es nem biztos hogy kell
    else:
        db5 = db5 +2 + 1               # innen az utolso 1-es nem biztos hogy kell
if len(list) > 0:
    if db5 <= 100:
        print("#Energia takarekos# 5/a. Az utasitas sorozat vegrehajtasahoz melyik akkumulatorra van szukseg? A 100 egysegnyi energiaju akkumulator is elegendo.")
        print("#Energia takarekos# 5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", db5)
    if 100 < db5 < 1000:
        print("#Energia takarekos# 5/a. Az utasitas sorozat vegrehajtasahoz melyik akkumulatorra van szukseg? A 1000 egysegnyi energiaju akkumulatorra van szukseg.")
        print("#Energia takarekos# 5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", db5)
    if 1000 < db5 < 1100:
        print("5/a. Az utasitas sorozat vegrehajtasahoz mind a 100 mind pedig az 1000 egysegnyi energiaju akkumulatorra szukseg van!")
        print("5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", db5)
    if db5 > 1100:
        print("5/a. Sem a 100 sem pedig az 1000 egysegnyi energiaju akkumulator nem elegendo az utasitas sorozat vegrehajtasahoz!")
        print("5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", db5)

else:
      print("#Energia takarekos# 5/a. Az utasitas sorozat vegrehajtasahoz melyik akkumulatorra van szukseg? Nem tortent elmozdulas!")
      print("#Energia takarekos# 5/b. Az utasitas sorozat vegrehajtasahoz szukseges egysegnyi energia:", len(list))
vegeido = (datetime.datetime.now())


ciklus = vegeido - kezdoido
print("ciklusido:", ciklus , "(ora:perc:masodperc)")



