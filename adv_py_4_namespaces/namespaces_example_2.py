a = 7

def goodfunc1():
    print('in goodfunc1, a = %i' % a)
    b = 3
    c = a + b
    return c


def badfunc():
    a += 1
    b = 3
    print('in badfunc1, a = %i' % a)
    c = a + b
    return c


def goodfunc2(a):
    a += 1
    print('in goodfunc2, a = %i' % a)
    b = 3
    c = a + b
    return c


print('before calling goodfunc1, a = %i' % a)
good1 = goodfunc1()

#bad1 = badfunc()

print('before calling goodfunc2, a = %i' % a)
good2 = goodfunc2(a)

print('at end of script, a = %i' % a)

