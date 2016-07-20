#----------------------------------
# ME 592 Quiz 2 Part b
# Matt Carpenter
# 06/26/16
#----------------------------------

import os
from numpy import *
from matplotlib.pyplot import *


def createPlot(freq,fignum=1):
    
    sampling = 1000
    #chose 1000 Hz for more precise sampling
    dt = 1.0/sampling
    if freq < 5:                        
        end_tm = 1
    elif freq < 11:
        end_tm = 0.5
    else:
        end_tm = 0.1
    #if statement picks appropriate end time for time vector to show
    #no more than 5 periods on the graph
    time_vect = arange(0,end_tm,dt)
    sine_wave = sin(2*pi*freq*time_vect)
    figure(fignum)
    clf()
    plot(time_vect,sine_wave,'r-', label='%i Hz\nSine Wave' % freq)
    xlabel('Time (s)')
    ylabel('Amplitude of Wave')
    title('GENERATE SINE WAVE')
    legend()                                                #legend gets all label names
    savefig(os.getcwd() + '\\%iHz_Sine_Wave.png' % freq)    #unique plot name
    

myfreq = [3,10,50]  # quiz assigned frequencies

for i in range(0,len(myfreq)):          #loop through frequency array to plot separate figures
    createPlot(myfreq[i],i+1)
    
show()
