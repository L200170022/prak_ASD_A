#Nomer1
def Siku(a):
    x=1
    while x<=a:
        print("*"*x)
        x+=1

print("Nomer 1")
Siku(5)

#Nomer 2
def SegiEmpat(a,b):
    x=1
    print("@"*b)
    while(x<a):
       print("@"+" "*(b-2)+"@")
       x+=1
    print("@"*b)
print("\nNomer 2")
SegiEmpat(5,5)

#Nomer 3A
def jumlahVokal(a):
    v="aiueoAIUEO"
    vokal=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            vokal+=1
    return (jumlahhuruf,vokal)
print("\nNomer 3 A")
print(jumlahVokal("Surakarta"))

#Nomer 3B
print("Nomer 3 B")
def jumlahKonsonan(a):
    v="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    konsonan=0
    jumlahhuruf=0
    for x in a:
        jumlahhuruf+=1
        if x in v:
            konsonan+=1
    return (jumlahhuruf,konsonan)
print(jumlahKonsonan("Surakarta"))

#Nomer 4
print("\nNomer 4")
def rerata(b=[]):
    x=0
    n=0
    if b != []:
        for i in b:
            x+=i
            n+=1
        return x/n
z=rerata([1,2,3,4,5])
print(z)

g=[3,4,5,4,3,4,5,2,2,10,11,23]
r=rerata(g)
print(r)

#Nomer 5
print("\nNomer 5")
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))

#Nomer6
print("\nNomer 6")
def bilanganprima():
    prima=list()
    for i in range(2,100):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if(x):
            print(i)
            prima.append(i)
bilanganprima()

#Nomer 7
print("\nNomer 7")
def faktorPrima(n):
    prima=list()
    for i in range(2,n):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if x and n%i==0:
            prima.append(i)
    return prima
print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))

#Nomer 8
print("\nNomer 8")
def apakahTerkandung(a,b):
    return a in b
h ="do"
k ="Indonesia tanah air kita"
print(apakahTerkandung(h,k))
print(apakahTerkandung("pusaka",k))

#Nomer 9
print("\nNomer 9")
def coba():
    for x in range(1,100):
        if (x%3)!=0 and (x%5)!=0:
            print(x)
        else:
            if (x%15)==0:
                print("PYTHON UMS")
            elif (x%3)==0:
                print("python")
            elif (x%5)==0:
                print("UMS")
coba()

#Nomer 10
print("\nNomer 10")
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    d=(b**2)-(4*a*c)
    if d<0:
        return "determinan negatif. Persamaan tidak mempunyai akar real"
    return  "determinanpositif. Persamaan mempunyai akar real"
print(selesaikanABC(1,2,3))

#Nomer 11
print("\nNomer 11")
def apakahkabisat(x):
    if(x%400==0):
        return True
    if(x%100==0):
        return False
    if(x%4==0):
        return True
    return False
print(apakahkabisat(2400))

#Nomer 12
print("\nNomer 12")
import random
def permainanTA():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("masukan angka: "))
        if(b>a):
            print("itu terlalu besar,coba lagi")
        elif(b<a):
            print("itu terlalu kecil,coba lagi")
        else:
            print("benar")
            break
print("belum dimasukan Perintah 'permainanTA'")

#Nomer 13
print("\nNomer 13")
def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",-6:"ratus ",-7:"juta ",8:"puluhjuta "}
    b=str(a)
    z=""
    i=-1
    while i>= -len(b):
        z=x[b[i]]+y[i]+z
        i-=1
    return z
print(katakan(3125750))

#Nomer 14
print("\nNomer 14")
def formatRupiah(x):
    y=str(x)
    z=""
    i = -1
    while i>= -len(y):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+z
        z=y[i]+z
        i-=1
    return "'"+"Rp "+z+"'"
print(formatRupiah(1500))
print(formatRupiah(2560000))