import time

a = lambda x, y : x+y
b = lambda : 'hello'

print(a(2,3))
print(b())
print(a)



def func_a(x, y):
    return x+y

#a ve func_a aslında identical.
#lambdalar fonksiyonlara param olarak da verilebilir aynı diger funclar gibi



def time_calculator(fn, **kwargs):
    """
    ilk input olarak bir fonksiyon alır
    sonrasında o fonksiyonun argumanları kwarg olarak alır.
    ve zaman olcer.
    """
    start = time.time()
    fn(**kwargs)
    end = time.time()
    print(f"Function Execution is: {end - start}")


time_calculator(lambda x: time.sleep(x), x = 1)

#z range'i boyunca y'ye x'i append eder.
my_lambda = lambda x,y,z :  [y.append(x) for x in range(0,z)]
time_calculator(my_lambda, x = 0 , y = [], z = 1000000)


# özellikle sorted icerisinde cok kullanilir.

myList = ['a', 'B', 'C', 'd']
print(sorted.__doc__)
print("\n\n", sorted(myList))
#burada görüldügü gibi sorted 'a' : 97 'B' : 46 oldugundan char olarak, 'B' yi başa koydu.
#simdi sorted'a bir key func vericez arguman olarak.

s_list = sorted(myList, key=lambda lstElement : lstElement.upper())
print(s_list)
#bu sayede tum elemanları sortlamadan upper yaptık ve 'a' en öne geldi.

#sorted, dictionary'leri de keylere gore siralar.

myDict = {'def' : 200, 'abc' : 500, 'xyz' : 100}
print(sorted(myDict))

#bunu value'ya gore siralamak istersek
print(sorted(myDict, key = lambda e : myDict[e]))


#sorted istedigimiz veri elemani tipinde calismayabilir. Bu durumda da lambda tanimlayabiliriz

myComplexList = [3+3j, 1+2j, 7+4j] 
#print(sorted(myComplexList)) -> hata verecektir.

print(sorted(myComplexList, key = lambda x : x.real**2 + x.imag**2))


### Challange : Randomize a list by sorted

myList = [1,2,3,4,5,6,7,8,9,10]

import random
print(sorted(myList, key = lambda x: random.randint(x, x*500)))
    
