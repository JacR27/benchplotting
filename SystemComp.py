# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 00:47:23 2015

@author: jrayner
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def compSystemcomponet(workflow,systems,collectlData):
    workflow = "W3" #workflow id    
    
    title = open('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/title',"r") # open file containing column headding
    columnLables = title.readline().split() # read colmn headding in to array
    title.close()
    
    data = []
    subprocessNames = []
    subprocessTimeTaken = []
    subprocessCompleteTime = []
    for system in systems:
        data.append(np.loadtxt('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/'+system+workflow+".tsv",skiprows=1)) #read system into numpy array    
        subprocesses = open('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/'+system+workflow,"r") # open file containt subprocesses
        rawData = [line.strip().split() for line in subprocesses]
        rawData= np.array(rawData) #read subplocesses in to numpy array
        times = np.array(rawData[:,0],dtype=np.float)
        subprocessNames.append(np.array(rawData[:,1]))       
        subprocessTimeTaken.append(np.array(times)/60) # read time column into its own array and convert to float
        for i in range(len(times)):
            times[i]= (np.sum(times[max([0,i-1]):i+1])) #generate clumaltive time for ploting ticks
        subprocessCompleteTime.append(np.array(times))
        subprocesses.close()
        
    
    xlimit = 0
    for i in range(len(systems)):
        A=data[i]
        if max(A[:,0]/60)>xlimit:
            xlimit = max(A[:,0]/60)
    
    fig = plt.figure()
    for i , system in enumerate(systems):
        x3 = fig.add_subplot(len(systems),1,i+1) #plot subprocesses data  
        #A = data[system][subprocessCompleteTime[system][0]:subprocessCompleteTime[system][1]]
        A= data[i]
        x3.set_xlim(min(A[:,0]/60),xlimit) 
        for cD in collectlData:
            x3.plot(A[:,0]/60,A[:,columnLables.index(cD)],label=cD)
        for n,name in enumerate(subprocessNames[i]):
            ymin, ymax= x3.get_ylim()
            x3.annotate(name, xy=(subprocessCompleteTime[i][n]/60, 1), xytext=(subprocessCompleteTime[i][n]/60,ymax),rotation=30,
            arrowprops=dict(visible=True, fill=False, width=0.0001,linestyle='dashed'))
        #print((subprocessTimeTaken[system]))
        x3.set_title("{:s}{:s} total run time: {:.0f} minutes".format(system,workflow,(sum(subprocessTimeTaken[i]))))
        
        
        
    
    
    x3.legend(loc='center left', bbox_to_anchor=(1, 0.5))   
    plt.show()
    
if __name__=="__main__":
    compSystemcomponet()