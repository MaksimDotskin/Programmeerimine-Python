print("""Tere, Mängime kivi, paberi, kääride mängu. Reeglid on väga lihtsad: 
Paber lööb kivi (paber mähib kivi).
Kivi võidab käärid (kivi tuhmub või lõhub käärid).
Käärid peksid paberit (käärid lõikasid paberit).
Alustame""")

winners=[]

while True:
    modeSelection=input("Kas tahate mängida arvutiga(sisesta 1) või teistega mängijaga?(sisesta 2)/Kui tahate lõpetada sisestage-'3'=> ")
    if modeSelection == "1":
        print("Te valitsite mängida arvutiga")
        name1=input("Sissestage oma nimi=> ")
        while True:
            while True:
                gamechoises=("kivi"), ("paber"), ("käärid")
                gamechoise=input("Vali kas kivi/paber/või käärid?=> ")

                if gamechoise==("kivi"):
                    gamechoise=1
                    break
                if gamechoise==("paber"):
                    gamechoise=2
                    break
                if gamechoise==("käärid"):
                    gamechoise=3
                    break
                else:
                    print("Sisestage täpsemalt")


            import random

            pcchoise= random.choice(gamechoises)
            
            if pcchoise==("kivi"):
                pcchoise=1
                
            if pcchoise==("paber"):
                pcchoise=2
            if pcchoise==("käärid"):
                pcchoise=3

            if pcchoise==gamechoise:
                resault=("Arvuti ka valis sama mis te- Viik")
                winner=("Mitte keegi")
                
            if pcchoise==1 and gamechoise==2:
                resault=("Arvuti valis kivi- Võit")
                winner=name1
            if pcchoise==1 and gamechoise==3:
                resault=("Arvuti valis kivi- Lüüa")
                winner="Arvuti"
            if pcchoise==2 and gamechoise==1:
                resault=("Arvuti valis paber- Lüüa")
                winner="Arvuti"
            if pcchoise==2 and gamechoise==3:
                resault=("Arvuti valis paber- Võit")
                winner=name1
            if pcchoise==3 and gamechoise==1:
                resault=("Arvuti valis käärid- Võit")
                winner=name1
            if pcchoise==3 and gamechoise==2:
                resault=("Arvuti valis käärid- Lüüa")
                winner="Arvuti"

            print(resault)
            print("Võtjate nimekiri:")

            winners.append(winner)

            print(winners)

            repeat=input("Kas tahate mängiga veel?(j/e)=> ")
            if repeat!=("j"):
                break    
    
    if modeSelection == "2":
            print("Te valitsite teistega mängijaga ")
            player1=input("Mängija 1- Sissestage oma nimi=> ")
            player2=input("Mängija 2- Sissestage oma nimi=> ")
            while True:

                while True:
                    gamechoise1=input("Mängija 1- Vali kas kivi/paber/või käärid?=> ")

                    if gamechoise1==("kivi"):
                        gamechoise1=1
                        break
                    if gamechoise1==("paber"):
                        gamechoise1=2
                        break
                    if gamechoise1==("käärid"):
                        gamechoise1=3
                        break
                    else:
                        print("Sisestage täpsemalt")

                while True:
                    gamechoise2= input("Mängija 2- Vali kas kivi/paber/või käärid?=> ")
                    
                    if gamechoise2==("kivi"):
                        gamechoise2=1
                        break
                    if gamechoise2==("paber"):
                        gamechoise2=2
                        break
                    if gamechoise2==("käärid"):
                        gamechoise2=3
                        break
                    else:
                        print("Sisestage täpsemalt")

                if gamechoise2==gamechoise1:
                    resault=("Viik")
                    winner=("Mitte keegi")
                if gamechoise2==1 and gamechoise1==2:
                    resault=("Mängija 1 Võitis")
                    winner=player1
                if gamechoise2==1 and gamechoise1==3:
                    resault=("Mängija 2 Võitis")
                    winner=player2
                if gamechoise2==2 and gamechoise1==1:
                    resault=("Mängija 2 Võitis")
                    winner=player2
                if gamechoise2==2 and gamechoise1==3:
                    resault=("Mängija 1 Võitis")
                    winner=player1
                if gamechoise2==3 and gamechoise1==1:
                    resault=("Mängija 1 Võitis")
                    winner=player1
                if gamechoise2==3 and gamechoise1==2:
                    resault=("Mängija 2 Võitis")
                    winner=player2

                print(resault)

                print("Võtjate nimekiri:")

                winners.append(winner)

                print(winners)

                repeat=input("Kas tahate mängiga veel?(j/e)=> ")
                if repeat!=("j"):
                    break    
    
    if modeSelection == "3":
        break