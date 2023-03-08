inimesed = []     
tulemused = []    

def sisseastumine():
    while True:     
        try:
            global ArvInimesed
            ArvInimesed = int(input("Sisestage taotlejate arv=> "))        
            break
        except:
            print("Vale andmed")
            
    for i in range(ArvInimesed):
        nimi = input("Sisestage taotleja nimi {}=> ".format(i+1))     
        while True:
            try:
                hinne = int(input("Sisestage taotleja hinne {}=> ".format(i+1)))    
                break
            except:
                print("Vale andmed")

        inimesed.append(nimi)      
        tulemused.append(hinne)


def valimus1():
    print("\nÜlikooli astunud inimeste nimekiri:")

    for i in range(ArvInimesed):
                
        print(inimesed[i])


def valimus2():
    print("\nInimeste loend ja nende tulemused:")

    for nimi, hinne in sorted(zip(inimesed, tulemused)):
        print(nimi, hinne)

def valimus3():
    while True:
        try:
                    
            n = int(input("Sisestage otsimiseks halvimate tulemuste arv=> "))
            break
        except:
            print("Vale andmed")

            
    halvimadHinned = sorted(tulemused)[:n]         
    halvimadInimesed = [inimesed[tulemused.index(hinne)] for hinne in halvimadHinned]

    print("\n{} kõige halvemate tulemustega taotlejad:".format(n))

    for i, nimi in enumerate(halvimadInimesed):
        print("{}. {} ({})".format(i+1, nimi, halvimadHinned[i]))

def valimus4():
    keskmine = sum(tulemused) / len(tulemused)
    print("\nTaotlejate keskmine hinne: {:.2f}".format(keskmine))

def valimus5():
    paremHinne=max(tulemused)
    print("Kõige parem tulemus=>",paremHinne)    
            


