with open('1a-input.txt','r', encoding='UTF-8') as f:
#with open('Smithy01_input.txt') as f:
    #lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263] ## Example
    sLines = f.read().splitlines()
    lines = [int(i) for i in sLines]
    print("len(lines) =", len(lines))
    n_higher = 0
    for i,n  in enumerate(lines):
        if i!=0 and n > lines[i-1]:
            n_higher+=1
    print("nH =", n_higher)
