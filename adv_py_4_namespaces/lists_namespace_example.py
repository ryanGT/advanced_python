mylist = [1,2,3]

def myfunc():
    a = mylist[0]
    b = mylist[1]
    mylist[0] = 7
    c = a + b
    print('in myfunc, mylist = %s' % mylist)
    return c

print('before calling myfunc, mylist = %s' % mylist)
c_out = myfunc()
print('after calling myfunc, mylist = %s' % mylist)

