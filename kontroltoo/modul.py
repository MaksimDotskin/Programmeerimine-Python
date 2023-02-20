def sisseastumine():

    inimesed = []     #список поступивших людей
    tulemused = []    #список их оценок
    

    while True:      #цикл while и try,expect здесь нужен чтобы пользователь не мог ввести ничего, кроме числа
        try:
            ArvInimesed = int(input("Sisestage taotlejate arv=> "))        #количество учеников
            break
        except:
            print("Vale andmed")
            
    for i in range(ArvInimesed):
        nimi = input("Sisestage taotleja nimi {}=> ".format(i+1))       #пользоватенль вводит имя которое заносится в спиок поступивших
        while True:
            try:
                hinne = int(input("Sisestage taotleja hinne {}=> ".format(i+1)))      #пользоватенль вводит оценку котороя заносится в спиок оценок поступивших
                break
            except:
                print("Vale andmed")

        inimesed.append(nimi)      
        tulemused.append(hinne)
    
    while True:       #меню выбора
        print("\nValige toiming:")
        print("1. Uurige ülikooli astunud inimeste nimekirja")
        print("2. Kuvage inimeste loend ja nende tulemused tähestikulises järjekorras")
        print("3. Leidke n inimest, kellel on kõige halvemad tulemused")
        print("4. Leidke taotlejate keskmine punktisumma")
        print("5. Parim tulemus üldse")
        print("0. Välju")
        
        while True:     #здесь ничего необчного
            try:
                valimus = int(input("Sisestage oma valik=> "))
                break
            except:
                print("Vale andmed")
        
        if valimus == 0:    #здесь ничего необчного
            break 

        elif valimus == 1:        #здесь ничего необчного
            print("\nÜlikooli astunud inimeste nimekiri:")

            for i in range(ArvInimesed):
                a=0
                if tulemused[i] >= a:
                    print(inimesed[i])

        elif valimus == 2:          #здесь благодоря функции sorted списки сортируются по алфавиту
            print("\nInimeste loend ja nende tulemused:")

            for nimi, hinne in sorted(zip(inimesed, tulemused)):
                print(nimi, hinne)
                
        elif valimus == 3:       
            while True:
                try:
                    
                    n = int(input("Sisestage otsimiseks halvimate tulemuste arv=> "))
                    break
                except:
                    print("Vale andmed")

            
            halvimadHinned = sorted(tulemused)[:n]         #здесь код показывает хучших поступивших, количество которых вводит пользователь(переменная n) используя различные функции
            halvimadInimesed = [inimesed[tulemused.index(score)] for score in halvimadHinned]

            print("\n{} kõige halvemate tulemustega taotlejad:".format(n))

            for i, nimi in enumerate(halvimadInimesed):
                print("{}. {} ({})".format(i+1, nimi, halvimadHinned[i]))

        elif valimus == 4:      #среднее арифмитическое, здесь нечего обьяснять
            keskmine = sum(tulemused) / len(tulemused)
            print("\nTaotlejate keskmine hinne: {:.2f}".format(keskmine))

        elif valimus == 5:
            paremHinne=max(tulemused)
            print("Kõige parem tulemus=>",paremHinne)    #мой вариант, это наилучший результат среди всех, функция max
            
            
        else:
            print("Vale andmed")    #не позволяет ввести что нибудь, кроме чисел от одного до пяти
