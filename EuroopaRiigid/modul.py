def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def jätka():
    print("Kas tahate jätka? j/e")
    V=input("=>")
    if V!="j":
        exit()




def Riig_pealinn():
    riigide_list:list=loe_failist("riigid_pealinnd.txt")
    riigid=[]
    pealinnad=[]
    for i in riigide_list:
        data = i.strip().split("-")
        riigid.append(data[0])
        pealinnad.append(data[1])
    while True:
        sõna=input("Sisestage riig või pealinn=> ")

        if sõna in riigid:
            ind=riigid.index(sõna)
            print(sõna,"pealinn on:",pealinnad[ind])
            print("Kas tahate veel kord? j/e")
            V=input("=> ")
            if V!="j":
                break
        
        if sõna in pealinnad:
            ind=pealinnad.index(sõna)
            print(sõna,"on:",riigid[ind],"pealinn")
            print("Kas tahate veel kord? j/e")
            V=input("=> ")
            if V!="j":
                break
        
        else:
            print("Sellist sõna nimekirjas pole")
    
def lisa_sõna():
    with open('riigid_pealinnd.txt', 'a', encoding='utf-8') as f:
        uus_riig=input("Sisestage uus riig=> ")
        uus_pealinn=input("Sisestage tema pealinn=> ")
        uus_kirja=uus_riig+"-"+uus_pealinn

        f.write(uus_kirja + '\n')
    print("Teie riig ja pealinn on lisanud")

def Sõnastiku_väljund():
    print("Loetlege riigid ja nende pealinnad: ")
    with open('riigid_pealinnd.txt', 'r') as file:
                i=file.read()
                print(i)

def parandamine():
    with open('riigid_pealinnd.txt', 'r') as file:
                i=file.read()
                print(i)
                while True:
                    old_sõna=input("Sisestage riig või pealinn, mis tahate parandada=> ")

                    if old_sõna in i:
                        new_sõna=input("Sisestage paradatud=> ")
                        i=i.replace(old_sõna, new_sõna)

                        with open('riigid_pealinnd.txt', 'w') as file:
                            file.write(i)
                        break
                    else:
                        print("Sellist sõna nimekirjas pole")
    print("Viga on parandatud")
def teadmise_kontrol():
    riigide_list:list=loe_failist("riigid_pealinnd.txt")
    riigid=[]
    pealinnad=[]
    for g in riigide_list:
        data = g.strip().split("-")
        riigid.append(data[0])
        pealinnad.append(data[1])      


    while True:      
        print("""Valige režiimis:
Riig-pealinn kontrol=> 1
Pealinn-riig kontrol=> 2""")
        try:    
            V=int(input("=>"))
            if V>2 or V==0:
                raise ValueError
            if V==1:
                õiged = 0
                total = len(riigid)

                for i in range(total):
                    sõna = riigid[i]
                    vastus = input(f"Kirjuta '{sõna}' pealinn=> ")
                    if vastus.lower() == pealinnad[i].lower():
                        print("Õige!")
                        õiged += 1
                    else:
                        print(f"Vale! Õige vastus on '{pealinnad[i]}'")
                print(f"\nTeil oli {õiged} õiget vastust {total} küsimusest ({õiged/total*100:.2f}%).")
                break

            elif V==2:
                õiged = 0
                total = len(pealinnad)

                for i in range(total):
                    sõna = pealinnad[i]
                    vastus = input(f"Kirjuta, mis riigi pealinn on'{sõna}'?=> ")
                    if vastus.lower() == riigid[i].lower():
                        print("Õige!")
                        õiged += 1
                    else:
                        print(f"Vale! Õige vastus on '{riigid[i]}'")
                print(f"\nTeil oli {õiged} õiget vastust {total} küsimusest ({õiged/total*100:.2f}%).")
                break
        except ValueError:
            print("Sisestage 1-2")
