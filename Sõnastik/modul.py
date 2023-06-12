def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def tõlge(f1,f2,sõna):
    rus:list=loe_failist(f1)
    est:list=loe_failist(f2)
    Sõnastik=dict(zip(est, rus))
    print(est)
      
    tõlgenud=Sõnastik.get(sõna)

    if tõlgenud:
        print("Tõlkinud sõna:", tõlge)
        status=True
        return tõlgenud,status
    else:
        answer=("Sellist sõnu sõnastikus pole")
        status=False
        return answer,status

def lisa_sõna(uus_rus_sõna,uus_est_sõna,uus_ing_sõna):
    with open('rus.txt', 'a', encoding='utf-8') as rus_file, \
         open('est.txt', 'a', encoding='utf-8') as est_file, \
         open('eng.txt', 'a', encoding='utf-8') as ing_file:
        rus_file.write(uus_rus_sõna + '\n')
        est_file.write(uus_est_sõna + '\n')
        ing_file.write(uus_ing_sõna + '\n')


def Sõnastiku_väljund():
    print("Sõnad vene keeles:")
    rus:list=loe_failist("rus.txt")
    print(rus)
    print("Sõnad eesti keeles:")
    est:list=loe_failist("est.txt")
    print(est)

def muuda_sõna(old_sõna,new_sõna):
    with open('rus.txt','r',encoding='utf-8') as rus_file:
        rus=rus_file.read()

    with open('est.txt','r',encoding='utf-8') as est_file:
        est=est_file.read()

    with open('eng.txt','r',encoding='utf-8') as ing_file:
        ing=ing_file.read()

    

    if old_sõna in rus:
        rus2=rus.replace(old_sõna,new_sõna)
    
        with open('rus.txt', 'w', encoding='utf-8') as rus_file:
            rus_file.write(rus2)

        answer="Sõna on muutanud"
        return answer

    elif old_sõna in est:
        est2=est.replace(old_sõna,new_sõna)

        with open('est.txt', 'w', encoding='utf-8') as est_file:
            est_file.write(est2)
        answer="Sõna on muutanud"
        return answer
    
    elif old_sõna in ing:
        ing2=ing.replace(old_sõna,new_sõna)

        with open('eng.txt', 'w', encoding='utf-8') as ing_file:
            ing_file.write(ing2)
        answer="Sõna on muutanud"
        return answer
    
    else:
        answer="Sellist sõnu sõnastikus pole"
        return answer




