#!/bin/bash

processName=$1
savepath=/home/jrayner/run2/scripts/benchmarking/
inputdir=./
scriptsdir=/home/jrayner/run2/scripts/

grep "Elapsed time" ${inputdir}${processName}.stdout | python ${scriptsdir}getsubprocesstimesISIS.py > $savepath$processName

python ${scriptsdir}benchmakingworkflows2.py "$processName" "$savepath" "$inputdir"
