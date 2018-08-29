import os
import sys

growtemplate = sys.argv[1]
growfile = growtemplate.replace(".xml",".tmp")
print(growfile)
graphname= "grownnets/test1CP_BA_to_rand.dat"


params = [1,0]
times = [4500,9000]

seedgraph= "seed/simple_start_graph.dat"
start = 10

for i in range(0,len(params)):
    grow = open(growtemplate,'r')
    fd = grow.read()
    grow.close()
    fd = fd.replace("START",str(start))
    fd = fd.replace("STOP",str(times[i]))
    fd = fd.replace("AAA",str(params[i]))
    fd = fd.replace("BBB", str(1 - params[i]))
    fd = fd.replace("GINPUT",seedgraph)
    fd = fd.replace("GOUTPUT",graphname)
    gf = open(growfile,'w')
    gf.write(fd)
    gf.close()
    os.system("java -jar feta2-1.0.0.jar "+growfile)
    start = times[i]
    seedgraph = graphname
