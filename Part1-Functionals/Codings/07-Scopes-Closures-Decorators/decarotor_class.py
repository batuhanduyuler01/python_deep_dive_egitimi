#gectigimiz zamanlar yaptigimiz gibi basitce decorator factory:

def decorator_factory(*,repeat_number = 1):
    
    def dec(func):

        def inner(*args, **kwargs):
            
            for _ in range(0, repeat_number):
                resp = func(*args, **kwargs)
                
            print(f"function is repeated {repeat_number} times")
            return resp
        return inner
    return dec


@decorator_factory(repeat_number=10)
def my_func():
    print("Hello World")
    return 0

class MyDecoratorClass:
    def __init__(self, *, reps=1):
        self.reps = reps

    def __call__(self, fn):
        print("my class invoke method called.")
        def inner(*args, **kwargs):
            import time
            time.sleep(1)
            print("decorated function called")
            for _ in range(0, self.reps):
                resp = fn(*args, **kwargs)

            print(f"function is repeated {self.reps} times")
            return resp
        return inner

@MyDecoratorClass(reps=5)
def my_fn():
    print("Bye Bye World!")
    return 0

my_fn()






