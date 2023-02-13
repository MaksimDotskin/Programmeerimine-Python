def Lisa_andmed(i:list,p:list):
    n=int(input("Mitu inimest:"))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p

def Kustutamine(i:list,p:list):
    nimi=input("Sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
    return i,p

def Suurim_palgad(i:list,p:list):
    while True:
        palk=max(p)
        ind=p.index(palk)
        nimi=i[ind]
        return palk,nimi

def Väisem_palgad(i:list,p:list):
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def Sorteerimine(i:list,p:list):
    v=int(input("Palk 1-kahaneb, 2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=p[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n=1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=p[k]
                    i[k]=abi
    return i,p

def Vordses_palgad(i:list,p:list):
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid))
    for palk in dublikatid:
        n=p.count(palk)
        k=-1
        print(f"(palk) saavad kätte järgmised inimesed: ")
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi,"Saab kätte",palk)
def kustuta(i:list,p:list, ):
    kesk_palk=sum(p)/len(p)
    v=int(input("Kellel palk 1- on suurem, 2- on väiksem"))
    if v==1:
        for palk in p:
            if palk>kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    else:
        pass
    return i,p