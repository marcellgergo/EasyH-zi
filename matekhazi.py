import math
pi = math.pi
lista = ["kocka", "téglatest", "henger", "gúla", "kúp", "gömb"]
def szamadas(s):
     while True:
            try:
                print(s,end=" ")
                value = float(input())
                return value
            except ValueError:
                print ("Kérlek, számot adj meg!")

def alakzat_kerdes():         
    while True:
        valasz = input("Milyen alakzatot szeretnél kiszámoltatni? ")
        if valasz not in lista:
            print("Kérlek a listából válassz! ")
        else:
            break
    return valasz

#kocka
def kocka_terfogat(kocka_oldal):
        return kocka_oldal ** 3
def kocka_felszin (kocka_oldal):
        return kocka_oldal ** 2 * 6

#téglatest
def teglatest_terfogat(oldal1, oldal2, oldal3):
        return oldal1 * oldal2 * oldal3
def teglatest_felszin(oldal1, oldal2, oldal3):
        return 2 * (oldal1*oldal2 + oldal2*oldal3 + oldal1*oldal3)

#henger
def henger_sugar(atmero):
        return atmero / 2
def henger_terfogat(sugar, magassag):
        return sugar ** 2 * pi * magassag
def henger_felszin(sugar, magassag):
        return sugar ** 2 * pi + 2 * sugar * pi * magassag

#gúla
def gula_magassag(gula_oldal, alap):
        magassag2 = gula_oldal ** 2 + alap ** 2
        return magassag2 // 2

def terulet(gula_oldal):
        return gula_oldal ** 2
def palast_terulet(gula_oldal, gula_magassag):
        return 4 * gula_oldal * gula_magassag / 2 

def gula_terfogat(gula_terulet, gula_magassag):
        return gula_terulet * gula_magassag / 3
def gula_felszin(terulet, palast_terulet):
        return terulet + palast_terulet

#kúp 
def kup_terfogat(kup_sugar, kup_magassag):
        return kup_sugar ** 2 * pi * kup_magassag / 3
def kup_felszin(kup_sugar, kup_oldal):
        return kup_sugar ** 2 * pi + kup_sugar * pi * kup_oldal

#gömb
def gömb_terfogat(gömb_sugar):
        return 4 * gömb_sugar ** 3 * pi / 3
def gömb_felszin(gömb_sugar):
        return 4 * gömb_sugar ** 2 * pi

test = alakzat_kerdes()
if test == 'kocka':
    oldal = szamadas('Add meg az oldal hosszát:')
    print = szamadas('Add meg a gúla oldalának hosszát:')
if test == 'téglatest':
    oldal1 = szamadas('Add meg az első oldal hosszát:')
    oldal2 = szamadas('Add meg a második oldal hosszát:')
    oldal3 = szamadas('Add meg a harmadik oldal hosszát:')
    print('A téglatest térfogata:', teglatest_terfogat(oldal1, oldal2, oldal3), 'cm3')
    print('A téglatest felszíne:', teglatest_felszin(oldal1, oldal2, oldal3), 'cm2')

if test == 'henger':
    sugar = szamadas('Add meg a henger sugarát:')
    magassag = szamadas('Add meg a henger magasságát:')
    if sugar == 0:
           atmero = szamadas('Add meg a henger átmérőjét:')
    print('A henger térfogata', henger_terfogat(sugar or atmero/2, magassag),'cm3')
    print('A henger felszíne', henger_felszin(sugar or atmero/2, magassag), 'cm2')

if test == 'gúla':
    gterulet = szamadas('Add meg a gúla területét:')
    gpalast_terulet = szamadas('Add meg a gúla palástjainak a területét')
    magassag = szamadas('Add meg a gúla magasságát:')
    if gterulet == 0:
        goldal = szamadas('Add meg a gúla oldalának hosszát:')
        gmagassag = szamadas('Add meg a gúla magasságát(területhez):')
    if gpalast_terulet == 0:
        magassag2 = szamadas('Add meg a gúla palastjának a magasságát:')
        goldal = szamadas('Add meg a gúla palástjának oldalának hosszát:')

    print('A gúla térfogata', gula_terfogat(gterulet or goldal**2, magassag),'cm3')
    print('A gúla felszíne', gula_felszin(gterulet or goldal**2, gpalast_terulet or 4*goldal*gmagassag/2),'cm2')

if test == 'kúp':
    
    print('A kúp térfogata', kup_terfogat(),'cm3')
    print('A kúp felszíne', kup_felszin(),'cm2')

if test == 'gömb':
    print('A gömb térfogata:', gömb_terfogat(10),'cm3')
    print('A gömb felszíne:', gömb_felszin(10),'cm2')

"""r = readFloat("Add meg az alapkör sugarát: ") #alapkör sugara
M = readFloat("Add meg a kúp magasságát: ") #kúp magassága
a = input("Add meg az alkotó hosszát: ") #alkotó hossza
A = input("Add meg a kúp felszínét: ") #felszín
V = input("Add meg a kúp térfogatát: ") #térfogat"""