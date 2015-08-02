# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:12:15 2015

@author: jrayner
"""

breakdown = open ('./system1','r')
for n in range(100):
    print("".join("a" + breakdown.readline().strip()))
    
breakdown.close()