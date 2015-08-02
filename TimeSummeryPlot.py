# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 01:23:03 2015

@author: jrayner
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def compSystems(workflow,systems):


    subprocesses = {}    
    for system in systems:
        subprocesses[system] = open('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/'+system+workflow,"r") # open file containt subprocesses
    
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
        
    
    lenth = len(subprocessNames[system])
    fig = plt.figure()
    fig2 =plt.figure()
    fig.suptitle(workflow)
    fig2.suptitle(workflow)
    x3 = fig.add_subplot(111) #plot subprocesses data
    x1 = fig2.add_subplot(111)
    barwidth = 0.5/len(systems)
    for i , system in enumerate(systems):
        totaltime = np.sum(subprocessTimeTaken[system]/60)
        x3.bar(np.arange(lenth)+barwidth*i,subprocessTimeTaken[system]/60,width=barwidth,color=cm.jet(1.*i/len(systems)),label=system)
        x1.bar(np.arange(lenth)+barwidth*i,subprocessTimeTaken[system]/totaltime/60,width=barwidth,color=cm.jet(1.*i/len(systems)),label=system)
    x3.set_xticks(np.arange(lenth)+0.25)
    x3.set_xticklabels(subprocessNames[system],rotation=90)
    print(subprocessNames[system])
    x3.set_ylabel("time (minutes)")
    x3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    x1.set_xticks(np.arange(lenth+0.25))
    x1.set_xticklabels(subprocessNames[system],rotation=90)
    x1.set_ylabel("time %")
    x1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.show()
    
if __name__=="__main__":
    compSystems()