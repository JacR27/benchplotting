#!/bin/bash

grep "Elaspsed time" runout | python ~/scripts/getsubprocesstimesISIS.py > processtics

python  ~/scripts/benchmakingworkflows.py

export GNUTERM=dumb
~/scripts/collectl.pg
