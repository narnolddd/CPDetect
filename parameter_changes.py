## Python program for obtaining best fitting mixture of models for different segments of a network's growth. Needs a lot of scrubbing up.

import os
import sys

like_file = sys.argv[1]
like_file_tmp = like_file.replace(".xml",".tmp")
like_file_tmp_tmp= like_file.replace(".xml","_tmp.tmp")

final_result="final_MLEs.txt"

no_segments = 10
net_file = "grownnets/CP_BA_Rand.dat"

# Get right interval size for number of segments
f = open(net_file,'r')
linelist = f.readlines()
f.close()
firstline, lastline = linelist[0].strip().split(" "), linelist[len(linelist)-1].strip().split(" ")
t1 = int(firstline[2])
t2 = int(lastline[2])
interval = int((t2 - t1) / no_segments)

def replace_start_end(start, end):
    with open(like_file,'r') as f:
        filedata = f.read()
        filedata = filedata.replace("XXX",str(start))
        filedata = filedata.replace("YYY",str(end))
        f.close()
        with open(like_file_tmp,'w') as g:
            g.write(filedata)
            g.close()

def replace_like_params(param):
    f1 = open(like_file_tmp,'r')
    fd = f1.read()
    fd = fd.replace("AAA",str(param))
    fd = fd.replace("BBB",str(1-param))
    f1.close()
    with open(like_file_tmp_tmp,'w') as f2:
        f2.write(fd)

likestart = t1
f3 = open(final_result,'w')

for i in range (0,no_segments):
    print(i)
    replace_start_end(likestart,likestart+interval)
    max_like, MLE = 0,0
    for j in range(0,100):
        param = j/100
        replace_like_params(param)
        os.system("java -jar feta2-1.0.0.jar "+like_file_tmp_tmp+" > like_vals.tmp")
        with open("like_vals.tmp",'r') as f:
            like = float(f.readline().split()[12])
        if like > max_like:
            max_like = like; MLE = param;
    f3.write("%d %f %f \n" % (likestart + interval/2, MLE, max_like))
    likestart=likestart+interval

f3.close()
