#nomor6
class simpulpohonbiner(object):
    def __init__ (self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

def ukuranpohon (akar, count = 0 ):
    if akar is None :
        return count

    return ukuranpohon(akar.kiri, ukuranpohon(akar.kanan, count +1))

a = simpulpohonbiner ('Ambarawa')
b = simpulpohonbiner ('Bantul')
c = simpulpohonbiner ('Cimahi')
d = simpulpohonbiner ('Denpasar')
e = simpulpohonbiner ('Enrekang')
f = simpulpohonbiner ('Flores')
g = simpulpohonbiner ('Garut')
h = simpulpohonbiner ('Halmahera Timur')
i = simpulpohonbiner ('Indramayu')

a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h
g.kanan = i

#nomor7
class tinggipohonbiner (object):
    def __init__ (self, data) :
        self.data = data
        self.kiri = None
        self.kanan = None
def tinggipohon(akar) :
    if akar is None:
        return 0
    else :
        return max(tinggipohon(akar.kiri), tinggipohon(akar.kanan))+ 1
    
a = simpulpohonbiner ('Ambarawa')
b = simpulpohonbiner ('Bantul')
c = simpulpohonbiner ('Cimahi')
d = simpulpohonbiner ('Denpasar')
e = simpulpohonbiner ('Enrekang')
f = simpulpohonbiner ('Flores')
g = simpulpohonbiner ('Garut')
h = simpulpohonbiner ('Halmahera Timur')
i = simpulpohonbiner ('Indramayu')

a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h
g.kanan = i

#nomor8
class simpulpohonbiner (object):
    def __init__ (self, data) :
        self.data = data
        self.kiri = None
        self.kanan = None

def cetak(subpohon, count = 0):
    if subpohon is not None:
        print (subpohon.data + ',level ' + str (count))
        (cetak(subpohon.kiri, count + 1), cetak(subpohon.kanan, count + 1))

a = simpulpohonbiner ('Ambarawa')
b = simpulpohonbiner ('Bantul')
c = simpulpohonbiner ('Cimahi')
d = simpulpohonbiner ('Denpasar')
e = simpulpohonbiner ('Enrekang')
f = simpulpohonbiner ('Flores')
g = simpulpohonbiner ('Garut')
h = simpulpohonbiner ('Halmahera Timur')
i = simpulpohonbiner ('Indramayu')

a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h
g.kanan = i


    
