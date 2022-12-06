# First Class Functions 
---
## 1. Introduction
--- 
Python'da tüm fonksiyonlar aslında first class functions.

-> First Class Objects:
- bir fonksiyona arguman olarak gecilebiliyorsa first class object'tir.
- fonksiyon tarafından return edilebilmelidir.
- bir variable'a assign edilebilmelidir.
- list, tuple, dict gibi veri tiplerinde store edilebilmelidir.


* şuana kadar gördügümüz tüm objeler first-class obje (int ,float, list etc.)
* bu sebeple fonksiyonlar da first class object diyebiliriz.

-> Higher Order Functions

- Arguman olarak fonksiyon alabilmeliler.
- Fonksiyon return edebilmeliler. (decorators, closures ...)
- built in higher order functions : sorted, map, filter...

--- 
## 2. Docstrings and Annotations
--- 
---> Docstrings
* help(x) ---> eğer x hakkında bir documentation varsa bunu geri döndürür.
* eger fonksiyonun ilk satırı stringse (yorum degil) ve bir seye assign edilmiyorsa docstring olur.
* parametreleri : ile belirttiğimizde bu da annotations olur. __annotations_ property'de saklanır.

- fonksiyon  __ __doc__ __ property'de saklanır.<br>
```
def my_func(a : str, b: int, *args : 'extra arguments') -> str :
    """
    bu func şu amaçla kullanılır...
    bd'ye aittir.
    """

print(my_func.__doc__)
help(my_func)
```
yukarıdaki ikili aynı kapıya cikar.

--- 
## 3.Lambda Expressions

---
- Another way to create functions
- sıkıntısı sadece one line olması. cpp gibi multi line yazamiyoruz
```
lambda [parameter list] : expression
```

- memory'de yer alan bir function obj yaratir.
- kullanmak icin bu obj'yi call etmek gerekir.
- lambda : anynmous function'dır. closure olmak zorunda degildir.

--- 
## 4.Function Introspection
--- 
- Her fonksiyonun aslında attributeları var.
```
def my_func():
    pass

my_func.boy = 178
my_func.kilo = 93

print(dir(my_func))

ör : my_func.__name__
     my_func.__defaults__
```


--- 
## 5.Callables
--- 

- callable aslında () operatoruyle cagirilabilen herhangi bir objeye denir.

- bir sınıftan objeyi callable hala getirmek icin __ call __ fonksiyonu yazılabilir.
--- 
## 6.Map - Filter - Zip - List Comprehension
--- 
###  A. map 
inp aldigi fonksiyonu iterable'lara uyguluyor.
```
map(func, *iterables)
```
*iterable -> a variable number of iterable objects 
func -> bi fonksiyon. iterable sayısı kadar input alabilir

- shortest iterable bittiginde, map func biter.

### B. filter
```
filter(func, iterable)
```

-single iterator ve single func alir.

* iterable-> single iterable
* func -> function that takes single argument

gercekten de bi iterator gezip filtreliyoruz. Burada bu inputu aldıktan sonra fonksiyonun geri dönüs degeri True ise kaliyor, False ise dropluyoz.

Eger fonksiyon olarak None versek, sadece 0 false olacagindan kalan elemanlar Truthy olur ve droplanmaz.

### C. zip
```
zip(*iterables)
```

- en az elamanı olan iterable kadar, tüm iterableları birleştirir.

### D. list comprehension
```
[ <expression> for <varname> in <iterable> ]
```

ÖR: asagidakiler ayni sey
```
list = [1,2,3,4]
lsquare = list(map(lambda x : x**2 , list))
lsquare2 = [x**2 for x in list]
```

ÖR: asagidakiler ayni sey MAP
```
l1 = [1,2,3,4]
l2 = [-1,-2,-3,-4]

res1 = list(map(lambda x,y : x+y, l1, l2))
res2 = [x+y for x, y in zip(l1,l2)]
print(res1 == res2)
```

ÖR: asagidakiler ayni sey FILTER
```
res1 = list(filter(lambda x: x%2 == 0, l1))
res2 = [x for x in l1 if x%2 == 0]
print(res1, res2)
```

En son hali list comprehension:

```
[ <expres> for <varname> in <iterable> if <expres2>]
```

--- 

## 7. Reducing Functions

- içerisinde bir iterable alan ve çeşitli işlemler sonucunda single output return eden fonksiyonlardır. 

mesela bir listenin maksimumunu veren fonksiyonlar
bazı builtin reducing functions:

max, min, sum, any

any(iterable) -> returns True if any element is Truthy
all(iterable) -> returns True if all elements are Truthy

reduce implementasyonu az cok söyle:
```
def _reduce(fn, iterable):
    result = iterable[0]
    for elem in iterable[1:]:
        if elem > result:
            result = elem
    return result
```

asagidaki gibi reduce'la bazi islemler yapabiliriz:

```
resultAny = reduce(lambda x, y: bool(x) or bool(y), mylist)
print(resultAny)

resultAll = reduce(lambda x,y : bool(x) and bool(y), mylist)
print(resultAll)

myl = [random.randint(1,10) for i in range(3)]
#find multiplication of elements with reduce
resultMu = reduce(lambda x, y: x * y, myl)
```

reduce fonksiyonuna bir initializer verebiliyoruz.
bu durumda iterable'in basina bu initializeri koyuyor.


```
myl = [1,2,3,4,5]
#find multiplication of elements with reduce
resultMu = reduce(lambda x, y: x * y, myl, 10)
```
yukaridaki gibi yaparsak normalde 5! = 120 sonucunu alacakken listenin basina 10 koyuyor. 1200 sonucunu aliyoruz.

--- 
## 8. Partial Functions
--- 

- üç elemanlı bi fonksiyon oldugunu düsünelim
```
def my_func(a,b,c):
    print(a,b,c)
```
- bu fonksiyona a'yi default arg veremeyiz. 
- ancak bazi noktalarda a'yi default istiyorsak

```
def my_fn(b,c):
    my_func(10, b, c)
```
seklinde partial hale getirebiliyoruz.
python bunu yapmak icin bize partial lib saglamis

```
from functools import partial
partial(my_func, 10)
```
aynı islemi görür.
genelde kisaltma icin kullanabiliriz obj oriented gibi

```
def pow_fn(base, exponent):
    return base ** exponent

square_fn = (pow_fn, exponent=2)
cube_fn = (pow_fn, exponent=3)
```