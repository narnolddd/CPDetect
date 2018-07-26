import os
import numpy as np
edgelist = []
operations = []
nodelist = []
neighbours = []

# os.system("java -jar feta2-1.0.0.jar test_growth.xml")

coolRate = 0.5
init_guess=0.5 #Initial parameter guess
no_steps=20

like_file = "AS_like.xml"
tmp_file = "AS_like.tmp"

def replace_param(param):
    with open(like_file,'r') as f:
        filedata = f.read()

    filedata = filedata.replace("AAA",str(param))
    filedata = filedata.replace("BBB",str(1-param))

    with open(tmp_file,'w') as f:
        f.write(filedata)

def getLike():
    os.system("java -jar feta2-1.0.0.jar AS_like.tmp > like_vals.tmp")
    with open("like_vals.tmp",'r') as f:
        like = float(f.readline().split()[12])
    return like

def acceptanceProb(newLike, oldLike, temp):
    if newLike > oldLike:
        return 1.0
    return np.exp((newLike - oldLike)/temp)

def getMLE():
    init_guess = 0.2
    jumpsize = 0.1
    coolRate = 0.5
    temp = 1
    replace_param(init_guess)
    init_like = getLike()
    count=0
    rejectcount=0
    k=1
    while True:
        count = count + 1
        if rejectcount > 5:
            jumpsize = jumpsize/2
        if rejectcount > 10:
            print("REJECTIONS EXCEEDED")
            break
        if count > 50:
            print("COUNT EXCEEDED")
            break
        new_guess = init_guess + np.random.normal(0,jumpsize)
        if new_guess>1 or new_guess<0:
            continue
        replace_param(new_guess)
        new_like = getLike()
        if new_like>init_like:
            prob_accept = 1
        else: prob_accept= 0.1
        print("New Guess %f New Likelihood %f Old Guess %f Old Likelihood %f Probability of Acceptance %f \n" % (new_guess, new_like, init_guess, init_like, prob_accept))
        r = np.random.uniform()
        if r<prob_accept:
            print("ACCEPT")
            init_guess=new_guess
            init_like=new_like
            rejectcount = 0
        else: print("REJECT"); rejectcount = rejectcount+1; temp = temp*(1-coolRate)

getMLE()
