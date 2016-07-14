# satureate sine wave for loop
from matplotlib.pyplot import *
from numpy import *

# create the time vector
t = arange(0,1,0.01)
# create the y vector
y = 2.0*sin(2*pi*t)

# I think this is the slowest and least
# elegant solution, but it is the clearest
# to understand

N = len(y)
y_sat = zeros(N)

for i in range(N):
    y_i = y[i]
    if y_i > 1.5:
        y_sat[i] = 1.5
    elif y_i < -1.5:
        y_sat[i] = -1.5
    else:
        y_sat[i] = y_i
        
figure(1)
clf()
plot(t,y,'r--')
plot(t, y_sat, label='$y(t)$', linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time (sec.)')
legend(loc=1)

show()
