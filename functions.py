from random import randint


nev=(input("Mi legyen főhősünk neve? "))

if nev=="":
    nev="Pista"

def pista_siras():
    osszsirasok=0
    for nap in range(90):
        print(f'\t\033[1;32;40m{nev} bácsi 3 hónapos koráig nem iszik!')
        sirasokszama=randint(0, 15)
        osszsirasok+=sirasokszama

        if sirasokszama==0:
            print(f'\033[1;32;40m{nev} {sirasokszama} alkalommal bőgött ma.')
        else:
            print(f'\033[1;40;40m{nev} {sirasokszama} alkalommal bőgött ma.')
    
    return osszsirasok

def pista_eletereje(osszsirasok):
    osszesen=0
    napokjozanon=0
    ivott=False
    osszesenivasnelkul=0
    haverokkalivas=0
    
    for nap in range(90,25185):

        evek=nap//365
        maradeknap=nap%365

        if nap>=25100:
            print(f"\033[1;31;40m{evek} év, {maradeknap}. nap.")
            print(f'{nev} bácsi elhunyt.')
            print(f'{osszsirasok} alkalommal sírt összesen.')
            print(f'{osszesenivasnelkul} liter pálinkát készített élete során {nev}.')
            print(f'{nev} bácsi összesen {haverokkalivas} alkalommal ivot másokkal.')
            break

        if randint(1,20000)==1:
            print(f"\033[1;31;40m{evek} év, {maradeknap}. nap.")
            print(f'{nev} bácsi elhunyt alkoholmérgezésben.')
            print(f'{osszsirasok} alkalommal sírt összesen.')
            print(f'{osszesenivasnelkul} liter pálinkát készített élete során {nev}.')
            print(f'{nev} bácsi összesen {haverokkalivas} alkalommal ivot másokkal.')
            break
        elif randint(1,50000)==1:
            print(f"\033[1;31;40m{evek} év, {maradeknap}. nap.")
            print(f'{nev} bácsi elhunyt agyvérzés miatt.')
            print(f'{osszsirasok} alkalommal sírt összesen.')
            print(f'{osszesenivasnelkul} liter pálinkát készített élete során {nev}.')
            print(f'{nev} bácsi összesen {haverokkalivas} alkalommal ivot másokkal.')
            break
        elif randint(1,1000000)==1:
            print(f"\033[1;31;40m{evek} év, {maradeknap}. nap.")
            print(f'{nev} bácsi elhunyt, mert a felesége agyonverte az alkoholfüggősége miatt.')
            print(f'{osszsirasok} alkalommal sírt összesen.')
            print(f'{osszesenivasnelkul} liter pálinkát készített élete során {nev}.')
            print(f'{nev} bácsi összesen {haverokkalivas} alkalommal ivot másokkal.')
            break

        if not ivott:
            maifozet=randint(1,5)
            osszesen+=maifozet
            osszesenivasnelkul+=maifozet
            if randint(1,5)==1:  
                ivott=True
                osszesen-=2
                print(f'\033[1;37;40m{evek} év, {maradeknap} nap: {maifozet} liter készült')
                print('\t\033[1;31;40mBe fog baszni...')
                napokjozanon=0
            if randint(1,20)==1:
                ivott=True
                osszesen-=10
                print(f'\033[1;37;40m{evek} év, {maradeknap} nap: {maifozet} liter készült')
                print('\t\033[1;31;40mPista bácsi rájött hogy vannak barátjai is és ők is tudnak inni. Be fog baszni...')
                haverokkalivas+=1


            else:
                print(f"\033[1;37;40m{evek} év, {maradeknap} nap.")
                print(f"\t\033[1;32;40m{nev} bácsi leszokóban van az alkoholból!")
                napokjozanon+=1
                print(f'\t\033[1;32;40m{napokjozanon} napja leszokóban van {nev} bácsi!')
                print(f'------> összesen: {osszesen} liter van raktáron!')
        else:
            print(f"\033[1;37;40m{evek} év, {maradeknap} nap.")
            print(f"\033[1;37;40mMa nem készült pálinka, mert {nev} bácsi be van baszva mint a ló!")
            ivott=False