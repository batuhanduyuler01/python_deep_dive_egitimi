from functools import wraps
def timed(reps):
    def decorator(fn):
        
        #closure olarak donecegiz.
        @wraps(fn)
        def inner(*args, **kwargs):
            from time import perf_counter
            total_elapsed = 0
            for i in range(0, reps):
                start = perf_counter()
                ret = fn(*args, **kwargs)
                end = perf_counter()
                elapsed = end - start

                total_elapsed += elapsed
            
            avg = total_elapsed / reps
            print(f"avg time : {avg}")
            return avg
        return inner
    return decorator


#reps aslında bir free variable. inner'a bagli degil timed'a da öyle.
#timed bir decorator ve bunu donuyoruz. decorator de reps ne biliyor.


#outer(n) -> aslında decorator donduruyor.
#artik o decoratore func verebiliriz.

#eski usul 
#my_func = timed(my_func)
#yeni usul
#my_func = outer(10)(my_func)
#burada aslında outer(10) -> timed decoratorunu donuyor.

@timed(10)
def factorial(n):
    print("hello world")


factorial(5)