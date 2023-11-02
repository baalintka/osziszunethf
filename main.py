import feladatok
#feladatok.feladat1()
#feladatok.feladat2(2450)
#feladatok.feladat3(1534)
szam:int = int(input("Kérem ajdon meg egy egész számot"))

while 0 < szam:
    ujszam = szam % 10
    print(ujszam)
    print(szam)

    szam //= 10
