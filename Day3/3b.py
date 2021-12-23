import numpy as np
from scipy import stats

with open('3a-input.txt','r') as f:
    lines = f.read().splitlines()
    
    bin_len = len(lines[0])
    lines_lst = []
    for line in lines:
        lines_lst.append(list(line))
    mode = stats.mode(lines_lst)

    
    oxy_lst = lines_lst.copy()
    for digit in range(bin_len):
        n_ones = n_zeros = 0
        for i in oxy_lst:
            if int(i[digit])==1:
                n_ones += 1
            else: n_zeros +=1
        if n_ones>n_zeros: match = 1
        elif n_zeros>n_ones: match = 0
        else: match = 1

        pop_lst =[]
        for i,num in enumerate(oxy_lst):
            if len(oxy_lst) > 1:
                if int(num[digit]) != match:
                    pop_lst.append(i)
    
        popped=0
        for j in pop_lst:
            oxy_lst.pop(j-popped)
            popped+=1
    
    oxy_bin = "".join(oxy_lst[0])
    print("Oxy bin:", oxy_bin)
    oxy_int = int(oxy_bin,2)
    print("Oxy int:", oxy_int)


    co2_lst = lines_lst.copy()
    for digit in range(bin_len):
        n_ones = n_zeros = 0
        for i in co2_lst:
            if int(i[digit])==1:
                n_ones += 1
            else: n_zeros +=1
        if n_ones>n_zeros: match = 0
        elif n_zeros>n_ones: match = 1
        else: match = 0
        pop_lst =[]
        for i,num in enumerate(co2_lst):
            if len(co2_lst) > 1:
                if int(num[digit]) != match:
                    pop_lst.append(i)
    
        popped=0
        for j in pop_lst:
            co2_lst.pop(j-popped)
            popped+=1
    co2_bin = "".join(co2_lst[0])
    print("CO2 bin:", co2_bin)
    co2_int = int(co2_bin,2)
    print("CO2 int =", co2_int)


    total = oxy_int*co2_int
    print("Total =", total)
