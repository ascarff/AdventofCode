with open('2a-input.txt','r') as f:
    #lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263] ## Example
    lines = f.read().splitlines()
    h = 0
    d = 0
    for line in lines:
        x = line.split()
        if x[0] == "forward": h = h+int(x[1])
        elif x[0] == "up": d = d-int(x[1])
        elif x[0] == "down": d = d+int(x[1])
        else: print("Fucked if I know")
            
    print("h =", h)
    print("d =", d)
    print("combo =", h*d)
        

