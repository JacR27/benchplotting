# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:29:09 2015

@author: jrayner
"""
import sys

def main():
    for line in sys.stdin.readlines():
        if line.strip()!="":
            sys.stdout.write(" ".join([i.replace(" ","_") for i in (line.strip().split(None, 4)[5:3:-1])],))
            sys.stdout.write("\n")
    
main()