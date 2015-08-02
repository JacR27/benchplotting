# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:50:36 2015

@author: jrayner
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def compSystemcomponet():
    workflow = "S1.1" #workflow id
    systems = ["W1.1","W1.2","W2","W3"]
    collectlData = ["[CPU]Wait%","[CPU]Nice%","[CPU]User%","[CPU]Sys%"]
    #collectlData = ["[DSK]WriteKBTot","[DSK]ReadKBTot"]
    #collectlData = ["[MEM]Cached","[MEM]Commit","[MEM]Tot"]
    #collectlData = ["[MEM]SwapUsed"]
    subprocesses = {}  
    data = {}
    for system in systems:
        subprocesses[system] = open('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/'+workflow+system,"r") # open file containt subprocesses
        data[system] = np.loadtxt('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/'+workflow+system+".tsv",skiprows=1) #read system into numpy array
    title = open('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/title',"r") # open file containing column headding
    columnLables = title.readline().split() # read colmn headding in to array
    subprocessNames = {}
    subprocessTimeTaken = {}
    subprocessCompleteTime = {}
    for key in subprocesses:
        rawData = [line.strip().split() for line in subprocesses[key]]
        rawData= np.array(rawData) #read subplocesses in to numpy array
        times = np.array(rawData[:,0],dtype=np.float)
        subprocessNames[key]=np.array(rawData[:,1])       
        subprocessTimeTaken[key]=np.array(times)/60 # read time column into its own array and convert to float
        for i in range(len(times)):
             times[i]= (np.sum(times[max([0,i-1]):i+1])) #generate clumaltive time for ploting ticks
        subprocessCompleteTime[key]= times
        subprocesses[key].close()
        title.close()
    fig = plt.figure()
    for i , system in enumerate(systems):
        x3 = fig.add_subplot(len(systems),1,i+1) #plot subprocesses data  
        x32=x3.twiny()
        #A = data[system][subprocessCompleteTime[system][0]:subprocessCompleteTime[system][1]]
        A= data[system]
        x3.set_xlim(min(A[:,0]/60),max(A[:,0]/60)) 
        for cD in collectlData:
            x3.plot(A[:,0]/60,A[:,columnLables.index(cD)],label=cD)
        x32.set_xticks(subprocessCompleteTime[system])
        x32.set_xticklabels([])
        #print((subprocessTimeTaken[system]))
        x3.set_title("{:s}{:s} total run time: {:.0f} minutes".format(system,workflow,(sum(subprocessTimeTaken[system]))))
        
        plt.grid()
        
    
    
    x3.legend(loc='center left', bbox_to_anchor=(1, 0.5))   
    plt.show()
    
if __name__=="__main__":
    compSystemcomponet()