#Python'da tuple tanimlamak icin () yetmez. 
#Mesela a = (1) bir tuple degil:

a = (1)
print(f"a with val: {a} is a type of : {type(a)}")

#tuple yapan aslinda virgul :
a = (1,)
print(f"a with val: {a} is a type of : {type(a)}")

#empty tanimlamak istiyorsak:
a = ()
a = tuple()
print(f"a with val: {a} is a type of : {type(a)}")

#pythonda unpacking islemi aslinda bu tuple yapisi sayesinde
a, b, c = 'XYZ'
print(f"a: {a}, b: {b}, c: {c}")

myTuple = 1, 2, 3, 4

print(f"type of myTuple: {myTuple} is : {type(myTuple)}")

#unpacking RHS first LHS after hesaplamasi sayesinde
#swap islemini hemen yapiyor.
def swap_func(a, b):
    tmp = a
    a = b
    b = tmp

def swap_with_unpack(a,b):
    a, b = b, a

#dictionary iterate ederken direkt keyleri iterate ediyor dümdüz.
#key val icin. items() diye bir sey kullaniyorduk.
#list ve tuple aksine, dictionary ve setler unordered types.


###################################

# * operatoru unpacking islemine yariyor. iterable bi seyi assign ederken ör:
    
myList = [1,2,3,4,5,6]

a, *b = myList
print(f"a: {a}, b: {b}")

#burada a'dan geri kalanı unpack edip b'ye assign etti.
    
#dictionary islemleri icin ** kullanmak gerekiyor.
#burada sumDict{myDict, mySecDict} yapamiyoruz. hatali
myDict = {'kirmizi': 1, 'mavi' : 2}
mySecDict = {'a': 0x50, 'b' : 0b0011}
#ayni key'den oldugundan yenisini almadi.
myThirdDict = {'kirmizi': 10}

sumDict = {**myDict, **mySecDict, **myThirdDict}
print(sumDict)


#normal hashmap gibi son ekleneni aliyor. single key olabilir.
abnormalDict = {'batu' : 10, 'batu': 11}
print(abnormalDict)

############################################