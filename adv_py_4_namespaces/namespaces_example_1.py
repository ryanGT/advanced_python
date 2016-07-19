a = 7

def myfunc1():
    print('in myfunc1, a = %i' % a)
    b = 3
    c = a + b
    return c


def myfunc2(a):
    b = 3
    print('in myfunc2, a = %i' % a)
    c = a + b
    return c

print('before calling myfunc1, a = %i' % a)
c1 = myfunc1()

c2 = myfunc2(3)
print('after calling myfunc2, a = %i' % a)
