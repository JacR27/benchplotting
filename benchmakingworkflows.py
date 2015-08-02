# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:55:03 2015

@author: jrayner
"""

import subprocess as subp
from datetime import datetime
from time import mktime
import sys
def main():
    name = sys.argv[1]
    #breakdown = open ('./system1','r')
    plottableCollectlFile= open(sys.argv[2] + name +".tsv",'w') # open newfile for output
    purportedlyPlotableCollectlFile = open(sys.argv[3] + "collectl.dat",'r') # open collectl output
    
    data = [] # inicalise array
    for line in purportedlyPlotableCollectlFile: 
        if line[0]=="#":   #remove header
            titleline = line[6:] #save heading row excluding date
        else:
            data.append(line.strip()) # write data to array
   # data = [line.strip() for line in purportedlyPlotableCollectlFile.splitlines() if not line.startswith('#')]
    
    plottableCollectlFile.write(titleline) # write header row to outputfile
    starttime = datetimestr2seconds(data[0][0:17]) #get first time string and convert to seconds
    
    #ticks = [line.split() for line in breakdown.readlines()]
    #ticks.append(float("inf"))
    #tic = 0
    #time = -1
    for i in data:
        #previousTime = time
        time = datetimestr2seconds(i[0:17])-starttime # convert timestamp to relitive time
        #print(ticks[tic])
        #if (previousTime < float(ticks[tic][0]) <= int(time)): 
            #print ("true")
            #plottableCollectlFile.write(str(time) + i[17:] + " " + ticks[tic][1] + "\n") #write date to outputfile
            #tic += 1
        #else:
        plottableCollectlFile.write(str(time) + i[17:] + "\n") #write date to outputfile
    
    purportedlyPlotableCollectlFile.close()
    plottableCollectlFile.close()
    
def datetimestr2seconds(timestring):
    dt = datetime.strptime(timestring,"%Y%m%d %H:%M:%S") # convert time string into datatime object
    dt = int(mktime(dt.timetuple())) # convert datetime object to seconds
    return dt
main()
