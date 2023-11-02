''' 1.	Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!    '''
def feladat1():
    szam:int = int(input("Kérem ajdon meg egy egész számot"))
    while szam < 200 or szam > 920:
        szam: int = int(input("Kérem ajdon meg egy egész számot"))
    szamosztva:int=szam/100
    print(round(szamosztva))
'''2.	Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne! használd hozzá az egész osztás operátorát - // ! 
pl: 123//10 =12  123%10=3
 '''
def feladat2(szam):
    egyesek:int=szam//1
    tizesek:int=szam//10
    szazasok:int=szam//100
    ezresek=szam//1000
    print(egyesek,tizesek,szazasok,ezresek)



def feladat3(szam):
    ujszam:int=0
    osszeg:int=0
    while 0 < szam:
        ujszam=szam%10
        osszeg+=ujszam

        szam//=10

    print("számjegyek összege: "+str(osszeg))