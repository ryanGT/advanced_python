import matplotlib.pyplot as plt
import numpy as np
# Asks for the total number of
quan = input("How many functions would you like to plot? \n")

    
# This is a function that has the frequency passed in and plots the wave
def plot(z):
    
    t = np.arange(0.0, 1/z ,0.001/z)
    y = np.sin(2*np.pi*z*t)
    plt.figure(i)
    plt.plot(t,y)
    filename = 'fig_%i.png' % i
    plt.savefig(filename, dpi=300)
    
# A for loop that runs the number of times requested, asks for the
# frequency, then calls the function to execute the plotting    
for i in range(0,quan):
    z = float(input("Enter the frequency: \n"))
    plot(z)
    
