# aslında burada bir dağıtıcı app'i yapmak istiyoruz.
# bana gonderilen elemanları türüne göre html formatina cevirmeliyim ancak int de gelebilir float da string de gibi gibi

# bunu c++'da function overloading'le basitçe yapıyoruz aslında. ama python default'da function overloading yok.
# bu sebeple fonksiyonları ayrı ayrı tanımlamalı ve if-else ile general bi func tanimlayabiliriz.


from html import escape

def html_escape(arg):
    return escape(str(arg))
                      
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))
                                  
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')
                                  
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
                                  
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

#html_list([1,2,3]) burada cagirmak sikinti!!!

from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))


myStr = """ batuhan
    duyuler
    """

myInt = 3

myL = [myStr, myInt]

# print(htmlize(myL))

### Burada bir circular reference var aslında. ancak ilk hangi fonksiyonu cagirdigimiz yer onemli oldugundan sikinti yok.
#  yani htmlize -> htm_list cagiriyor
#  htm_list -> htmlize cagiriyor.
# ilk htm_list cagirsak sikintiydi. ancak ilk htmlize cagirdigimizdan problem yok.



#single argument dispacther yapalim
#aslinda base class bir dispatcher gibi düsünebiliriz c++'ta. derived'da fonksiyon nasıl üretilmisse oraya yonlendiriyor.

def singledispatch(fn):
    registry = dict()

    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    def decorator(arg): #single argument
        fn = registry.get(type(arg), registry[object]) # eger registry dict'te bu arguman yoksa, default olan registry[object]'i don. default func gibi düsün.
        return fn(arg)

    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorator.register = register
    decorator.registry = registry.keys()
    decorator.dispatch = dispatch
    return decorator


@singledispatch
def htmlize(arg):
    return escape(str(arg))
                      
@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

@htmlize.register(str)
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


# htmlize = singledispatch(htmlize)
# artık htmlize bir decorator ve closure ile birlikte.
# closure icerisinde registry sozlugu de tanimli. unutmamak lazim
# htmlize.register fonksiyonu (yani closure-decoratorun fonksiyonu ile)


# html_int = htmlize.register(int)(fn) -> bu islem registry[int] = html_int yapmamizi sagliyor ve html_int'e closure donmus olduk
# yoksa tanimlama yapamiyorduk


print(htmlize.registry)
print(htmlize.dispatch(int))
