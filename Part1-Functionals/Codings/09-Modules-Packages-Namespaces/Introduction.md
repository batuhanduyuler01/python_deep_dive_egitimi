# Modules

Modules -> aslında object of type ModuleType


```
def func():
    a = 10
    return a

globals()['func']() -> returns 10
```

burada ne yapmıs olduk? <br>
aslında globals bize namespace'leri donduruyor. ben global namespace'teki func elemanını aldim
callable oldugundan da cagirabildim. 


```
a = 20
def my_func():
    a = 10
    b = 20
    print(locals())

print(globals())
```

my_func icinde cagirdigim locals() aslında sadece a ve b'yi donecektir.

```
import fractions

print(fractions) -> dosya yolundaki modulu gosterecektir.
#<module 'fractions' from '/opt/local/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/fractions.py'>
```


```
import math
print(id(math))

import math
print(id(math))
```
aynı adresi basacaktır. cünkü import ettigimizde aslında system cache'e ekliyoruz bu modulu.

```
import sys
sys.modules['math']

id(sys.modules['math'])
```
burada aslında reload ederken, python once system cache'ye bakar. Eğer orda varsa reload etmez.


bunun disinda modullerin ozelliklerini de dir(mod) diyerek neler tanimlanmis gorebiliriz
```
from x import y
import x

dir(x)

x.hello = lambda : print("hello")

hello_func = getattr(x, 'hello')
hello_func = x.__dict__["hello"]
#bu ikisi ayni sey.
#x'in dict icinde sahip oldugu memberlari vardi zaten.

hello_func()
#hello
```
--- 
## 2. Importing Modules
--- 
python, import islemlerini run time'da yapiyor yani gercekten kodumuz kosarken.
<br>c, c++ gibi dillerde, modullerin compiling ve linkleme islemleri compile time'da yapiliyor.

iki türlü de sistemin bu modulelrin nerede oldugunu bilmesi lazım.

python nerede yüklü?
```
import sys
sys.prefix
```

cpython üzerinde calisiyoruz. yani kullandigimiz builtinler (dict, list vb.) <br>aslında c dilinde yazilmis. bu C binary'lerinin nerede oldugunu gormek icin:
```
sys.exec_prefix
```
komutunu kosabiliriz. aslında bir virtualenv yaratırken bu prefix, exec_prefixlerin konumu farklı bir yer yapiyoruz o yeni bir env yapiyor.

```
sys.path
```
bu komutta yer alan yerlere bakıyor aslında importing yaparken python.

yeni bir import yaparken de aslında sys'nin cache'sine bakılıyor ve reload buna gore yapilmayabiliyor. high levelde sırayla su islemler yapiliyor

1. sys.modules 'un cache'sine bakiliyor, eğer orda module bulunursa direkt referansı donuluyor yoksa 2.adıma geciliyor.
2. yeni bir module object olusturuluyor (types.ModuleType)
3. source code, dosyadan load ediliyor.
4. sys.modules'e dosya ismi ve load edilen modul, dict'e append ediliyor (key-value)
5. compile ve executing source code islemi gerceklestiriliyor.

```
#module1.py

print("module1 called")

class Module_1:
    def __init__(self):
        print("module 1 class is invoked")
```

```
#main.py
import module1

print("main.py")

import module1
```

-> module1 called
-> main.py

yani module1 import edildigi yerde module1 kodunu kosuyor.<br>
sonrasında tekrar module1 import ettigimizde cache'te oldugundan dolayi tekrar kodu kosmuyor.

ancak :
```del globals()["module1"]``` dersek cache'ten kaldirmis oluruz.

--- 
python module import ederken söyle davranabilir:

```compile``` ve ```exec``` fonksiyonlarını sırasıyla kullanır.
```compile``` aslında bize bir ```python byte object``` üretir. 
```exec``` ile de onu kosar.


--- 
modulleri kendimiz import edecegimiz fonksiyonlar yazmıstık.

bunun disinda ```importlib``` kütüphanesini kullanarak da bu islemleri yapabiliriz
```
module_name = 'math'
import module_name -> calismayacaktir.

import importlib
math = importlib.import_module(module_name)
```
bu sekilde de gerceklestirebiliriz.

```
print(importlib)
print(fractions)
```
dedigimizde dosya yollari cikacaktir.

```
....\importlib\\__init__.py
....\Anaconda3\\lib\\fractions.py
```
.py uzantılı dosyalar gözüküyor.

bazen de .pyc uzantılı dosyalar cikabilir. bunlar c ile derlenmis dosyalardir.
.pyd dll'ler cikabilir. <br>veya .zip dosyalardan bile import edebiliriz bazi seyleri.

- finders : finds the module wanna import and finds the related loader.
- loaders : loads the modulea
- finder + loader = importer

```
print(sys.meta_path)
```
dersek builntinimporter, frozenimporter, pathfinder gibi bu nesneleri görebiliriz

burada python gidip önce builtinimporter, frozenimportera soruyor.

eğer module1'i göremezse pathfinder'a gidiyor ve bu path var mı diye bakıyor

bulursa modulu importluyor. bunun gibi kendi pathfinderlarımızı bir database'de arama yapmasi gibi gibi yazabiliriz veya zip dosyasi arama vb.

bunun disinda mesela farklı dizinlerde moduller yazdik diyelim
```
import os
ext_module_path = os.environ["HOME"] #kendi root directory'im
file_abs_path = os.path.join(ext_module_path, 'module2.py')
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py ...')\n")
    code_file.write("x = 'python'\n")
```
burada aslında ext_module_path ile root dizini mi aldım ve module2.py ile birlesitirip dosya dizinimi olusturdum ve dosyaya birkac sey yazdim.

```
importlib.util.find_spec("module2")
```
bu sekilde modulu bulamayacam cünkü ```sys.path``` icerisinde yer almiyor bu dizin.

```
sys.path.append(ext_module_path)
```
bu sekilde modulumu yarattigim dizini sys'in path listesine ekledim ve artik importlib arama yapacagi zaman bu dizine de bakacak
```
importlib.util.find_spec("module2")
import module2
```
dedigimiz zaman artık basarili bir sekilde modulu bulacak ve import edebilecektir.

--- 
NOT:

```
from math import *
import math
```
yukarıdaki iki import aslında bi noktada farklı.
ikisinde de module import ediliyor ve sys cache'ye yaziyoruz. ancak :

- ilkinde, moduldeki tüm parametreleri, kendi py dosyamdaki global namespace'e aktariyorum. yani ileride bir ```pi``` degiskeni tanimlasam ```math.pi``` degiskeninin yerini almis olacak.

- ikincisinde import ettim ama kendi ```pi``` degiskenim ile ```math.pi``` degiskeni farkli.
--- 
### Reloading Modules

```
#test.py
print("reloading test...")
```
```
#main.py
import test
#reloading test...


'test' in sys.modules -> TRUE

import test
#nothing---

del sys.modules['test'] -> memory adresi temizledik
import test
#reloading test...
```

yani sys'nin cahce'sinden temizlemedigimiz sürece, modulu reload edemiyoruz cünkü referansı bulup aynı referanstan devam ettiriyor.

- ama sys.cache'den silmeden once baska yerler de bu test modulunu import etmis olabilir. bu yüzden yeterli olmayabilir.

- bu sebeple importlib kullanabiliriz. importlib referansı degistirmiyor (memory adres sabit kaldı) ancak bu adresin icerigini update ediyor. yani safe bir approach! ama production'da tehlikeli!
```
import importlib
importlib.reload(modul)
```

--- 
## USAGE OF MAIN
--- 

bulunduğumuz dizinde usage_of__ main__ diye yeni bir dizin olusturduk. ne ise yarar bu __ __main__ __ ?

bir modul tanimladik ve run.py'de import ettik. eger run.py'de o modulun ismine bakarsak ```__ name __``` ile, modul ismi oldugunu görürüz. main.py'nin ismi ise ```__ main __```olacaktir. 
```
#run.py
import modul1

print(__name__)
print(modul1.__name__)
```
```python3 run.py```<br>
dersek ilkinde main'i basar sonrasinda modul1'i.
ancak direkt <br>```python3 modul1.py``` dersek bu sefer'de modul1'in ismi main olmus olacaktir. bu sebeple modullere 
``` 

if __name__ = "__main__":
    #some code
```
şeklinde bi main func koyabiliriz. bu sayede bi modul hem baska yerden import edilebilir hem de kendi calistirilabilir hale gelir.

ayni zamanda python argumentparser kütüphanesi yardimiyla bu modullere command line input parametre vererek vs biz de kullanabiliriz.

```
python3 modul1.py -r 10 -p "batuhan"
```
10 kere tekrar et batuhan yaz gibi argümanlar ekledigimizi düsünürsek, terminalden bu sekilde cagirilmasi gereklidir.

- Bunlarin disinda python <"file"> dedigimizde aslında python gidip ```__ main __``` arıyor. bu noktada :

```
python3 usage_of_main__
```
seklinde direkt dizin adini python ile cagirirsam, o dizinde ```__ main __``` var mı diye arayacak ve buldugunda onu calistiracaktir.

--- 
# Packages

- Paketler aslında moduledür. ama her modul package degildir.

- Paketler, icerisinde modul barındırabilir veya sub-package barındırabilir.

- Eğer bir modul, package ise muhakkak ```__ path __ ``` attribute'u olmalıdır.

```
import x
if x.__path__ != empty :
    IT IS A PACKAGE
else:
    IT IS A MODULE
```
