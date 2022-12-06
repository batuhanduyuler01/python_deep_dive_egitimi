import random

sequence = [random.randint(1,100) for i in range(10)]
print(sequence)


#old way
def find_maksimum(seq : list)->int : 
    maks = seq[0]
    for elem in seq:
        if (elem > maks):
            maks = elem
    return maks

print(f"old way : {find_maksimum(sequence)}")


#reduce way
from functools import reduce
comparison_func = lambda x, y : x if x > y else y
print(f"reduce way maks element : {reduce(comparison_func,sequence)}")


#aslında reduce suna benzer bi sey
#sifirinci elemandan itibaren en buyugu bul

def _reduce(fn, iterable):
    result = iterable[0]
    for elem in iterable[1:]:
        if elem > result:
            result = elem
    return result
        
#some with reduce
res = reduce(lambda x,y :  x+y, sequence)
print(f"Result for addition process {res}")


#any function'ını reduce ile yazmak

mylist = [0, '', None, 100]
#100 Truthy oldugundan True doner
print(any(mylist))
# 0, '', None Falsy Truthy olmadigindan false
print(all(mylist))


resultAny = reduce(lambda x, y: bool(x) or bool(y), mylist)
print(resultAny)

resultAll = reduce(lambda x,y : bool(x) and bool(y), mylist)
print(resultAll)

myl = [random.randint(1,10) for i in range(3)]
#find multiplication of elements with reduce
resultMu = reduce(lambda x, y: x * y, myl)

print(myl)
print(resultMu)