## Arguments vs Parameters

#burada my_func icerisindeki a ve b : function parameters ve local variables in my_func
def my_func(a, b) -> None:
    a = 20
    b = "x"

def my_func_for_lists(a, b) -> None:
    a.append(50)
    a += [1]
    b = 'c'

myVar : int = 10
myStr : str = "bth"

#burada myVar ve myStr benim argumanlarim.
#x ve y pass by reference oluyor yani memory adresleri func'a geciyor.
my_func(myVar, myStr)

#burada string ve int mutable olmadigindan 10 ve bth olarak basar, cünkü yeni bi deger verirken yeni memory aliyor.
#ama liste gibi mutable bi nesne verseydik o zaman func başarılı şekilde degerleri degistirecekti.
print(myVar, myStr)

myVar : list = [10, 20, 30]
my_func_for_lists(myVar, myStr)
print(myVar, myStr)

#Default value

def my_func_with_default_val(a, b, c = 100):
    pass

# def my_func_with_illegal_default_val(a, b = 100, c):
#     pass # Illegal.

#eger default val veriyorsak sagdakileri de default almali. c++'ta da böyle.

def my_function(a, b = 5, c = 20):
    print(f"a: {a}, b: {b}, c: {c}")
#eger sadece a ve c kullanmak istiyorsak soyle olmali:
#bu sekilde c=50 gibi belirtiyorsak keyword argument diyoruz.
my_function(a=20, c=50)
my_function(c=10, a=1, b=5)

#burada my_function(c=20, 1, 5) illegal kullanim. eger sondakini named kullaniyosak ya da ortadaki, hepsini
#named argument'e cevirmeliyiz. yoksa ambiguity olur.

############################################################################################


# -> default value argumentların tehlikeli oldugu bi nokta var:

#module a.py
import datetime
import time
def module_timer(a, b, tm = datetime.datetime.now(datetime.timezone.utc)):
    print(f"Time is : {tm}")

#module b.py
#import a.py as a
#a.module_timer() -> bu func hep aynı sonucu verir.
#cunku import a.py as a derken aslında default value  bi kere memory'e yaziliyor ve func defaultla her cagrildiginca
#daha once yazilan memory adresine gidiliyor.

module_timer(1,2)
time.sleep(5)
module_timer(2,3)
time.sleep(5)
module_timer(2,3, datetime.datetime.now(datetime.timezone.utc))

#yukaridaki blokta 1. ve 2. call'larda aynı datetime yazilirken 3.de farkli yazilacak.
#bu sebeple genelde bu default val'lerde None kullanmak mantıklı.

def module_timer_updated(a, b, tm=None):
    if (tm == None):
        tm = datetime.datetime.now(datetime.timezone.utc)

    print(f"Time is : {tm}")

#bu sekilde default value'yi None initialize ettik ve param gelmezse gercekten saati guncelleyecek
module_timer(1,2)
time.sleep(5)
module_timer(2,3)