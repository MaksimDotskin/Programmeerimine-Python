print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => ")))) #добавил две скобки
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mötet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake lui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0: #добавил двоеточье
            if b % 2 == 0: #добавил ровно
                    paaris += 1 #поменял местами = и +
            else:
                    paaritu += 1 #поменял местами = и +
            b = b // 10
     
    print("Paarisarvud:", paaris) #добавил запятую
    print("Paarituid numbreid:", paaritu) #добавил запятую
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake * sisestatud number")
    print()
    b=0
    while a > 0: #добавил двуеточье
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #поменял местами = и +
    print("*Tagasta* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine") #удалил скобку
    print()
    if c % 2 == 0: #добавил ровно
        print("с - paarisarv. Jagage 2-ga.")
    else:
        print("с - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 == 0: #добавил ровно
                    c = c / 2 #удалил ровно
            else:
                    c = (3*c + 1) / 2 #удалил ровно
            print(round(c), end=" ") #добавил верный знак припенания
    print()
    print("Hüpotees on õige") #добавил верный знак припенания