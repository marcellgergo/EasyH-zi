import math
pi = math.pi
lista = ["kocka", "téglatest", "henger", "gúla", "kúp", "gömb", "tetraéder"]
def alakzat_kerdes():         
    while True:
        valasz = input("Milyen alakzatot szeretnél kiszámoltatni? ")
        if valasz not in lista:
            print("Kérlek a listából válassz! ")
        else:
            break
    return valasz


test = alakzat_kerdes()
if test == 'kocka':
    def kocka_oldal(felszin, terfogat):
        return felszin / 6
    def kocka_terfogat(oldal):
        return oldal ** 3
    def kocka_felszin(oldal):
        return oldal ** 2 * 6
  
    print('A kocka térfogata:', kocka_terfogat(15), 'cm3')
    print('A kocka felszíne:', kocka_felszin(15), 'cm2')

if test == 'téglatest':
    def teglatest_oldal1(felszin, terfogat, oldal2, oldal3):
        return terfogat / oldal2 / oldal3
    def teglatest_oldal2(felszin, terfogat, oldal1, oldal3):
        return terfogat / oldal1 / oldal3
    def teglatest_oldal3(felszin, terfogat, oldal1, oldal2):
        return terfogat / oldal1 / oldal2

    def teglatest_terfogat(oldal1, oldal2, oldal3):
        return oldal1 * oldal2 * oldal3
    def teglatest_felszin(oldal1, oldal2, oldal3):
        return 2 * (oldal1*oldal2 + oldal2*oldal3 + oldal1*oldal3)

    print('A téglatest térfogata:', teglatest_terfogat(15), 'cm3')
    print('A téglatest felszíne:', teglatest_felszin(15), 'cm2')


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