with open('2a-input.txt','r') as f:
    #lines = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'] ## Example
    lines = f.read().splitlines()
    aim=0
    h = 0
    d = 0
    for line in lines:
        x = line.split()
        if x[0] == "forward": 
            h = h+int(x[1])
            d += aim*int(x[1])
        elif x[0] == "up": 
            #d = d-int(x[1])
            aim = aim-int(x[1])
        elif x[0] == "down": 
            #d = d+int(x[1])
            aim = aim+int(x[1])
        else: print("Fucked if I know")
        print(line, ", h=",h, ", d=",d, ", aim=:",aim)    
    print("h =", h)
    print("d =", d)
    print("combo =", h*d)
        

