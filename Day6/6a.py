import time

t0=time.time()

import matplotlib.pyplot as plt
import numpy as np
with open('6a-input.txt','r') as f:
    
    #input = [3,4,3,1,2] ## Example
    
    input_s = f.read().split(',')
    input = [int(i) for i in input_s]
    fishies = [0,0,0,0,0,0,0,0,0]
    for i in input:
        fishies[i] += 1

    day = 0
    fishk=[]
    while day<257:
        new_fish=0
        print("After", day, "days,", sum(fishies), "fishies")
        fishk.append(sum(fishies))
        tmp_fishies = [0,0,0,0,0,0,0,0,0]
        for i,n in enumerate(fishies):
            if i!=8:
                tmp_fishies[i]=fishies[i+1]
           
        tmp_fishies[6]+=fishies[0]
        tmp_fishies[8]=fishies[0]
        fishies=tmp_fishies
                
        day += 1

t1=time.time()
total=t1-t0
print("timetaken = ", total)

               
plt.plot(fishk)
plt.xlabel('Days')
plt.ylabel('Num of Fishies')
plt.show()
