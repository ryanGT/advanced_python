from matplotlib.pyplot import *
from numpy import *

# create the time vector
t = arange(0,1,0.01)
# create the y vector
y = 2.0*sin(2*pi*t)

if y > 1.5:
    y = 1.5
elif y < 1.5:
    y = -1.5


