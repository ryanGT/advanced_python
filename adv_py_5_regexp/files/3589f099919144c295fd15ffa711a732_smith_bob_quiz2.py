#import the matplot library and numpy to be able to use functions such as sin
from matplotlib.pyplot import *
from numpy import *

# define a function called sine_wave with input a
def sine_wave(a):
    #create a vector over a range from 0 to 1 in increments of 0.01
    t=arange(0,1,0.01)
    #make y equal to sine values using the values from t and input from a
    y=a*sin(2*pi*t)

    #plots the values of t and y to make a sine wave
    plot(t,y)
    #make a label on the x axis
    xlabel('Time (sec)')
    #make a label on the y axis
    ylabel('y(t) (Hz)')
    #make a title over the graph and uses the string function to put the a input value in the title
    title('Quiz 2 Sine Wave '+str(a)+' Hz')
    #show the graph in a new window
    show()
    #save the graph to a png file with the input a to make a unique name
    savefig("sine_wave"+str(a)+".png")

#ask for the number of times the loop is repeated
x=input("Enter number of loops ")

#make a loop that repeats x number of times
for i in range(x):
    #ask for frequency to be used in sine_wave function
    a=input("Enter frequency ")
    #put value a into the sine_wave function
    b=sine_wave(a)
