from math import *
from pickle import TRUE
from random import *
from time import sleep

#try:
##    nimi=input("Mis su nimi on?")
##    if nimi.upper()=="JUKU":
##        print("lähme kinno")
##        vanus=int(input("kui vana sa oled?"))
##        if vanus>=0 or vanus<=100:
##            print("VIGA")
##        elif vanus<6:
##            print("tasuta!")
##        elif vanus>=6 and vanus<=14:
##            print("Lapse pilet")
##        elif vanus>=15 and vanus<=65:
##            print("täispilet")
##        elif vanus>=65:
##            print("soodus pilet")
##    else:
##        print("Otsime Juku")
##except:
##    print("vale andmetüüp")
###teine ülesanne
##nimi1=input("mis sinu nimi on?")
##nimi2=input("mis sinu nimi on?")
##if nimi1.isalpha()==True and nimi2.isalpha():
##    if nimi1==("oleg") and nimi2==("sanja"):
##        print(f"{nimi1} ja {nimi2} te olete täna pinginaabrid")
##    else:
##        print()
##else:
##    print("välja Andmetüüp")
##kolmas ülesanne
##try:
##    pikkus=float(input("Mis pikkus on?"))
##    laius=float(input("Mis laius on?"))
##    if pikkus>0 and laius>0:
##        print("lean pindala!")
##        Pindala=laius*pikkus
##        print(f"Pindala on : {Pindala}")
##        print("Kas teeme remondi või ei tee?")
##        vastus=input("")
##        if vastus.lower()=="jah":
##            hind=float(input("kui palju maksab ruutmeeter?"))
##            if hind<0:
##                print("vale vastus, palun sisesta positiivne arv.")
##            else:
##                põrand=hind*Pindala
##                print(f"remondi summa on: {põrand}")           
#except:
#    print("Andmetüüp on vale, peab olema ujumiskomaga")
#neljas ülesanne
#try:
#    hind=float(input("mis on hind?"))
#    if hind>0:

#        if hind>700:
#            print(f"sul on soodus 30%, {hind-hind*0.3}")
#        else:
#            print(f"{hind}")
#except:
#    print("andmetüüp on vale")
#viies ülesanne
#n=int(input("Mitu toa korteris?"))
#for i in range(1,n+1,1): #range(n) i=0,1,2,3,..,n-1
#    t=float(input(f"{i}. toa Temperatuur: "))
#    if t>18:
#        print("Soe")
#    else:
##        print("Külm")
##kuues ülesanne
##p=k=l=0
##inimene=randint(1,20)
##print("Kokku on",inimene,"inimest")
##for i in range(1,inimene+1,1):
##    sleep(1)
##    pikkus=randint(56,256)
##    if pikkus>178:
##        print("pikk!")
##        p+=1
##    elif pikkus>155 and pikkus<=178:
##        print("keskmine")
##        k?=1
##    else:
##        print("Lühike")
##        l+=1
##print(f"Pikka kasvu {p} inimest")
##print(f"Keskmise kasvu {k} inimest")
##print(f"Lühike kasvu {l} inimest")

#p=k=l=0
#kogus randint(1,20) #inimeste kogus
#print("kokku on ",kogus,"inimest")
#while kogus-=1
#sleep(1)
#pikkus=randint(56,256)
#if pikkus>178:
#    print("Pikk")
#    p+1
#elif pikkus>155 and pikkus>=178:
#    print("keskmine")
#    k+=1
#    else:
#        print("lühike")
#        l+=1
#print("popa")
#print("popa")
#print("popa no malenkaja")
a=0
b=1
while a!=b:
    while True:
        try:
            a=float(input("Sisesta 1. külg: "))
            break
        except:
            print("Sisesta veel kord")
    while True:
        try:
            b=float(input("Sisesta 2. külg: "))
            break
        except:
            print("Sisesta veel kord")
    if a!=b: print("Andmetüüp on ok, vaid see ei ole ruud!")
print(f"See on ruud. Ruudu külg võrdub {a}")

