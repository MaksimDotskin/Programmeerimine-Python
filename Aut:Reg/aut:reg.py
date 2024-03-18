from MyModul import *
loe_fail_list(faili_nimi)
while True:
    print(""" 
registreerimine=> 1
autoriseerimine=> 2
nime või parooli muutmine=> 3
unustanud parooli taastamine=> 4
lõpetamine ja salvestamine=> 0
    
Sisestage 0-4""")
          


    try:
        V=int(input("=> "))

        if V>5:
            raise ValueError
        elif V==1:
            registreerimine()
        elif V==2:
            autoriseerimine()
        elif V==3:
            nime_või_parooli_muutmine()
        elif V==4:
            unustanud_parooli_taastamine()
        elif V==0:
            exit()
            write_fail_list()

            
    except ValueError:
        print("Sisestage 0-4")
