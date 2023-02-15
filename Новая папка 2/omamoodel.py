from ast import Str
#from curses.ascii import isupper
from datetime import date, datetime
from struct import pack
from unicodedata import digit
#8/02/23
def Lisa_andmed(i:list,p:list):
    """
    param List i: Inimeste järjend
    param list: Palgade järjend
    rtype: list, list
    """
    n=int(input("Mitu inimest:"))
    for j in range(n):
        nimi=input("sissesta nimi:")
        palk=int(input("sissesta palk:"))
        i.append(nimi)
        p.append(palk)
    return i,p
def kustutamine(i:list,p:list):
    """
    param list i: inimeste järjend
    param listp: palgade järjend
    rtype: list, lsit
    """
    nimi=input("Sissesta nimi:")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            i.pop(ind)
            ind=i.index(nimi)
            p.pop(ind)

    return i,p
def suurim_palk(i:list,p:list):
    """
    """
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi
def väike_palk(i:list,p:list):
    """
    """
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi
def sorteerimine(i:list,p:list):
    """
    """
    v=int(input("palk 1-kaheneb,2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi 
                    abi=i[j] 
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,):
               if  p[j]<p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi 
                    abi=i[j] 
                    i[j]=i[k]
                    i[k]=abi
    return i,p
def vordsed_palgad(i:list,p:list):
    """
    """
    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid=list(set(dublikatid))
    for palk in dublikatid:
        n=p.count(palk)
        k=-1
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi)
def imja(i:list,p:list):
    """
    """
    nimi=input("kelle tahad leida")
    while nimi not in i:
        nimi=input("palun kirjuta õige nimi")
        n=i.count(nimi)
    if n!=1:
        print(f"siin on mõned inimesed kes nimi on {nimi}")
        kopia=i.copy()
        for i in range(n):
            ind=kopia.index(nimi)
            kopia.remove(nimi)
            kopia.insert(ind,"")
            print(f"{i+1} {nimi} saab {p[ind]}")
    else:
         ind=i.index(nimi)
         print(f"{nimi} saab {p[ind]}")
def kustuta(i:list,p:list):
    """
    """
    kesk_palk=sum(p)/len(p)
    print(kesk_palk)
    for palk in p:
        if palk<kesk_palk:
            ind=p.index(palk)
            p.remove(palk)
            i.pop(ind)
            print(f"kustutatud {palk}")
        else:
            pass
    return i,p 
#def redact(i:list,p:list):
#    """
#    """
#    ind=i.index[0]
#    i[0].isupper()+i[1:]
#    return i
def suur_vaike(i:list,p:list):

    #for j in i:
    #    #ind=i.index[aa]       
    #    print(f"{j}")

    #tekst = "great"

    #print(i[0], tekst[2])



    number=int(input("naita palga number"))
    v=int(input("kellel palk 1- on suurem,2-on väiksem?"))
    if v==1:
        for g in p:
            if g > number:
                ind=p.index(g)
                print(f"{g}, {i[ind]}")
    if v==2:
        for g in p:
            if g < number:
                ind=p.index(g)
                print(f"{g}, {i[ind]}")
def keskminepalk(i:list,p:list):
    kesk_palk=sum(p)/len(p)
    for palk in p:
        if palk==kesk_palk:
            ind=p.index(palk)
            print(f"{kesk_palk},{i[ind]}")
def top3(i:list,p:list):

    top1=p[0]
    top2=p[0]
    top3=p[0]
    for palk in p:
        if palk>top1:
            top1=palk
        elif palk>top2:
            top2=palk
        elif palk>top3:
            top3=palk

    print("rikkad",top1, top2, top3)
    #vaesed
    top1=p[0]
    top2=p[0]
    top3=p[0]
    for palk in p:
        if palk<top1:
            top1=palk
        elif palk<top2:
            top2=palk
        elif palk<top3:
            top3=palk

    print("vaesed",top1, top2, top3)
def tulumaks():
    tulu=int(input("palga suurus "))
    #maksuvaba_tulu=()
    if tulu<1200:
        maksuvaba_tulu=500
    elif tulu<2100:
        maksuvaba_tulu=500-0.55556*(tulu-1200)
    else:
        maksuvaba_tulu=0

    
    maks=(tulu-maksuvaba_tulu) *0.20
    netopalk=tulu-maks
    print(f"netopalk on {netopalk}")