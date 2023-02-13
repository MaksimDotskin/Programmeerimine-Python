#Задание- напиши код, используя циклы while и for, который будет запрашивать у пользователя число и считать его факториал



while True:
    try:
        number=int(input("Sisesta number=>  "))
        pr=1
        for i in range(1,number+1):
            pr = pr * i
            
        print("Faktoriaalne",number,"=",pr)
        break

    except:
        print("Sisesta veel kord")





