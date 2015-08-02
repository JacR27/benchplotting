#!/bin/bash

gnuplot<<EOF
set terminal png
set output "plot.png"
#set bmargin 10
set boxwidth 0.5
set style fill solid
set key outside
set xtics rotate by 4 right #offset 0,-1
set bmargin 15
plot "system1" u 0:1:xtic(2) with boxes title "system1"
EOF
