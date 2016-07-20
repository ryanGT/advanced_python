from matplotlib.pyplot import *
from numpy import *

class sine_plotter(object):
    """Class for plotting sine waves"""
    def __init__(self, f, fs=100.0, T=1.0, amp=1.0):
        """f is the frequency of the sine wave in Hz.  fs is the
        sampling frequency also in Hz.  T is the total time for the
        plot.  amp is the amplitude of the sine wave."""
        self.f = f
        self.fs = fs
        self.T = T
        self.amp = amp


    def build_tvect(self):
        """Calculate the t vector based on fs and T."""
        self.dt = 1.0/self.fs
        t = arange(0,self.T,self.dt)
        self.t = t


    def calc_y(self):
        """Calculate the y vector"""
        self.y = self.amp*sin(2*pi*self.f*self.t)
        

    def plot(self, fignum=1, fmt='-', clear=True, label=''):
        """Plot y vs. t, calculating t and y if they don't exist yet."""
        # check if self.t has been calculated
        if not hasattr(self, 't'):
            self.build_tvect()

        # check if self.y has been calculated
        if not hasattr(self, 'y'):
            self.calc_y()

        figure(fignum)
        if clear:
            clf()

        kwargs = {'linewidth':2}
        if label:
            kwargs['label'] = label

        plot(self.t, self.y, fmt, **kwargs)# use **kwargs tp pass in
                                           # linewidth=2 and
                                           # label=label if label is
                                           # given


        xlabel('Time (sec.)')
        ylabel('$y(t)$')


class cosine_plotter(sine_plotter):
    def calc_y(self):
        """Calculate the y vector"""
        self.y = self.amp*cos(2*pi*self.f*self.t)
    

class double_sine_plotter(sine_plotter):
    def __init__(self, f, f2, fs=100.0, T=1.0, amp=1.0, amp2=0.1):
        # call the init method of the base class:
        sine_plotter.__init__(self, f, fs=fs, T=T, amp=amp)
        self.f2 = f2
        self.amp2 = amp2
        
    def calc_y(self):
        """Calculate the y vector"""
        self.y = self.amp*sin(2*pi*self.f*self.t) + \
                 self.amp2*sin(2*pi*self.f2*self.t)

if __name__ == '__main__':
    plotter1 = sine_plotter(2.0)
    plotter1.plot()

    plotter2 = cosine_plotter(3.0)
    plotter2.plot(fignum=2)

    plotter3 = double_sine_plotter(2.0, f2=6.0, amp2=0.5)
    plotter3.plot(fignum=3)

    plotter4 = cosine_plotter(5.0)
    plotter4.plot(fignum=2, clear=False)

    show()
