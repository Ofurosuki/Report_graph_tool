import matplotlib.pyplot as plt
import numpy as np
import platform
import math
class ThesisFormat:
    xlabel = 'X label'
    ylabel = 'Y label'
    def __init__(self) -> None:
        self.plt_style()
    
    def plt_style(self):
        plt.rcParams['figure.autolayout'] = True
        plt.rcParams['figure.figsize'] = [6.4, 4.8]
        if platform.system() == 'Windows':
            plt.rcParams['font.family'] ='Times New Roman'
        else:
            plt.rcParams['font.family'] ='Times New Roman Cyr'
        plt.rcParams['font.size'] = 14
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['axes.linewidth'] = 1.0
        plt.rcParams['errorbar.capsize'] = 6
        plt.rcParams['lines.markersize'] = 6
        plt.rcParams['lines.markerfacecolor'] = 'white'
        plt.rcParams['mathtext.fontset'] = 'cm'



    def plt_line(self):
        #x=np.array([0,4,8,12,16,20,24,28,32,36,40,42.58])
        #y=np.array([0,1.64,3.86,6.11,8.34,10.53,12.68,14.8,16.8,18.8,20.7,22])

        # n=1
        # pn=np.polyfit(x,y,n)
        # xp = np.linspace(0, 43, 100)
        # p=np.poly1d(pn)
        

        fig, ax = plt.subplots()
        #ax.plot(x,y,"o",label="observed",color="blue")
        #ax.plot(xp,p(xp),"-",color="blue") 

        
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.legend()
        plt.show()

if __name__ == '__main__':
    plt.rcParams['axes.unicode_minus'] = False
    thesis_format = ThesisFormat()
    thesis_format.xlabel = "currency "+r"$I$"+ " /mA"
    thesis_format.ylabel = "Intensity"+r"$\ P\ \mathrm{/\mu W}$"
    thesis_format.plt_line()