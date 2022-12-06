#aslında unpacking islemi yapmaya yarayan bi muhabbet.

#ör :

x, *y = [1,2,3,4,5]
#bu kullanimda x = 1, y = [2,3,4,5] oluyordu.
#simdi func parametresi yaptigimizda, a ve b'den sonra girilen her eleman *args unpack edebilir

def my_func(a, b, *args):
    print(f"\na * b : {a*b} \n rest of the elements:\n")
    for i, elem in enumerate(args):
        print(f"{i}. elem after b is : {elem} \t")


my_func(10, 20, 'batuhan', 0xFF, True, [1,2,3,4]) 

#burada my_func'a 6 elemanlı bir liste verip unpack ederek input saglayabilirdik.
#ör:
inputList = [10, 20, 'batuhan', 0xFF, True, [1,2,3,4]]
my_func(*inputList)

# *args'dan sonra yeni parametre ekleyemiyoruz.
# my_func(a, b, *args, d) -> illegal.

##################################################################

# positional arguments ve keyword arguments'i görmüstük
# fonksiyonda my_func(a=10, b=20) gibi cagiriyorsak keyword arg veriyoruz
# fonskyinoda my_func(10, 20) gibi veriyorsak positional arg veriyoruz.
# bi fonksiyonda keyword arg almaya zorlamak icin *args kullanabiliriz:

def force_keyword_arg(a, b, *args, d):
    print("d keyword arg almak zorunda!")


# force_keyword_arg(10, 20, 30, 40, 50)
# yukaridaki ornekte :TypeError: force_keyword_arg() missing 1 required keyword-only argument: 'd'
# hatasini basacaktir.

force_keyword_arg(10, 20, (10,20,30), d=10) # dogru kullanim!

# eger hic positional arg almak istemiyorsak
def force_only_keyword_arg(*, a, c):
    print("only keyword args")
    print(a, c)

# force_only_keyword_arg(10, 20) -> hatali kullanim asagidaki logu basar
# TypeError: force_only_keyword_arg() takes 0 positional arguments but 2 were given

force_only_keyword_arg(a = 50, c = 51)

# bu * elemanı da *args gibi ortalarda olabilir. o zaman ondan öncekiler positional sonrakiler mandatory keyword
def force_keyword_from_middle(a, b, *, c):
    print(a, b, c)

force_keyword_from_middle('burada', 'zorunlu olan', c='sadece c')

##################################################################

# **kwargs
#Burada *args'tan farkli olarak gelen parametreler positional degil kword olmak zorunda
# *args aslinda tuple olarak packing yaparken **kwargs dictionary olarak packing yapiyor.

def kwarg_example(a, b, **kwargs):
    print(f"kwargs are: {kwargs}")

kwarg_example(10, 20, c = {'a':0x01}, batu=True, duyuler=False)

#**kwargs sonrasi func eleman alamaz. genel kullanimda soyle olabilir

def general_func(*args, **kwargs):
    pass