# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:51:39 2015

@author: jrayner
"""

import subprocess as subp
import matplotlib.pyplot as plt
import numpy as np
def main():
    filename = "S3"
    CPU=["[CPU]Wait%","[CPU]Nice%","[CPU]User%","[CPU]Sys%"]
    IO=["[DSK]WriteKBTot","[DSK]ReadKBTot"]
    MEM=["[MEM]Cached","[MEM]Commit","[MEM]Tot","[MEM]Anon"]
    average=1
    title = open('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/title',"r") # open file containing column headding
    columnLables = title.readline().split() # read colmn headding in to array
    
    subprocesses=open('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/'+filename,"r") # open file containt subprocesses
    breakdown = [line.strip().split() for line in subprocesses] 
    breakdown = np.array(breakdown) #read subplocesses in to numpy array
    breakdownNames = breakdown[:,1]
    breakdowntimes=np.array(breakdown[:,0],dtype=np.float) # read time column into its own array and convert to float
    ctime = np.array(breakdowntimes)
    for i in range(len(breakdowntimes)):
        ctime[i] = np.sum(ctime[max([0,i-1]):i+1]) #generate clumaltive time for ploting ticks
    
    A = np.loadtxt('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/'+filename+".tsv",skiprows=1) #read data file into array

    print(max(A[:,0])-max(ctime)) # print test to see if time recoded by collectl is the same as the workforl itself
    fig = plt.figure() #start figure
    acpu = fig.add_subplot(513) #plot cpu data
    #acpu.set_xlim(0,max(A[:,0])/60)    
    acpu.set_ylabel("CPU percent")
    acpu.set_ylim(0,110)
    for n in CPU:
        acpu.plot(A[:,0]/60,A[:,columnLables.index(n)],label=n)
    xmin, xmax =acpu.get_xlim()    
    tics =acpu.get_xticks()
    ticlabels = acpu.get_xticklabels()
    print (tics,ticlabels)
    acpu2=acpu.twiny()
    acpu2.set_xticks(tics)
    #acpu2.set_xticklabels(ticlabels)
    acpu.set_xticks(ctime/60)
    acpu.set_xticklabels(breakdownNames,rotation=60)
    acpu.xaxis.grid()
    
    acpu.legend(loc='center left', bbox_to_anchor=(1, 0.5))    
    
    x3 = fig.add_subplot(515) #plot subprocesses data
    x3.bar(np.arange(len(breakdowntimes)),breakdowntimes/60,width=0.5)
    x3.set_xticks(np.arange(len(breakdowntimes))+0.25)
    x3.set_xticklabels(breakdownNames,rotation=90)
    x3.set_ylabel("time (minutes)")
    x3.set_title("{:s} total run time: {:.0f} minutes".format(filename,(sum(breakdowntimes)/60)))
    
    aIO = fig.add_subplot(512)
    aIO2=aIO.twiny()   
    #aIO.set_xlim(0,max(A[:,0])/60)
    
    aIO.set_ylabel("IO (MB/s)")
    for n in IO:   
        aIO.plot(A[:,0]/60,A[:,columnLables.index(n)]/1000,label=n)
    xmin, xmax =aIO.get_xlim()
    aIO.set_xticklabels([])
    aIO2.set_xlim(xmin,xmax)
    aIO2.set_xticks(ctime)
    aIO2.set_xticklabels([])
    plt.grid()
    aIO.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    aMEM= fig.add_subplot(511)
    aMEM2=aMEM.twiny()    
    #aMEM.set_xlim(0,max(A[:,0])/60)
    aMEM.set_xlabel("time (minutes)")   
    aMEM.set_ylabel("MEM (GB)")
    for n in MEM:
        aMEM.plot(A[:,0]/60,A[:,columnLables.index(n)]/1000**2,label=n)
    xmin, xmax =aMEM.get_xlim()
    aMEM2.set_xlim(xmin,xmax)
    aMEM2.set_xticks(ctime) 
    aMEM2.set_xticklabels([])
    plt.grid()
    aMEM.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()
    
    title.close()
    subprocesses.close()
if __name__=="__main__":
    main()
