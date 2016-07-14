from matplotlib.pyplot import *
from scipy import *

# create a time vector and the y vector
t = arange(0,1,0.001)
y = 2*sin(2*pi*t)

# create a copy of y for the dashed line
import copy
y_sat = copy.copy(y)

figure(1)
clf()
plot(t,y,'r--')

y_sat[y_sat > 1.5] = 1.5
y_sat[y_sat < -1.5] = -1.5

# plot the results
plot(t,y_sat,linewidth=2.0, label='$y(t)$')
ylabel('$y(t)$')
xlabel('Time (sec.)')
legend(loc=1)

# show the plot on the screen
show()
