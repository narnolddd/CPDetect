set terminal postscript eps size 3.5,2.62 enhanced color \
font 'Helvetica,30' linewidth 5
set border linewidth 0.1
unset key
set xtics font 'Helvetica,12'
set ytics font 'Helvetica,12'
set xlabel font 'Helvetica,20'

file = "measurements/twoCPS.dat"

set xrange [0:9000]
set xlabel 'Network size (i.e. time)'

set output "images/rand_to_BA_meandegsq.eps"
set yrange [30:60]
set title 'Mean squared degree <k^2>'
plot file using 1:11 with lines

set output "images/rand_to_BA_maxdeg.eps"
set yrange [0:50]
set title 'Maximum degree k_{max}'
plot file using 1:4 with lines

set output "images/rand_to_BA_assort.eps"
set yrange [0:0.25]
set title 'Degree assortativity'
plot file using 1:13 with lines

set output "images/rand_to_BA_cluster.eps"
set log y
set yrange [0.001:0.1]
set title 'Global clustering coefficient'
plot file using 1:6 with lines
unset log y

##############################################################################

file = "measurements/2CPs2.dat"

set output "images/BA_to_rand_meandegsq.eps"
set yrange [0:100]
set title 'Mean squared degree <k^2>'
plot file using 1:11 with lines

set output "images/BA_to_rand_maxdeg.eps"
set yrange [0:220]
set title 'Maximum degree k_{max}'
plot file using 1:4 with lines

set output "images/BA_to_rand_assort.eps"
set yrange [-0.2:0.1]
set title 'Degree assortativity'
plot file using 1:13 with lines

set output "images/BA_to_rand_cluster.eps"
set log y
set yrange [0.001:0.2]
set title 'Global clustering coefficient'
plot file using 1:6 with lines
unset log y

##############################################################################

file = "measurements/1CP_rand_to_BA.dat"

set output "images/1CP_rand_to_BA_meandegsq.eps"
set yrange [30:60]
set title 'Mean squared degree <k^2>'
plot file using 1:11 with lines

set output "images/1CP_rand_to_BA_maxdeg.eps"
set yrange [0:40]
set title 'Maximum degree k_{max}'
plot file using 1:4 with lines

set output "images/1CP_rand_to_BA_assort.eps"
set yrange [0:0.3]
set title 'Degree assortativity'
plot file using 1:13 with lines

set output "images/1CP_rand_to_BA_cluster.eps"
set log y
set yrange [0.001:0.1]
set title 'Global clustering coefficient'
plot file using 1:6 with lines
unset log y

##############################################################################

file = "measurements/1CP_BA_to_rand.dat"

set output "images/1CP_BA_to_rand_meandegsq.eps"
set yrange [50:110]
set title 'Mean squared degree <k^2>'
plot file using 1:11 with lines

set output "images/1CP_BA_to_rand_maxdeg.eps"
set yrange [0:200]
set title 'Maximum degree k_{max}'
plot file using 1:4 with lines

set output "images/1CP_BA_to_rand_assort.eps"
set yrange [-0.2:0.1]
set title 'Degree assortativity'
plot file using 1:13 with lines

set output "images/1CP_BA_to_rand_cluster.eps"
set log y
set yrange [0.001:0.1]
set title 'Global clustering coefficient'
plot file using 1:6 with lines
unset log y
