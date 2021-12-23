with open('7-input.txt','r') as f:
    
    #input = [16,1,2,0,4,2,7,1,2,14] ## Example
    
    input_s = f.read().split(',')
    input = [int(i) for i in input_s]
    
    min = min(input)
    max = max(input)

    closest = -9999
    for i in range(min, max+1):
        tmp_input = [abs(input_i - i) for input_i in input]
        tmp_fuel = [(tmp_i*(tmp_i+1)/2) for tmp_i in tmp_input]
        fuel_needed = sum(tmp_fuel)
        
        if closest==-9999 or closest > fuel_needed: closest = fuel_needed
        
    print("least fuel needed =", closest, "\n\n")
