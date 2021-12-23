with open('8-input.txt','r') as f:
    
    #input = [16,1,2,0,4,2,7,1,2,14] ## Example
    
    input_lines = f.read().splitlines()
    
    total_1478 = 0
    for line in input_lines:
        codes = line.split()
        for i,n in enumerate(codes):
            if i>10:
                if len(n) == 2 or len(n) == 3 or len(n) == 4 or len(n) == 7:
                    total_1478 += 1
    print(total_1478)

