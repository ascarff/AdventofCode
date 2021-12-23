with open('1a-input.txt','r') as f:
    #lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263] ## Example
    lines = f.read().splitlines()
    inputs = [int(i) for i in lines]
    print("len(inputs) =", len(inputs))
    
    slider = []
    for i,n  in enumerate(inputs):
        if i==len(inputs)-2: break
        num = n+inputs[i+1]+inputs[i+2]
        slider.append(num)
        
    nHigher = 0
    for i,n in enumerate(slider):
        if i!=0 and n>slider[i-1]:
            nHigher+=1

print("nHigher =", nHigher)    
            
        

