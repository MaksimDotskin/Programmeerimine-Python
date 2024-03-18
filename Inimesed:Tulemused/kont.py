from mimodul import *


sisseastumine()

while True:       
    print("\nValige toiming:")
    print("1. Uurige ülikooli astunud inimeste nimekirja")
    print("2. Kuvage inimeste loend ja nende tulemused tähestikulises järjekorras")
    print("3. Leidke n inimest, kellel on kõige halvemad tulemused")
    print("4. Leidke taotlejate keskmine punktisumma")
    print("5. Parim tulemus üldse")
    print("0. Välju")
    
    while True:     
        try:
            valimus = int(input("Sisestage oma valik=> "))
            break
        except:
            print("Vale andmed")
    
    if valimus == 0:    
        break 

    elif valimus == 1:        
        valimus1()

    elif valimus == 2:          
        valimus2()
            
    elif valimus == 3:       
        valimus3()

    elif valimus == 4:      
        valimus4()

    elif valimus == 5:
        valimus5()   
        
        
    else:
        print("Vale andmed")    

