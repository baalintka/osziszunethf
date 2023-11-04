
import math

''' 	Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!    '''
def feladat1():
    szam:int = int(input("Kérem ajdon meg egy egész számot 200 és 920 között"))
    while szam < 200 or szam > 920:
        szam=int(input("Rossz,kérem ajdon meg egy egész számot 200 és 920 között"))
    szamosztva:float=szam/100
    print("Első számjegy: ",int(szamosztva))



'''	Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne!'''
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
    eredeti:int=szam
    ujszam:int=0
    osszeg:int=0
    while 0 < szam:
        ujszam=szam%10
        osszeg+=ujszam

        szam//=10

    print(eredeti,"Számjegyeinek összege: "+str(osszeg))

'''irj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá!”
'''
def feladat4():
    print("   10x10-es alapú szorzótábla:)")
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
        szam = float(input("Hiba! Kérem adjon meg egy valós számot"))
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
    if len(nev) > hossz:
        hossz = len(nev)
        leghosszabbnev = nev
    if nev[0] == "A".lower():
        van = True
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
            i+=1
            if i==10:
                print(str(fbetu), ".db f-et adott meg ")
                print("Leghosszabb  f sorozat: ", str(sorozat))
        if dobas=="i".lower():
            if sorozat > leghosszabbsorozat:
                leghosszabbsorozat=sorozat
            sorozat=0
            i+= 1
            if i==10:
                print(str(fbetu), ".db f-et adott meg ")
                print("Leghosszabb  f sorozat: ",str(leghosszabbsorozat))






'''Irj programot amely beolvas egy pozitív egész számot, és ,megmondja hogy tökéletes szám-e(A tökéletes számok azok, melyek osztóinak összege egyenlő a szám
 kétszeresével.'''
def feladat10():
    szam:int =int(input("Kérem adjon meg egy pozitív egész számot"))
    i:int=1
    osztoosszeg:int=0
    while i <= szam:
        if szam%i==0:
            osztoosszeg+=i
            i+=1
        else:
            i+=1

    if (szam*2)==osztoosszeg:
        print("Ez egy tökéletes szám")
    else:
        print("Ez nem egy tökéletes szám")


''' Írj metódust, ami paraméterében kap két számot, és kiírja a két szám legnagyobb közös osztóját!'''
def feladat11(a,b):
    segedvalt:int=1
    if a<b:

        if a ==1:
            segedvalt=a
        else:
            segedvalt=a-1

        while not (a%segedvalt==0 and b%segedvalt==0):

            segedvalt-=1
        if segedvalt==1:
            print(a,b," legnagyobb közös osztója: ",a)
        else:
            print(a,b," legnagyobb közös osztója: ", segedvalt)


    elif b<a:
        if b ==1:
            segedvalt=b
        else:
            segedvalt=b-1

        while not (b%segedvalt==0 and a%segedvalt==0):

            segedvalt-=1
        if segedvalt == 1:
            print(a, b, " legnagyobb közös osztója: ", b)
        else:
            print(a, b, " legnagyobb közös osztója: ", segedvalt)


    if a==b:
        print(a,b," legnagyobb közös osztója: ", b)


'''Írj metódust, ami paraméterében kap két számot, és kiírja a legkisebb közös többszörösüket!
'''
def feladat12(a,b):
    segedvalt:int=1
    if a < b:
        segedvalt=b+1
        while not (segedvalt%b==0 and segedvalt%a==0):

            segedvalt+=1
        print(a,b,"Legkisebb közös többszöröse: ",segedvalt)
    elif b < a:
        segedvalt = a + 1
        while not (segedvalt % a == 0 and segedvalt % b == 0):

            segedvalt += 1
        print(a,b,"Legkisebb közös többszöröse: ",segedvalt)
    if a==b:
        c:int=a*b
        print(a,b,"Legkisebb közös többszöröse: ",c)


'''Egy hétfői napon az 1-es csoportnak 9 órája van. Az első órában a teljesítményük 90%-át képesek nyújtani. 
A 2-3. órában már kissé éhesek, és csupán 60%-os a munkabírásuk. A 4-7. órában szerencsére programozást tanulnak, 
így némiképp javul a hatékonyságuk (70%), a 8-9. órában azonban már újra lecsökken (50%).
Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak; jelezz hibát, 
ha nem ebben az intervallumban lévő számot kapsz, pl. “Ez már tényleg túlzás.”). Példa egy esetre: Be: 3, Ki: “Még bírjuk (60%).”   -  
nem kell tesztfüggvényeket írni, de az alábbi táblázat alapján ellenőrizzétek a munkátokat!
'''
def feladat13(szam):
    if  szam < 0:
        print("Hiba")
    elif szam >= 10:
        print("Ez már tényleg túlzás.")
    elif szam==0:
        print("Be se jövök!")
    elif szam ==1:
        print("Még 90% on vagyunk!")
    elif szam ==2 or szam==3:
        print("Még bírjuk (60%)")
    elif szam ==4 or szam==5 or szam==6 or szam==7:
        print("Progit tanulunk, töltődünk! 70%")
    elif szam ==8 or szam==9:
        print("Lassan nem bírjuk tovább! 50%")

'''5.	Az egyik diák (legyen Márti a neve) az alábbi algoritmus alapján tevékenykedik az órákon:
a.	hétfőn alszik az összes órán,
b.	kedden csak hittan órán figyel,
c.	programozás órán dolgozik, de csak szerdán
d.	csütörtökön minden órán figyel, mert jó kedve van (aznap szokott moziba menni),
e.	pénteken a hétvégéről ábrándozik, így csak félig figyel minden aznapi órán,
f.	a többi óráról semmit nem tudunk.
Írj metódsut, melynek  2 bemenő prarmétere van (nap neve, óra neve) és tájékoztatást ad Márti állapotáról.
'''

def feladat14(nap,ora):
    if nap == "hétfő":
        print("alszik")
    elif nap=="kedd" and ora!="hittan":
        print("alszik")
    elif nap=="kedd" and ora=="hittan":
        print("figyel")
    elif nap=="szerda" and ora!="programozás":
        print("nincs info")
    elif nap == "szerda" and ora == "programozás":
        print("dolgozik")
    elif nap=="csütörtök":
        print("figyel")
    elif nap=="péntek":
        print("félig van jelen")
    else:
        print("nincs info")

