import string
import random

autoriseeritud=None
sisse_loogitud_login=None
sisse_loogitud_parol=None


def loe_fail_list(faili_nimi):
    global loginid
    loginid = []
    global paroolid
    paroolid = []

    with open(faili_nimi, 'r') as file:
        for line in file:
            login, password = line.strip().split(' ')
            loginid.append(login)
            paroolid.append(password)
    print(loginid)
    print(paroolid)

    return loginid, paroolid

faili_nimi='log.txt'


def write_fail_list():
    with open('log.txt', 'a') as file:
        for nimi, parool in zip(loginid, paroolid):
            file.write(nimi + ' ' + parool + '\n')

def registreerimine():
    while True:
        nimi=input("Login: ")
        if nimi in loginid:
            print("See nimi on juba võetud")
        else:
            loginid.append(nimi)
            print("Login on registreeritud")

            print("Automaatne_parooli_genereerimine=> 1")
            print("Ise parooli loomine=> 2")
            while True:
                try:
                    V=int(input("=> "))
                    if V>2 or V<1:
                        raise ValueError
                    elif V==1:
                        automaatne_parooli_genereerimine()
                        break
                    elif V==2:
                        kasutaja_loob_ise_parool()
                        break
                except ValueError:
                    print("Sisestage 1-2")
            break
def automaatne_parooli_genereerimine():
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print("Teie parool on: ",psword)
    paroolid.append(psword)


def kasutaja_loob_ise_parool():
    while True:
        print("""Turvanõuded:
Parool peab sisaldama suuri ja väikesi tähti, numbreid ja erimärke""")
        
        psword=input("Parool: ")
        if check_parool(psword):
            print("Parool on registreeritud")
            paroolid.append(psword)
            break
        else:
            print("Parool ei vasta turvanõuetele, palun sisestage veel kord ohutusnõuete järgimine")


def check_parool(psword):
    if not any(char.isupper() for char in psword):
        return False
    if not any(char.islower() for char in psword):
        return False
    if not any(char.isdigit() for char in psword):
        return False
    spec_simv = set(string.punctuation)
    if not any(char in spec_simv for char in psword):
        return False
    return True

def autoriseerimine():
    while True:
        nimi=input("Login: ")
        psword=input("Parool: ")
        loginid_paroolid=[]

        for i in range(len(loginid)):
            loginid_paroolid.append(loginid[i]+' '+paroolid[i])

        login_parool=nimi+' '+psword
        if login_parool in loginid_paroolid:
            print("Olete sisse logitud")
            global autoriseeritud
            autoriseeritud=True
            global sisse_loogitud_login
            sisse_loogitud_login=nimi
            global sisse_loogitud_parol
            sisse_loogitud_parol=psword

            break
        else:
            print("Vale login või parool")
            print("Proovige veel kord")


def nime_või_parooli_muutmine():
    if autoriseeritud==True:

        print("""Logimise muutmine=> 1
Parooli muutmine=>2 """)
        
        while True:
            try:
                V=int(input("=> "))
                if V>2 or V<1:
                    raise ValueError
                elif V==1:
                    Logimise_muutmine()
                    break
                elif V==2:
                    Parooli_muutmine()
                    break

            except ValueError:
                print("Sisestage 1-2")
    elif autoriseeritud!=True:
        print("Sisselogimise või parooli muutmiseks palun autoriseerige")

def change_value_login():
    global sisse_loogitud_login
    for i in range(len(loginid)):
        if loginid[i] == sisse_loogitud_login:
            loginid[i] = uus_login
    sisse_loogitud_login= uus_login

def Logimise_muutmine():
    print("Vana login: ",sisse_loogitud_login)
    global uus_login
    uus_login=input("Uus login: ")
    change_value_login()


def change_value_parool():
    global sisse_loogitud_parol
    for i in range(len(paroolid)):
        if paroolid[i] == sisse_loogitud_parol:
            paroolid[i] = uus_parool
    sisse_loogitud_parol= uus_parool


def Parooli_muutmine():
    print("Vana parool: ",sisse_loogitud_parol)
    print("""Turvanõuded:
Parool peab sisaldama suuri ja väikesi tähti, numbreid ja erimärke""")
    while True:
        global uus_parool
        uus_parool=input("Uus parool: ")
        if check_parool(uus_parool):
            change_value_parool()
            break
        else:
            print("Parool ei vasta turvanõuetele, palun sisestage veel kord ohutusnõuete järgimine")

def unustanud_parooli_taastamine():
    print("""Parooli taastamiseks sisestage oma kasutajanimi ja vähemalt paroolist üks suur täht,
üks väike täht, üks number ja üks sümbol, mida mäletate unustatud paroolist""")
    
    while True:
        login=input("Login: ")

        if login in loginid:
            login_index = loginid.index(login)
            my_password = paroolid[login_index]
            suur_taht=input("Suur täht: ")
            vaike_taht=input("Väike täht: ")
            num=input("Number: ")
            sumb=input("Sümbol: ")
            nelitaht=[suur_taht,vaike_taht,num,sumb]

            if all(x in my_password for x in nelitaht):
                print("""Sisestage uus parool
    Turvanõuded:
Parool peab sisaldama suuri ja väikesi tähti, numbreid ja erimärke""")
                while True:
                    global uus_parool
                    uus_parool=input("Uus parool: ")
                    if check_parool(uus_parool):
                        change_value_parool()
                        break
                    else:
                        print("Parool ei vasta turvanõuetele, palun sisestage veel kord ohutusnõuete järgimine")

            else:
                print("""Parooli taastamine ebaõnnestus,
sisestatud märgid ei ühti sisestatud sisselogimise kaotatud parooliga""")
            break
        else:
            print("Vale login")