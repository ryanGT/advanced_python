#created by: Michael Jordan

from matplotlib.pyplot import * #imports all functions from pyplot into the global namespace
from numpy import *             #imports all functions from numpy into the global namespace

#defines a function that can be used for plotting a sine wave at any frequency
#sets default values to plot a 2Hz sine wave
def plotFunc(hz=2, clrFig=True):
    dt=0.001
    endGraph=2*hz**-1
    t=arange(0,endGraph+dt,dt)  #sets amount of time for sampling to specified duration second
    y=sin(2*pi*hz*t)            #defines what sine wave to plot
    figure(1)
    if clrFig==True:
        clf()                   #clears the figure so that multiple sine waves are not plotted on top of one another
    plot(t,y)                   #plots t vs y
    title('Frequency vs. Time') #titles the figure
    xlabel('Time(sec)')         #labels the x-axis
    ylabel('Frequency (Hz)')    #labels the y-axis
    
plotThese=[3,10,50]             #any frequency you want to plot can be entered in this list

N=len(plotThese)                #finds out how many graphs will need to be plotted

for a in range(N):
    i=plotThese[a]              #pulls the number out of the list so you dont need to use 'plotThese[]'
    plotFunc(i)
    savefig("plotFig(%iHz).png"%i,dpi=300)
    print(i)                    #prints all the frequencies it graphs so you can tell where it breaks
    
show()                          #will show the last graph created, the others must be opened manually
