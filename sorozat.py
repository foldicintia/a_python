import random

def general(alsohatar,felsohatar):
    szamok_litsaja = []
    if felsohatar < alsohatar:
        atmenet = alsohatar
        alsohatar = felsohatar
        felsohatar = atmenet
    for i in range(0,15,1):
        vszam = random.randint(alsohatar,felsohatar)
        szamok_litsaja.append(vszam)
    return szamok_litsaja

def legkisebb(szamok_listaja):
    #minimum
    min_ert= szamok_listaja[0]
    min_hely=0
    for i in range(0,len(szamok_listaja),1):
        if szamok_listaja[i] < min_ert:
            min_ert=szamok_listaja[i]
            min_hely= i
    print("II.b")
    print(f"\tA legkisebb elem: {min_ert}")
    kifajl = open("legkisebb.txt","w",encoding="utf-8")
    print("II.b")
    print(f"\tA legkisebb elem: {min_ert}")
    kifajl.close()

def ketto():
    szamok_litsaja=general(100,200)
    legkisebb(szamok_litsaja)