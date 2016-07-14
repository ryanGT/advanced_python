raw_a = raw_input("Enter a positive number: ")

try:
    a = float(raw_a)
except ValueError:
    print('You must enter a number')
    raw_a = raw_input("Enter a positive number: ")
    a = float(raw_a)

assert (a > 0), "A is not positive"

b = 7.0
c = a + b

print('c = %s' % c)
