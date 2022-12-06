from functools import wraps

counters = {}

def counter(fn):
    """
    counter fonksiyonu input olarak bi fonksiyon ve counter sözlük aliyor.
    sonrasinda bi fonksiyon ile closure olusturuyor. ve bu fonksiyona input alarak 
    original func return edecek sekilde hazirlanan inner'i donuyor
    """
    global counters
    cnt = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal cnt 
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    #inner = wraps(fn)(inner)
    #wraps burada original func'in isim, imza, docstring gibi parametrelerini decorate edilmis func(inner)'a gömüyor.
    return inner


def add(a, b=0):
    return a+b

@counter
def mult(a, b=0):
    return a*b

add = counter(add)
print(add.__name__)

add(10,15)
add(15,20)
mult(3,2)

print(counters)


# simple timer application with decorator

import time
from functools import wraps

def timer(fn):

    @wraps(fn)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result =  fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"function executs in {end - start} seconds")
        return result

    return inner

@timer
def wait_some_time(sleepTime : int):
    print("started to waiting")
    time.sleep(sleepTime)
    print("sleep is finished.")


#1 1 2 3 5 8 13 21 34 ....
def calculate_fibonacci(n):
    if (n <= 2):
        return 1
    else:
        return (calculate_fibonacci(n-1)) + (calculate_fibonacci(n-2))

@timer
def calculate_fib(n):
    return calculate_fibonacci(n)


@timer
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1

    for i in range(3, n+1):
        # c++ yoluyla boyle
        # tmp = fib_2
        # fib_2 = fib_1 + fib_2
        # fib_1 = tmp

        # python yoluyla
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


#cacheleme yaptigindan fib loops cok daha hizli
#34. fibonacci sayisi ne?
# print(f" fib loops : {fib_loop(34)}")
# print(f" fib recursive : {calculate_fib(34)}")
    

# LOGGER DECATOR

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

my_func()

#cagirilma sirasi wraplenme sirasi gibi. ilk auth cagiriliyor.

name = "root"
my_func()

