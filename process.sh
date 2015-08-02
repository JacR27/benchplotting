#!/bin/bash

processName=$1
savepath=/home/jrayner/run2/scripts/benchmarking/
inputdir=./
scriptsdir=/home/jrayner/run2/scripts/

grep "Elapsed time" ${inputdir}runout | python ${scriptsdir}getsubprocesstimesISIS.py > $savepath$processName

python ${scriptsdir}benchmakingworkflows.py "$processName" "$savepath" "$inputdir"
