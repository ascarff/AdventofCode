import numpy as np

with open('5-input.txt','r') as f:
    lines = f.read().splitlines()
    
    xys = []
    for i, line in enumerate(lines):
        tmp_line=line.split()
        x1,y1=tmp_line[0].split(',')
        x2,y2=tmp_line[2].split(',')
        xys.append([int(x1), int(x2), int(y1), int(y2)])

    ### Find max vals in lines and make diagram of that size
    max_vals=np.amax(xys,axis=0)
    max_x = max(max_vals[0], max_vals[1])
    max_y = max(max_vals[2], max_vals[3])

    diagram = [[0 for col in range(max_y+1)] for col in range(max_x+1)]

    for i,vals in enumerate(xys):
        if xys[i][0]==xys[i][1]:
            ### vertical line
            x_vert = xys[i][0]
            
            if xys[i][2]> xys[i][3]:
                start=xys[i][2]
                stop=xys[i][3]-1
                iterator=-1
            elif xys[i][2]<xys[i][3]:
                start=xys[i][2]
                stop=xys[i][3]+1
                iterator=1
            for y_vert in range(start, stop, iterator):
                diagram[x_vert][y_vert]+=1
        elif xys[i][2]==xys[i][3]:
            ### horizontal line
            y_hori = xys[i][2]
            
            if xys[i][0]> xys[i][1]:
                start=xys[i][0]
                stop=xys[i][1]-1
                iterator=-1
            elif xys[i][0]<xys[i][1]:
                start=xys[i][0]
                stop=xys[i][1]+1
                iterator=1
            for x_hori in range(start, stop, iterator):
                diagram[x_hori][y_hori]+=1
        else:
            ### diagonal line
            if xys[i][0]> xys[i][1]:
                x_start=xys[i][0]
                x_stop=xys[i][1]-1
                x_iterator=-1
            if xys[i][0]<xys[i][1]:
                x_start=xys[i][0]
                x_stop=xys[i][1]+1
                x_iterator=1
            if xys[i][2]> xys[i][3]:
                y_start=xys[i][2]
                y_stop=xys[i][3]-1
                y_iterator=-1
            if xys[i][2]<xys[i][3]:
                y_start=xys[i][2]
                y_stop=xys[i][3]+1
                y_iterator=1
            
            for i, x_diag in enumerate(range(x_start, x_stop, x_iterator)):
                y_diag=y_start+(i*y_iterator)
                diagram[x_diag][y_diag]+=1                    
                    
    total_crossings=0
    for x in range(max_x+1):
        for y in range(max_y+1):
            if diagram[x][y]>1:
                total_crossings+=1
    print("Total crossings =", total_crossings)
    
