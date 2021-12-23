with open('8-input.txt','r') as f:
    
    #input = [16,1,2,0,4,2,7,1,2,14] ## Example
    
    input_lines = f.read().splitlines()
    
    
    a = b = c = d = e = f = g = ''
    codenums = []
    for line in input_lines:
        codes = line.split()
        cf = []
        bd = []
        code_string = ''
        for i,n in enumerate(codes):
            if len(n) == 2:
                cf.append(n[0])
                cf.append(n[1])
                #print("cf =", cf)
                break
        for i,n in enumerate(codes):
            if len(n) == 4:
                for l in n:
                    if l not in cf:
                        bd.append(l)
                #print("bd =", bd)
                break
        for i,n in enumerate(codes):
            if len(n) == 6 :
                #print("cf =", cf, ", bd =", bd)
                if cf[0] not in n and cf[1] in n:
                    c = cf[0]
                    f = cf[1]
                    #print("c, f =", c, f)
                    break
                elif cf[1] not in n and cf[0] in n:
                    c = cf[1]
                    f = cf[0]
                    #print("c, f =", c, f)
                    break
                            
        for i,n in enumerate(codes):
            
            if i>10:
                if len(n) == 2:
                    code_string+='1'
                if len(n) == 3:    
                    code_string+='7'
                if len(n) == 4:
                    code_string+='4'
                if len(n) == 7:
                    code_string+='8'
                if len(n) == 5:
                    if c in n and f in n:
                        code_string+='3'
                    elif c in n:
                        code_string+='2'
                    elif f in n:
                        code_string+='5'
                if len(n) == 6:
                    if c not in n or f not in n:
                        code_string+='6'
                    elif bd[0] in n and bd[1] in n:
                        code_string+='9'
                    else:
                        code_string+='0'
        #print(code_string)
        if len(code_string) <4: print("AHHHHH")
        codenums.append(int(code_string))
        
    print(sum(codenums))
            


       # break
