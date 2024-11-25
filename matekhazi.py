import math
pi = math.pi
lista = ["kocka", "téglatest", "henger", "gúla", "csonka gúla", "kúp", "csonka kúp", "gömb", "tetraéder"]
def alakzat_kerdes():         
    while True:
        valasz = input("Milyen alakzatot szeretnél kiszámoltatni? ")
        if valasz not in lista:
            print("Kérlek a listából válassz! ")
        else:
            break
    return valasz

#kocka
def kocka_terfogat(oldal):
        return oldal ** 3
def kocka_felszin(oldal):
        return oldal ** 2 * 6

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

def gula_terulet(gula_oldal):
        return gula_oldal ** 2
def gula_palast_terulet(gula_oldal, gula_magassag):
        return 4 * gula_oldal * gula_magassag / 2 

def gula_terfogat(terulet, gula_magassag):
        return terulet * gula_magassag / 3
def gula_felszin(terulet, palast_terulet):
        return terulet + palast_terulet

#csonka gúla

#kúp 
def kup_terfogat(kup_sugar, kup_magassag):
        return kup_sugar ** 2 * pi * kup_magassag / 3
def kup_felszin(kup_sugar, kup_oldal):
        return kup_sugar ** 2 * pi + kup_sugar * pi * 3

test = alakzat_kerdes()
if test == 'kocka':
    oldal = input('Add meg az oldal méretét:')
    print('A kocka térfogata:', kocka_terfogat, 'cm3')
    print('A kocka felszíne:', kocka_felszin, 'cm2')

if test == 'téglatest':
    print('A téglatest térfogata:', teglatest_terfogat(10,20,30), 'cm3')
    print('A téglatest felszíne:', teglatest_felszin(10,20,30), 'cm2')

if test == 'henger':
    print('A henger térfogata', henger_terfogat(15, 20),'cm3')
    print('A henger felszíne', henger_felszin(15, 20), 'cm2')

if test == 'gúla':
    print('A gúla térfogata', gula_terfogat(15,20),'cm3')
    print('A gúla felszíne', gula_felszin(15,20),'cm2')

if test == 'kúp':
    print('A kúp térfogata', kup_terfogat(),'cm3')
    print('A kúp felszíne', kup_felszin(),'cm2')

"""def readFloat(s):
     while True:
            try:
                print(s,end=" ")
                value = float(input())
                return value
            except ValueError:
                print ("Please enter the price with 2 decimal places")"""
"""r = readFloat("Add meg az alapkör sugarát: ") #alapkör sugara
M = readFloat("Add meg a kúp magasságát: ") #kúp magassága
a = input("Add meg az alkotó hosszát: ") #alkotó hossza
A = input("Add meg a kúp felszínét: ") #felszín
V = input("Add meg a kúp térfogatát: ") #térfogat"""