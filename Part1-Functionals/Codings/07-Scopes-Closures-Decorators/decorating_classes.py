#bi classa yeni ve generic fonksiyonlar ekleyebiliriz.
#mesela tüm sınıflara info fonksiyonu basmak isteyebiliriz
#onların sahip oldugu degiskenleri vb. buna info fonksiyonu desek
#aslında fonksiyonun member func olacagi icin self parametresini almasi lazim



def info(self):
    for k, v in vars(self).items():
        print(f"memb : {k} val : {v}")


def debugger(cls):
    cls.debug = info
    #return etmezsek decorator olarak kullanamayiz.
    #sebebi de normalde decarotor mantigi my_func = decorator(my_func)
    #simdi bu debugger decorator'u bi sey return etmezse NoneType obj kalir.
    return cls

@debugger
class myClass:
    def __init__(self):
        self.boy = 180
        self.kilo = 93


    def speak(self):
        print("Selamlar Dunya!")

@debugger
class Vehicle:
    def __init__(self):
        self.teker_sayisi = 4
        self.kapi_sayisi = 2


#myClass = debugger(myClass)
m = myClass()
m.debug()    

v = Vehicle()
v.debug()