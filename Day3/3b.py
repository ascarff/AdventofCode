with open('3a-input.txt','r') as f:
    lines = f.read().splitlines()
    

def find_which_matches(digit, target_lst, oxy_co2):
        
    n_ones = n_zeros = 0
    for i in target_lst:
        if int(i[digit])==1:
            n_ones += 1
        else: n_zeros +=1
    if oxy_co2=='oxy':
        if n_ones>n_zeros: match = 1
        elif n_zeros>n_ones: match = 0
        else: match = 1
    elif oxy_co2=='co2':
        if n_ones>n_zeros: match = 0
        elif n_zeros>n_ones: match = 1
        else: match = 0
    else:
        print("Second argument must bt 'oxy' or 'co2'")
    return(match)

def find_remove_non_matchers(digit, target_lst, match):
    pop_lst = []
    for i, num in enumerate(target_lst):
        if len(target_lst) > 1:
            if int(num[digit]) != match:
                pop_lst.append(i)
        
    popped = 0
    for j in pop_lst:
        target_lst.pop(j-popped)
        popped +=1

def convert_bin_to_dec(target_lst):
    if len(target_lst) > 1:
        print("Too many items in list, should only be one left")
        return
        
    n_bin = "".join(target_lst[0])
    n_dec = int(n_bin,2)
    return(n_bin, n_dec)



bin_len = len(lines[0])
lines_lst = []
for line in lines:
    lines_lst.append(list(line))
    
oxy_lst = lines_lst.copy()
co2_lst = lines_lst.copy()
for digit in range(bin_len):
    oxy_match = find_which_matches(digit, oxy_lst, "oxy")
    find_remove_non_matchers(digit, oxy_lst, oxy_match)
    co2_match = find_which_matches(digit, co2_lst, "co2")
    find_remove_non_matchers(digit, co2_lst, co2_match)

oxy_bin, oxy_dec = convert_bin_to_dec(oxy_lst)
co2_bin, co2_dec = convert_bin_to_dec(co2_lst)

total = oxy_dec*co2_dec



print("Oxy bin =", oxy_bin)
print("Oxy dec =", oxy_dec)
print("CO2 bin =", co2_bin)
print("CO2 dec =", co2_dec)
print("Total =", total)
