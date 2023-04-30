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

def tõlge_ev():
    rus:list=loe_failist("rus.txt")
    est:list=loe_failist("est.txt")
    Sõnastik=dict(zip(est, rus))
    print(est)
    while True:
        sõna=input("Sisestage sõna eesti keeles, mis tahate tõlkida=> ")
        tõlge=Sõnastik.get(sõna)

        if tõlge:
            print("Tõlkinud sõna:", tõlge)
            break
        else:
            print("Sellist sõna sõnastikus pole")
    

def tõlge_ve():
    rus:list=loe_failist("rus.txt")
    est:list=loe_failist("est.txt")
    Sõnastik=dict(zip(rus, est))
    print(rus)
    while True:
        sõna=input("Sisestage sõna vene keeles, mis tahate tõlkida=> ")
        tõlge=Sõnastik.get(sõna)

        if tõlge:
            print("Tõlkinud sõna:", tõlge)
            break
        else:
            print("Sellist sõna sõnastikus pole")

def lisa_sõna():
    with open('rus.txt', 'a', encoding='utf-8') as rus_file, \
         open('est.txt', 'a', encoding='utf-8') as est_file:
        uus_rus_sõna=input("Sisestage uus sõna vene keeles=> ")
        uus_est_sõna=input("Sisestage uus sõna eesti keeles=> ")
        rus_file.write(uus_rus_sõna + '\n')
        est_file.write(uus_est_sõna + '\n')


def Sõnastiku_väljund():
    print("Sõnad vene keeles:")
    rus:list=loe_failist("rus.txt")
    print(rus)
    print("Sõnad eesti keeles:")
    est:list=loe_failist("est.txt")
    print(est)



def muuda_sõna():
    
    print("""Muuda vene sõna=> 1
Muuda eesti sõna=> 2""")
    while True:            
        V=int(input("=>"))
        if V==1:
            with open('rus.txt', 'r') as rus_file:
                i=rus_file.read()
                print(i)
                while True:
                    old_sõna=input("Sisestage sõna mis tahate muuda=> ")

                    if old_sõna in i:
                        new_sõna=input("Sisestage muutanud sõna=> ")
                        i=i.replace(old_sõna, new_sõna)

                        with open('rus.txt', 'w') as rus_file:
                            rus_file.write(i)
                        break
                    else:
                        print("Sellist sõna sõnastikus pole")

            break
        elif V==2:
            with open('est.txt', 'r') as est_file:
                i=est_file.read()
                print(i)
                while True:

                    old_sõna=input("Sisestage sõna mis tahate muuda=> ")
                    if old_sõna in i:
                        new_sõna=input("Sisestage muutanud sõna=> ")
                        i=i.replace(old_sõna, new_sõna)

                        with open('est.txt', 'w') as est_file:
                            est_file.write(i)
                        break
                    else:
                        print("Sellist sõna sõnastikus pole")
            break
        else:
            print("Sisestage 1-2")

def teadmise_kontrol():
    print("""Eesti-vene kontrol=> 1
Vene-eesti kontrol=> 2""")
    while True:      

        V=int(input())
        if V==1:
            rus = loe_failist("rus.txt")
            est = loe_failist("est.txt")
            õiged = 0
            total = len(rus)
            for i in range(total):
                sõna = est[i]
                tõlge = input(f"Kirjuta sõna '{sõna}' tõlge vene keeles=> ")
                if tõlge.lower() == rus[i].lower():
                    print("Õige!")
                    õiged += 1
                else:
                    print(f"Vale! Õige vastus on '{rus[i]}'")
            print(f"\nTeil oli {õiged} õiget vastust {total} küsimusest ({õiged/total*100:.2f}%).")
            break

        elif V==2:
            rus = loe_failist("rus.txt")
            est = loe_failist("est.txt")
            õiged = 0
            total = len(est)
            for i in range(total):
                sõna = rus[i]
                tõlge = input(f"Kirjuta sõna '{sõna}' tõlge eesti keeles=> ")
                if tõlge.lower() == est[i].lower():
                    print("Õige!")
                    õiged += 1
                else:
                    print(f"Vale! Õige vastus on '{est[i]}'")
            print(f"\nTeil oli {õiged} õiget vastust {total} küsimusest ({õiged/total*100:.2f}%).")
            break
        
        else:
            print("Sisestage 1-2")