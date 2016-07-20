from matplotlib.pyplot import * ## imports to global namespace
from numpy import * ## imports numpy library to gloabal namespace


def plotfun(numplots,freq):
    for i in range(0,numplots):
        u = arange(0,1,0.05) 
        y=sin(freq*pi*u) 
        figure(2)
        clf() 
        plot(u,y)
        xlabel('Time (sec)') 
        ylabel('Amplitude') 
        title('Hz Sine Wave') 
        savefig('myplot2.png',dpi=300) 
        show() 
    print "Done"    
        

iterations = raw_input("Enter total number of plots to generate: ")
freq = raw_input("Enter in the frequency of the plot desired: ")

plotfun(int(iterations),float(freq))

t = arange(0,1,0.01) 
y=sin(6*pi*t) 
figure(1)
clf() 
plot(t,y)
xlabel('Time (sec)') 
ylabel('Amplitude') 
title('3 Hz Sine Wave') 
savefig('myplot1.png',dpi=300) 
show()


u = arange(0,0.5,0.001) 
y=sin(20*pi*u) 
figure(4)
clf() 
plot(u,y)
xlabel('Time (sec)') 
ylabel('Amplitude') 
title('10 Hz Sine Wave') 
savefig('myplot2.png',dpi=300) 
show() 


v = arange(0,0.1,0.001) 
y=sin(100*pi*v) 
figure(3)
clf() 
plot(v,y)
xlabel('Time (sec)') 
ylabel('Amplitude') 
title('50 Hz Sine Wave') 
savefig('myplot3.png',dpi=300) 
show()

