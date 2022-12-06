#fibonacci serisini for loop ve recursion ile yapmistik.
#daha once buldugu degerleri tekrar bulmasini engellemek icin cahce yapisi 
#koyarak recursion'in ileriki asamalarinda kisa sürmesini saglayabiliriz
#ancak bu durumda memory'den fedakarlik yapmis oluyoruz bu unutulmamali.



class Fib:
    def __init__(self):
        self.cache = {1 : 1, 2 : 1}

    def fib(self, n):
        if n not in self.cache:
            print(f"calculating fib for {n}")
            self.cache[n] = self.fib(n-1) + self.fib(n-2)

        return self.cache[n]


f = Fib()
print(f"\n result is: {f.fib(9)}\n")

# ayni islemleri fonksiyonla da yapabiliriz
def cached_fibonacci():
    cache = {1:1, 2:2}

    def calc_fib(n):
        nonlocal cache
        if n not in cache:
            print(f"calculating fib for {n}")
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

    return calc_fib

c = cached_fibonacci()
print(f"\n result is: {c(9)}\n")
print(f"\n result is: {c(9)}\n")


# ya da decorator kullanarak yapabiliriz.

def memoize_fn(fn):
    cache = {}

    def inner(n):
        if n not in cache:
            print(f"calculating fib for {n}")
            cache[n] = fn(n)
        return cache[n]
    return inner


@memoize_fn
def fib(n : int)->int:
    if (3 > n):
        return 1
    else:
        return (fib(n-1)) + (fib(n-2))
    #return 1 if n < 3 else fib(n-1) + fib(n-2)        

print(f"\n memoize result is: {fib(20)}\n")
print(f"\n memoize result is: {fib(20)}\n")


#python bizim icin lru_cache yapmis functools icinde
#last recent used cache
#cahce size'i belirleyebiliyoruz.
#ve yeni hesaplamalar yaptigimizde FIFO prensibine uygun sekilde
#ilk eklenen degerleri cache'den cikartiyor
#max size = None dersek sinirsiz cacheliyor

from functools import lru_cache

@lru_cache(maxsize=8)
def fibo(n : int)->int:
    print(f"Calculating {n} ...")
    return 1 if n < 3 else fibo(n-1) + fibo(n-2)

print(f"\n lru cache result is: {fibo(8)}\n")
print(f"\n lru result is: {fibo(8)}\n")
print(f"\n lru result is: {fibo(9)}\n") #cahce'den 1i cikartti 9u ekledi
print(f"\n lru result is: {fibo(1)}\n") #1i tekrar hesaplıcak
print(f"\n lru result is: {fibo(16)}\n") #16-9 cachledi
print(f"\n lru result is: {fibo(8)}\n") #hepsini tekrar hesaplıcak





