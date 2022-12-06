#normalde print func built-in scope
#yani direkt cagirabiliyoruz.

#ancak ben redefine ettigimde
#ilk olarak module namespace aranacagindan
#benim yeni tanimladigim print func cagirilir.

# def print(x):
#     import time
#     time.sleep(x)


a = 10
def my_func():
    a = 20
    print(a)

def my_fn():
    global a
    a = 50

my_func()
print(a)
my_fn()
print(a)

### Non Local Scopes
print("\n\n\n######NON_LOCAL_SCOPES######\n\n")

def outer_func():
    x = "hello"
    def inner_1():
        def inner_2():
            print(x)
        inner_2()
    inner_1()

outer_func()
print("\n")

def outer_1():
    x = "python"
    def inner_1():
        x = "c++"
        print(f"inner : {x}")
    inner_1()
    print(f"outer : {x}")

outer_1()


def outer_2():
    x = "python"
    def inner_1():
        nonlocal x
        x = "c++"
        print(f"inner : {x}")
    inner_1()
    print(f"outer : {x}")

outer_2()

### Closures
print("\n\n\n######CLOSURES######\n\n")

def counter():
    count : int = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc

fn = counter()
c = fn()
c = fn()
print(f"counter value is c : {c}")
#görüldügü üzere ilk fn'i counter'a esitledigimde inner'in closure'ını verdik fn'e.
#sonrasinda hep ayni inneri cagirarak counter'i artirdik.

fn_1 = counter()
fn_2 = counter()
#bu sekilde bi tanimlamada iki farkli inc yaratilip dönecek
c_1 = fn_1()
c_1 = fn_2()
#bu sekilde artirirsam aslinda c_1 hala 1 olmali. yani fn_2'nin free var. counteri
print(f"counter of fn_2 : {c_1}")

#peki shared scope'u genisletebilir miyiz?

def outer() :
    count : int = 0
    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count
    return inc1, inc2

f1, f2 = outer()
f1()
c2 = f2()
print(f"counter value of f2 is {c2}")

adders = list()
for n in range(1,3):
    adders.append(lambda x: x+n)

print(adders[1](5)) # 7
print(adders[0](5)) # 7


#bu problemi cözmek icin söyle bir sey yapabiliriz

def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x, y=n: x+y)
    return adders

adders = create_adders()
print(adders[0](10)) # -> 11
print(adders[2](10)) # -> 13
#default value'lar creation time'da memory'e yerlesiyordu.
#bu sebeple fonksiyon create edilirken default value'yi set etmis olduk.

#mesela bir fonksiyonun kac kere cagirildigini hesaplayan bi func yazalim:

def counter(fn , counters : dict):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt 
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)

    return inner

def add(a, b):
    return a+b

def mult(a,b):
    return a*b

c = dict()
add_cnt = counter(add, c)
mult_cnt = counter(mult, c)


add_cnt(10,20)
add_cnt(5,10)
mult_cnt(20,25)

print(c)

add = counter(add, c)
add(2,3)
print(c)
