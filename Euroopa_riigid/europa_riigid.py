from modul import *

while True:
    print("""Menu:
Riig/Pealinn=> 1
Lisa sõnastikusse=> 2
Vigade parandamine=> 3
Teadmise kontroll=> 4
Loetlege riigid ja nende pealinnad=> 5
Välja=> 0

Sisestage number 1-5""")
    try:

        V=int(input("=>"))
        if V>5:
            raise ValueError
        elif V==1:
            Riig_pealinn()
            jätka()
        elif V==2:
            lisa_sõna()
            jätka()
        elif V==3:
            parandamine()
            jätka()
        elif V==4:
            teadmise_kontrol()
            jätka()
        elif V==5:
            Sõnastiku_väljund()
            jätka()   
        elif V==0:
            exit()
        
    except ValueError:
        print("Sisestage number 1-5")




