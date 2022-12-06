class MyClass:
    def __init__(self, counter = 0):
        print("My Class is initialized")
        self.counter = counter


    def __call__(self) :
        self.counter += 1
        print(f"My Class Object is called {self.counter}nd time")



#_call_ yazmasaydık callable false dönerdi.
print(callable(MyClass)) 


obj = MyClass()
obj()
obj()

#----------MAP--------#

l = [1,2,3,4,5,6,7,8,9,10]
l2 = [10, 11 ,12 ,13, 14, 15]
fn = lambda x, y : (x**2, y**2)
print(list(map(fn, l, l2)))
#map fonksiyonu, fn inputu kadar iterable aldı.
#l2 iterable'ı 6 elemanlı oldugu icin 6 eleman'a uyguladi
#l1'in elemanları pas gecti.


#----------FILTER--------#

newL = [0, 1, 2, 3]

#hepsini sadece 0 gidecek.
print(list(filter(None, newL)))

#hepsini sifirla carptigimizdan hepsi gidecek
print(list(filter(lambda x: x*0, newL)))

#sadece 2-2 = 0 oldugundan [0, 1, 3] kalacak
print(list(filter(lambda x: x-2, newL)))

#cift sayilari bulma eger mod 2 sifirsa True doner.
print(list(filter(lambda x: x%2 == 0, newL)))

#----------ZIP--------#

l1 = [0,1,2,3,4]
l2 = 'bthn'

print(list(zip(l1,l2)))

#----------LIST COMP.--------#

lsquare = list(map(lambda x : x**2 , [1,2,3,4]))
lsquare2 = [x**2 for x in [1,2,3,4]]

print(lsquare, lsquare2)

#ÖR

l1 = [1,2,3,4]
l2 = [-1,-2,-3,-4]

res1 = list(map(lambda x,y : x+y, l1, l2))
res2 = [x+y for x, y in zip(l1,l2)]
print(res1 == res2)

#ÖR

res1 = list(filter(lambda x: x%2 == 0, l1))
res2 = [x for x in l1 if x%2 == 0]
print(res1, res2)



l1 = range(1,11)
res = list(filter(lambda y : y < 36, map(lambda x: x**2, l1)))
print(res)

res2 = [x**2 for x in l1 if x**2 < 36]
print(res2)

#----------REDUCING FUNCS.--------#
