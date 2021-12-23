with open('9-input.txt','r') as f:
    
    #input = [2199943210
#3987894921
#9856789892
#8767896789
#9899965678] ## Example
    
    input_lines = f.read().splitlines()
    risk=[]
    

    basin_sizes=[]
    for i,line in enumerate(input_lines):
        for j,num in enumerate(line):
            basin_size=0
            if input_lines[i][j]!='9':
                basin_size+=1
                input_lines[i][j]='9'
                for k,numk in enumerate(line):
                    if k>j:
                        if numk!='9':
                            basin_size+=1
                            input_lines[i][k]='9'
                        else:
                            break
                


                basin_sizes.append(basin_size)
            else:
                continue
            















'''
            if i==0 and j==0:
                min_adjacent = min(int(input_lines[i][j+1]), int(input_lines[i+1][j]))
            elif i==0 and j==99:
                min_adjacent = min(int(input_lines[i][j-1]), int(input_lines[i+1][j]))
            elif i==0:
                min_adjacent = min(int(input_lines[i][j-1]), int(input_lines[i][j+1]), int(input_lines[i+1][j]))
            elif i==99 and j==0:
                min_adjacent = min(int(input_lines[i-1][j]), int(input_lines[i][j+1]))
            elif i==99 and j==99:
                min_adjacent = min(int(input_lines[i-1][j]), int(input_lines[i][j-1]))
            elif i==99:
                min_adjacent = min(int(input_lines[i-1][j]), int(input_lines[i][j-1]), int(input_lines[i][j+1]))
            elif j==0:
                min_adjacent = min(int(input_lines[i-1][j]), int(input_lines[i][j+1]), int(input_lines[i+1][j]))
            elif j==99:
                min_adjacent = min(int(input_lines[i-1][j]), int(input_lines[i][j-1]), int(input_lines[i+1][j]))
            else:                
                min_adjacent = min(int(input_lines[i-1][j]), int(input_lines[i][j-1]), int(input_lines[i][j+1]), int(input_lines[i+1][j]))
            

            if int(input_lines[i][j])<min_adjacent:
                tmp_risk=int(input_lines[i][j])+1
                risk.append(tmp_risk)
        

    print("Total risk =", sum(risk))
        
'''
