from modul import *

while True:
    print("""Menu:
Tõlge eesti keelest vene keelde=> 1
Tõlge vene keelest eesti keelde=> 2
Lisa sõna eesti sõnaraamatusse=> 3
Muuda sõna=> 4
Teadmiste kontroll=> 5
Sõnastiku väljund=> 6
Välja=> 0

Sisestage number 1-6""")
    try:

        V=int(input("=>"))
        if V>6:
            raise ValueError
        elif V==1:
            tõlge_ev()
            jätka()
        elif V==2:
            tõlge_ve()
            jätka()
        elif V==3:
            lisa_sõna()
            jätka()
        elif V==4:
            muuda_sõna()
            jätka()
        elif V==5:
            teadmise_kontrol()
            jätka()
        elif V==6:
            Sõnastiku_väljund()
            jätka()
        elif V==0:
            exit()
        
    except ValueError:
        print("Sisestage number 1-6")





