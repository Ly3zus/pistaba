from random import randint

def pista_siras():
    osszsirasok=0
    for nap in range(90):
        print('\t\033[1;32;40mPista bácsi 3 hónapos koráig nem iszik!')
        sirasokszama=randint(0, 15)
        osszsirasok+=sirasokszama

        if sirasokszama == 0:
            print(f'\033[1;32;40mPistike {sirasokszama} alkalommal bőgött ma.')
        else:
            print(f'\033[1;40;40mPistike {sirasokszama} alkalommal bőgött ma.')
    
    return osszsirasok

def pista_eletereje(osszsirasok):
    osszesen=0
    napokjozanon=0
    ivott=False
    osszesenivasnelkul=0
    
    for nap in range(90,25185):
        if nap>=25100:
            print('\033[1;31;40mPista bácsi elhunyt.')
            print(f'{osszsirasok} alkalommal sírt összesen.')
            print(f'{osszesenivasnelkul} liter pálinkát készített élete során Pista bá.')
            break
        
        if not ivott:
            maifozet=randint(1, 5)
            osszesen+=maifozet
            osszesenivasnelkul+=maifozet
            if randint(1, 5)==1:  
                ivott=True
                osszesen-=1
                print(f'\033[1;37;40m{nap}. nap: {maifozet} liter készült')
                print('\t\033[1;31;40mBe fog baszni...')
                napokjozanon=0
                if randint(1, 10000)==1:
                    print('\033[1;31;40mPista bácsi elhunyt alkoholmérgezésben.')
                    break
                elif randint(1, 20000) == 1:
                    print('\033[1;31;40mPista bácsi elhunyt agyvérzés miatt.')
                    break
                elif randint(1, 1000000) == 1:
                    print('\033[1;31;40mPista bácsi elhunyt, mert a felesége agyonverte az alkoholfüggősége miatt.')
                    break
            else:
                print(f"\033[1;37;40m{nap}. nap.")
                print("\t\033[1;32;40mPista bácsi leszokóban van az alkoholból!")
                napokjozanon += 1
                print(f'\t\033[1;32;40m{napokjozanon} napja leszokóban van Pista bácsi!')
                print(f'------> összesen: {osszesen} liter van raktáron!')
        else:
            print(f"\033[1;37;40m{nap}. nap.")
            print("\033[1;37;40mMa nem készült pálinka, mert Pista bácsi be van baszva mint a ló!")
            ivott=False
