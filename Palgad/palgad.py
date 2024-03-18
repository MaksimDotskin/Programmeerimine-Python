from mymoodul import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","A",]

while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n 1-Lisa andmed\n 2-Kustuta andmed\n 3-Suuria palk\n 4 Мäiksem palk\n"))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=Lisa_andmed(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==2:
        inimesed,palgad=Kustutamine(inimesed,palgad)
    elif menu==3:
        palk,nimi=Suurim_palgad(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}'l")
    elif menu ==4:
        palk,nimi=Väisem_palgad(inimesed) (palgad)
        print(f"Väiksem palk on {palk} {nimi}'l")
    elif menu==5:
        inimesed,palgad=Sorteerimine(inimesed,palgad)
    elif menu==13:
        inimesed,palgad=kustuta(inimesed,palgad)
        print(inimesed,palgad)
