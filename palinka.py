from random import randint

pistabacsinapjainakszama=0

for i in range(0,90):
    osszsirasok=0
    pistabacsinapjainakszama+=1
    print('\t\033[1;32;40mPista bácsi 3 hónapos koráig nem iszik!')
    sirasokszama=randint(0,15)
    osszsirasok+=sirasokszama
    
    if sirasokszama==0:
        print(f'\033[1;32;40mPistike {sirasokszama} alkalommal bőgött ma.')
    else:
        print(f'\033[1;40;40mPistike {sirasokszama} alkalommal bőgött ma.')
    

napokjozanon=0
osszesen=0
ivott=False
osszesenivasnelkul=0
for i in range(90,25185):
    pistabacsinapjainakszama+=1
    if pistabacsinapjainakszama>=25100:
        print('\033[1;31;40mPista bácsi elhunyt.')
        print(f'{osszsirasok} alkalommal sírt összesen.')
        print(f'{osszesenivasnelkul} liter pálinkát készített élete során Pista bá.')
        break
    if ivott==False:
        maifozet=randint(1,5)
        osszesen+=maifozet
        osszesenivasnelkul+=maifozet
        if randint(1,5)==1:
            ivott=True
            osszesen-=1
            print(f'\033[1;37;40m{i}. nap: {maifozet} liter készült')
            print('\t\033[1;31;40mBe fog baszni...')
            napokjozanon=0
            if randint(1,10000)==1:
                print('\033[1;31;40mPista bácsi elhunyt alkoholmérgezésben.')
                print(f'{osszsirasok} alkalommal sírt összesen.')
                print(f'{osszesenivasnelkul} liter pálinkát készített élete során Pista bá.')
                break
            elif randint(1,20000)==1:
                print('\033[1;31;40mPista bácsi elhunyt agyvérzés miatt.')
                print(f'{osszsirasok} alkalommal sírt összesen.')
                print(f'{osszesenivasnelkul} liter pálinkát készített élete során Pista bá.')
                break
            elif randint(1,1000000)==1:
                print('\033[1;31;40mPista bácsi elhunyt mivel a felesége agyonverte az alkoholfüggősége miatt.')
                print(f'{osszsirasok} alkalommal sírt összesen.')
                print(f'{osszesenivasnelkul} liter pálinkát készített élete során Pista bá.')
                break
        else:
            print(f"\033[1;37;40m{i}. nap.")
            print("\t\033[1;32;40mPista bácsi leszokóban van az alkoholból!")
            napokjozanon+=1
            print(f'\t\033[1;32;40m{napokjozanon} napja leszokóban van Pista bácsi!')
            print(f'------> összesen: {osszesen} liter van raktáron!')
    else:
        print(f"\033[1;37;40m{i}. nap.")
        print(f"\033[1;37;40mMa nem készült pálinka mert Pista bácsi be van baszva mint a ló!")
        ivott=False
    