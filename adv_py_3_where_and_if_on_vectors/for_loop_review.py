mylist = ['a','b','c','d']

for item in mylist:
    print('item = %s' % item)


N = len(mylist)

for i in range(N):
    print('i = %i' % i)
    item = mylist[i]
    print('item = %s' % item)
    print('='*20)
