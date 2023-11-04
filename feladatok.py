''' 	Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!    '''
import math


def feladat1():
    szam:int = int(input("Kérem ajdon meg egy egész számot 200 és 920 között"))
    while szam < 200 or szam > 920:
        szam=int(input("Rossz,kérem ajdon meg egy egész számot 200 és 920 között"))
    szamosztva:float=szam/100
    print("Első számjegy: ",int(szamosztva))


'''	Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne! használd hozzá az egész osztás operátorát - // ! 
pl: 123//10 =12  123%10=3
 '''
def feladat2(szam):

    egyesek:int=szam//1
    tizesek:int=szam//10
    szazasok:int=szam//100
    ezresek:int=szam//1000


    print(f"egyesek: {egyesek} tizesek: {tizesek} százasok: {szazasok} ezresek: {ezresek}")




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

            print(f"{i*v:>4}",end="")
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

'''6.	A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!'''
def feladat6():

    szam:float = float(input("Kérem adjon meg egy valós számot"))
    while szam < 0:
        szam = float(input("Kérem adjon meg egy valós számot"))
    negyzetgyok: float =0
    negyzetgyok=math.sqrt(szam)
    print(round(szam)," Négyzetgyöke, kerekítve :",(round(negyzetgyok)))

'''	A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív,
 akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, 
területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!'''
def feladat7():

    a: float = float(input("Kérem adjon meg egy valós számot"))
    b: float = float(input("Kérem adjon meg egy valós számot"))
    while a < 0 or b < 0:
        print("Hiba: a téglalap oldalai nem pozitívak!")
        a: float = float(input("Kérem adjon meg egy valós számot"))
        b: float = float(input("Kérem adjon meg egy valós számot"))
    kerulet:float=2*(a+b)
    print("Kerület: ",str(round(kerulet)))
    terulet:float=a*b
    print("Terület: ",str(round(terulet)))


'''Írj metódust, mely neveket kér a felhasználótól addig amíg a „@” jelet nem kapja. 
Hány nevet adott meg a felhasználó? 
Van-e benne A betűvel kezdődő név? 
Melyik a leghosszabb név? 
'''
def feladat8():
    hossz:int=0
    leghosszabbnev:str=""
    van:bool=False
    szamlalo:int=0
    nev:str=input("Adjon meg egy nevet, (befejezéshez -->@)")
    szamlalo+=1
    while nev != "@":
        nev = input("Adjon meg egy nevet, (befejezéshez -->@)")
        szamlalo += 1
        if len(nev) > hossz:
            hossz=len(nev)
            leghosszabbnev=nev
        if nev[0] == "A".lower():
            van=True
    if van:
        print("Van benne 'A' kezdőbetűs név")
    else:
        print("Nincs benne 'A' kezdőbetűs név")
    print(str(szamlalo - 1),"Nevet adott meg")
    print("Leghosszabb név betűinek száma: ",str(hossz))
    print("Leghosszabb név: ",leghosszabbnev)


'''	Írj metódust, mely egy érmedobás eredményét kéri be a felhasználótól 10-szer egymás után! A felhasználó minden lépésben a „f” vagy  „i” betűket kell megadjon. Addig kérd be a jeleket, amíg jó jelet nem ad meg. 
Hányszor adott meg „f” betűt? 
Mekkora a leghosszabb f sorozat? 
'''
def feladat9():
    leghosszabbsorozat:int=0
    sorozat:int=0
    fbetu:int=0
    i:int=0


    while i!=10:
        dobas: str = input("Adja meg az érmedobás eredményét f vagy i: ")
        while dobas!="f" and dobas!="i":
            dobas = input("Adja meg az érmedobás eredményét rendesen f vagy i: ")
        if dobas=="f".lower():
            fbetu+=1
            sorozat+=1
            print(dobas)
            i+=1
        if dobas=="i".lower():
            if sorozat > leghosszabbsorozat:
                leghosszabbsorozat=sorozat
            sorozat=0
            print(dobas)
            i+= 1


    print(str(fbetu),".db f-et adott meg ")
    print("Leghosszabb  f sorozat: ",str(leghosszabbsorozat))

def feladat10():
    pass