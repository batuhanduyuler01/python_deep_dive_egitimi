# Scopes - Closures - Decorators

## 1. Global and Local Scope
--- 

-> Global Scope

Pythonda c++'taki ya da c'deki gibi global scope'ta bir nesne tanımlamaktansa, module icerisinde tanımladigimiz degiskenler o modul icinde global oluyor.

ancak built in modulunde print, True, False gibi degerler gercekten global diyebiliriz.

-> Local Scope

fonksiyon icerisinde yaratilan variable'lar diyebiliriz.

fonksiyon her cagirildiginda yeni bir scope yaratilir.
o zamana kadar oyle bir scope yok.

```
a = 10
def my_func():
    a = 20
    print(a)

def my_fn():
    global a
    a = 50

my_func() -> 20
print(a)  -> 10
my_fn() 
print(a)  -> 50
```

my_func icin local scope'ta yaratilan a degisiyor. bu sebeple global scopetaki a'yi degistirmiyor.
ancak my_fun icin __global__ keywordu kullandık. Bu sayede global namespace'e eristi direkt.

--- 
## 2. Non-Local Scopes
--- 

```
def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
#bu func, outer func cagirildiginda yaratilir.
    inner_func()
```

- önce x yaratilir.
- sonra inner_func yaratilir x'i bilmiyo
- inner_func cagrildiginda bi üstteki scope aranir
- x bulunur. 
- burada x aslında non-local scope'ta bulundu.


```
def outer_1():
    x = "python"
    def inner_1():
        x = "c++"
        print(f"inner : {x}")
    inner_1()
    print(f"outer : {x}")

outer_1()

inner : c++
outer : python 
```
non local olarak tanımlarsak üstteki scopetaki x'i alacaktır
```
def outer_2():
    x = "python"
    def inner_1():
        nonlocal x
        x = "c++"
        print(f"inner : {x}")
    inner_1()
    print(f"outer : {x}")

outer_2()

inner : c++
outer : c++
```

--- 
## 3. Closures
--- 

```
def outer():
    x = "hello"
    def inner():
        print(f"{x} world!")
    
    inner()

outer()
```
yukarıdaki fonksiyonda inner func'taki x aslında outer scope'taki x'e refer ediyor.
buna nonlocal variable demiştik. Free variable da diyebiliyoruz.


memory'de inner değişkenine baktığımızda aslında hem inner fonckisoyunu hem de free variable x'i refer ediyoruz. Bunu bi kapsul gibi düsünebiliriz.


Bu yapıya <b>Closure</b> deniyor.

__Closure Part__
```
x = "hello"
    def inner():
        print(f"{x} world!")
```

- genel olarak closure'u, inner function + extended scope of free variables olarak düsünebiliriz.


```
def outer():
    x = "hello"
    def inner():
        print(f"{x} world!")
    
    return inner

fn = outer()

print(fn.__code__.co_freevars) 
print(fn.__closure__) #cell adresi ve icerigini basar.
```
__fn -> inner + extended scope(free variable)__

lambdalar ile closure yaratılabilir
```
adders = list()
for n in range(1,3):
    adders.append(lambda x: x+n)

print(adders[1](5)) -> 7
print(adders[0](5)) -> 7
```
burada closure, aslında ```adders[ n ]( x )``` cagirildinda yaratildigindan dolayi
n = 2 oldugunda iki fonksiyon da cagirilmis olacak. yani pyton fonksiyon cagirilana kadar n'i evaluate etmemis olacak.

bu problemi cözmek icin söyle bir yöntem izleyebiliriz.
```
def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x, y=n: x+y)
    return adders

adders = create_adders()
print(adders[0](10)) # -> 11
print(adders[2](10)) # -> 13
print(adders[2](10, 5)) # -> 15
```
- default value'lar creation time'da memory'e yerlesiyordu.
- bu sebeple fonksiyon create edilirken default value'yi set etmis olduk.
- ve bunlar artık shared variable paylasmadigindan closure olmadi
- cünkü hicbir free variable'ı yok.

Normalde bi avg hesaplamayı listeye elemanları pushlayarak ve listenin uzunluğu bölü eleman sayısı ile hesaplayabiliyorduk. Python'da closure ve C'de global variable kullanarak basitce hesaplama ornekleri asagida (dizi kullanmadan memory efficient)

Python Implementasyonu
```
def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total/count
    return add

a = averager()
a(10) # -> 10
a(20) # -> 15
```
C Implementasyonu
```
#include <stdio.h>

int total = 0;
int count = 0;

float add(int number)
{
    total += number;
    count += 1;
    return total/count;
}


int main()
{
    float(*fn)(int) = add; 
    printf("%f is the avg", fn(10)); // -> 10
    printf("%f is the avg", fn(20)); // -> 15
    
    printf("Hello World");

    return 0;
}
```

asagidaki ornekte bi counter fonksiyonu belirledik ve return olarak bi closure dönüyor. Burada fn alıyor ve global bi counters sözlügü aldi.

ardindan tanimladigimiz fonksiyonları bu counter'a vererek, closure'ı geri aliyoruz. her cagirdigimizda counter'i bu sözlüge append ediyor.

en son fonksiyonu direkt bu closure'a esitledik. aslinda decorator mantigi da bu.
bu add fonksiyonunu kendi counter sinifimizla wraplemis olduk.
```
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
#decorator'e benziyor. add fonksiyonunu sarmaladik counter ile.
add = counter(add, c)
add(2,3)
print(c)
```

--- 
## 4. DECORATORS
--- 

### Decorators Generally:

- takes a function as an argumen
- returns a closure
- closure usually accept (*args, **kwargs) : any type of argument
- run some code in the closure (inner func)
- closure fonksiyon, aslında original fonksiyonu bu input parametrelerle cagirir kendi ekstra islerini de yapar
- sonuc olarak bu original fonksiyonunu yaptigi isi return edebilir.

önceki örneklerde add fonksiyonunu decorate etmiştik aslında counter ekleyerek. ```add = counter(add)``` bu işe yaramıştı. genel olarak da böyle yapabiliriz
``` my_func = func(my_func)```

ya da python'ın bizim icin yaptigi bi güzellik var. bu şekil yerine ```@``` sembolunu kullanarak da bu isi yapabiliriz.
```
@counter
def add(a, b=0):
    return a+b
```


```
### LOGGER DECATOR

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)

        print(f"{run_dt} --- {fn.__name__} called.")
        return result

    return inner


#fonksiyona en yakın hangi decorator varsa ilk onla wraplenir.
@logged
@timer
def func_1(x : int, y : str):
    time.sleep(1)

#func_1 = logged(timer(func_1)) -> bunla ayni sey.
func_1(5, "batuhan")
```
son wrapleyen decarotor haliyle ilk cagiriliyor
mesela bi app olsun. authenticate oldugunda log basalim

o zaman ilk authenticate ile wraplicez ve kontrol yapicaz.

sonrasinda kontrolu gecerse log basicaz.
```
#burada soyle bir mentalite oturtulabilir.
print("\n---\n\n\n---\n")
name = "batuhan"
def auth(fn):

    @wraps(fn)
    def inner(*args, **kwargs):
        global name
        if name != "batuhan":
            print("auth is failed")
            return
        
        return fn(*args, **kwargs)
    return inner

@auth
@logged
def my_func():
    print("my_func is called")

my_func() #-> auth successed.

name = "root"
my_func() #-> auth failed

```

--- 
### DECORATOR PARAMETERS
--- 
decoratorler de parametre alabilir
aynı lru_cache'de oldugu gibi
lru cache özellikle recursive func'larda ya da gecmis cevaplari tuttugumuz ve hiz kazandirmak istedigimiz fonksiyonlarda, memory'den feda ederek bir cahce tuttugumuz yapi. First In First Out yapisinda bir cache tutuyor. Yani cache'e yeni eklemeler yaparken eskilerini cikartiyoruz.
```
from functools import lru_cache
@lru_cache(max_size=16)
def factorial(n:int)->int:
    return 1 if n < 2 else factorial(n-1)
```

- mesela timed decorator'ına avg hesaplayacak ve iterasyon kosacak yeni bir parametre ekleyebiliriz.

```
def timed(func):
    from time import perf_count
    def inner(*args, **kwargs):
        start = perf_count()
        ret = func(*args, **kwargs)
        end = perf_count()
        elapsed = end - start
        return ret
    return inner

@timed
def factorial(n:int)->int:
    return 1 if n < 2 else factorial(n-1)
```

yukarıdaki örnekte timed yeni bir parametre alsa

```timed(func, iterNum)``` olsa <br>
```@timed(10)```  seklinde tanimlayamayiz.

burada söyle düsünmek lazım. timed(10) aslında bize bir decorator nesnesi donsun. Ben de onu @ ile bildirmis olayim. bunu saglamak icin de nested func'lar kullanabiliriz. decorators-2.py'de mevcut.

