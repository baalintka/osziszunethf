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


'''Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre. 
PL. 324 -> „324 számjegyeinek összege: 9”
'''
def feladat3(szam):
    ujszam:int=0
    osszeg:int=0
    while 0 < szam:
        ujszam=szam%10
        osszeg+=ujszam

        szam//=10

    print("számjegyeinek összege: "+str(osszeg))

'''irj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj hozzá formázott kiiratást!”
'''
def feladat4():

    i:int=1
    v:int=1
    while v != 11:
        while  i!=11:
            print(i*v,end="  ")
            i+=1
        i=1
        print("")
        v+=1
'''1.feladat:	Egy a természettel  Vadászati és Természeti Világkiállításon téged bíztak meg, hogy egy kihelyezett információs tábla részműködését leprogramozd!
A felhasználónak be kell gépelnie melyik szektort szeretné megnézni, a te programod pedig kiírja az ott található kiállítás nevét.
•	A esetén Nemzetközi Csarnok, World Conservation Forum 2021
•	B és E esetén a Kereskedelmi Csarnok felirat jelenjen meg
•	C esetén Konferencia-központ Innovációs Showroom
•	D esetén Hal, Víz és Ember
•	F esetén Hagyományos Vadászati Módok Csarnoka
•	G Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás
•	H esetben Központi Magyar Kiállítás
•	Minden egyéb nem szám adatra írja ki, hogy forduljon a pénztárhoz.
'''
def feladat5():
    szoveg:str=input("Kérem adja meg melyik szektort szeretné megnézni")
    while szoveg.isnumeric():
        szoveg=input("Kérem adja meg melyik szektort szeretné megnézni")

    if szoveg =="A".lower():
        print("Nemzetközi Csarnok, World Conservation Forum 2021")
    elif (szoveg =="B".lower()) or (szoveg =="E".lower()):
        print("Kereskedelmi csarnok")
    elif szoveg =="C".lower():
        print("Konferencia-központ Innovációs Showroom")
    elif szoveg =="D".lower():
        print("Hal, Víz és Ember")
    elif szoveg =="F".lower():
        print("Hagyományos Vadászati Módok Csarnoka")
    elif szoveg =="G".lower():
        print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
    elif szoveg =="H".lower():
        print("Központi Magyar Kiállítás")
    else:
        print("Forduljon a pénztárhoz")