set term aqua

file = "CP_BA_Rand_measurements.dat"

set xrange [0:20000]
set yrange [0:60]

plot file using 1:11 with lines
