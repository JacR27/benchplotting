# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:01:14 2015

@author: jrayner
"""
import SystemComp as p1
import SystemWorkflowPlot as p2
import TimeSummeryPlot as p3
import matplotlib.pyplot as plt
def plot():
    systems = ["S1.1","S1.2","S2","S3","S4"]
    workflow = "W2"
    collectlData = [["[CPU]Wait%","[CPU]Nice%","[CPU]User%","[CPU]Sys%"],
                    ["[DSK]WriteKBTot","[DSK]ReadKBTot"],
                    ["[MEM]Cached","[MEM]Commit","[MEM]Tot","[MEM]Anon"]]
    for i in range(len(collectlData)):
        p1.compSystemcomponet(workflow,systems,collectlData[i])
    p3.compSystems(workflow,systems)
    for i in systems:
        p2.main(i+workflow)
    print("hello World")
    
plot()