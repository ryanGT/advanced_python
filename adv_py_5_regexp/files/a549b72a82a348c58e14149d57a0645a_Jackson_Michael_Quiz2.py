import matplotlib.pyplot as plt
import numpy as np


def TimePlot(frequency, figNum): 
	
	#Always want to create three periods no matter what the freq is
	Period = 1/frequency
	PeriodRange = Period*3
	dt = Period/100		
	
	t = np.arange(0,PeriodRange,dt) # to get the one second interval
	y = np.sin(2*np.pi*frequency*t) #standard form sin(wt)
		
	plt.figure(figNum)
	plt.clf()
	plt.plot(t,y,'r')
	plt.xlabel('$Time(seconds)$')
	plt.ylabel('$y_'+str(figNum)+'(t)$')
	plt.title(str(frequency)+' Hz. Sine Wave')
	plt.savefig(str(int(frequency))+' Hz Sine Wave.png',dpi=300) #used int to get rid of floating point so no dots in name
	plt.legend(['$y_'+str(figNum)+'(t)$'],3)
	
	return


freq = [3.0,10.0,50.0] #frequency of sine waves(need to be floating point)

for i in range(len(freq)): #by putting in more frequency values into the array above,
#the for loop will automatically adjust how many plots will be created.
	TimePlot(freq[i],i+1)

plt.show() #Put this down here so the plots will show up at the same time	


