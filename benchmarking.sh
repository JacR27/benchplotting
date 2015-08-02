#!/bin/bash

processName=$1
workflowpath=/illumina/development/Isis/2.5.55.16.NorthStar/Isis 
workingdir=./

echo "this script will run a comand benchmarking and monitor system using collectl"

collectl -s cmd -f $workingdir$processName &
CollectlPid=$!
echo collectl started

nohup /usr/bin/time -v $workflowpath -r $workingdir> ${workingdir}${processName}runout

echo killing collectl

kill $CollectlPid

collectl -p $workingdir${processName}* -P -f ${workingdir}plot

gzip -d ${workingdir}plot*

mv ${workingdir}plot* ${workingdir}${processName}collectl.dat
