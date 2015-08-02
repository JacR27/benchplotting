# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:38:41 2015

@author: jrayner
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import benchmarkingYAML as ya
def compSystemcomponet():
    
    workflow = "W12"
    systems = ["S1","S2","S4"]
    average = 60
    collectlData = [["[CPU]Wait%","[CPU]Nice%","[CPU]User%","[CPU]Sys%"],
                    ["[DSK]WriteKBTot","[DSK]ReadKBTot"],
                    ["[MEM]Cached","[MEM]Commit","[MEM]Tot","[MEM]Anon"]]
    
    switchsubrocesses = 0
    
    title = open('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/title',"r") # open file containing column heading
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
        subprocessCompleteTime.append(np.array(times)/60)
        subprocesses.close()
        
    xlimit = 0
    for i in range(len(systems)):
        A=data[i]
        if max(A[:,0]/60)>xlimit:
            xlimit = max(A[:,0]/60)
    length = len(subprocessNames[i])
    fig1 = []
    for n in collectlData:    
        fig1.append(Plot1(average,workflow,subprocessTimeTaken,systems,data,xlimit,n,columnLables,subprocessNames,subprocessCompleteTime))
    fig2,fig3,fig4 = Plot2(workflow,systems,subprocessTimeTaken,length,subprocessNames,subprocessCompleteTime)
        
    plt.show()
    if True:        
        for i,fig in enumerate(fig1):
            fig.savefig('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/plots/' + workflow+ str(i) + '.png',bbox_inches='tight')
        fig2.savefig('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/plots/' + workflow+"Bar2" + '.png',bbox_inches='tight')
        fig4.savefig('C:/cygwin64/home/jrayner/run2/scripts/benchmarking/plots/' + workflow+"Bar" + '.png',bbox_inches='tight')
        print("saved")

def Plot1(average,workflow,subprocessTimeTaken,systems,data,xlimit,collectlData,columnLables,subprocessNames,subprocessCompleteTime):
    fig = plt.figure()
    for i , system in enumerate(systems):
        ax = fig.add_subplot(len(systems),1,i+1) #plot subprocesses data  
        #A = data[system][subprocessCompleteTime[system][0]:subprocessCompleteTime[system][1]]
        A= data[i]
        
        ax.set_xlim(min(A[:,0]/60),xlimit) 
        for cD in collectlData:
            B = np.zeros(np.size((A[:,columnLables.index(cD)])))
            for d in range(np.size(A,axis=0)):
                B[d] = np.mean(A[max([0,d-average]):d+1,columnLables.index(cD)])
            #print(system + " " + cD + ": " + str(np.sum(A[0:int(subprocessCompleteTime[i][1]*60),columnLables.index(cD)])))
            ax.plot(A[:,0]/60,B,label=cD)
        for n,name in enumerate(subprocessNames[i]):
            ymin, ymax= ax.get_ylim()
            ax.annotate(name, xy=(subprocessCompleteTime[i][n], 1), xytext=(subprocessCompleteTime[i][n],ymax),rotation=30,
            arrowprops=dict(visible=True, fill=False, width=0.0001,linestyle='dashed'))
        ax.set_title("{:s}, {:s}".format(system,ya.workflows[workflow].version + ", " + ya.workflows[workflow].runType,))
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    fig.tight_layout()
    fig.set_size_inches(12,6)
    
    
    return fig
    
def Plot2(workflow,systems,subprocessTimeTaken,length,subprocessNames,subprocessCompleteTime):
    fig = plt.figure()
    fig2 =plt.figure()
    fig3 =plt.figure()
    fig.suptitle(ya.workflows[workflow].version + ", " + ya.workflows[workflow].runType)
    fig2.suptitle(ya.workflows[workflow].version + ", " + ya.workflows[workflow].runType)
    fig3.suptitle(ya.workflows[workflow].version + ", " + ya.workflows[workflow].runType)
    
    ax = fig.add_subplot(111) #plot subprocesses data
    ax2 = fig2.add_subplot(111)
    
    barwidth = 0.5/len(systems)
    for i , system in enumerate(systems):
        totaltime = np.sum(subprocessTimeTaken[i])
        ax.bar(np.arange(length)+barwidth*i,subprocessTimeTaken[i],width=barwidth,color=cm.jet(1.*i/len(systems)),label=system)
        ax2.bar(np.arange(length)+barwidth*i,subprocessTimeTaken[i]/totaltime,width=barwidth,color=cm.jet(1.*i/len(systems)),label=system)
    ax.set_xticks(np.arange(length)+0.25)
    ax.set_xticklabels(subprocessNames[i],rotation=90)
    ax.set_ylabel("time (minutes)")
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax2.set_xticks(np.arange(length)+0.25)
    ax2.set_xticklabels(subprocessNames[i],rotation=30)
    ax2.set_ylabel("time %")
    ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))    
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    STT=  (np.array(subprocessCompleteTime))
    SN= np.array(subprocessNames)
    ax3 = fig3.add_subplot(111)
    barwidth = 0.5
    for i in range(length-1,-1,-1):
        ax3.bar(np.arange(len(systems)),STT[:,i],width=barwidth,color=cm.jet(1.*i/length),bottom = 0,label=SN[0,i])
        ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax3.set_xticks(np.arange(len(systems))+0.25)
        ax3.set_xticklabels(systems)
        ax3.set_ylabel("time (minutes)")
    return fig, fig2,fig3
if __name__=="__main__":
    compSystemcomponet()