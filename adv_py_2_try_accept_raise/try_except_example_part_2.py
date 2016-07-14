raw_a = raw_input("Please enter something: ")

try:
    a = float(raw_a)
except ValueError:
    print('You must enter a number')
    raw_a = raw_input("Please enter something: ")
    a = float(raw_a)
    
b = 7.0

c = a + b

print('c = %s' % c)
