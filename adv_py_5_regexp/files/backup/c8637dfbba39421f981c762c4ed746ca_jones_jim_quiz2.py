# Quiz 2
# Jim Jones
# ME 492

from numpy import *
from matplotlib.pyplot import *


inputs = [3,10,50]	# desired frequencies

def plotsine(f,fignum):
	T = 2./f		# 2 periods
	dt = 1./(100*f)	# 100 data points per periods
	x = arange(0,T,dt)
	y = sin(f*2*pi*x)
	figure(fignum)
	plot(x,y,label='%iHz Sine Wave'%f)
	xlabel('Time (sec)')
	ylabel('Amplitude')
	title('Sine Wave with Frequency of %i Hz'%f)
	legend(loc=4)

for i,freq in enumerate(inputs):
	plotsine(freq,i+1)
	savefig('quizfig_%iHz.png'%freq)
	
show()	# This could be added into the function.
		# Adding it would give more speed, but less flexibility
