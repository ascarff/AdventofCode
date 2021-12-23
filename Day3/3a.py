with open('3a-input.txt','r') as f:
    #lines = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'] ## Example
    lines = f.read().splitlines()
    zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
    ones = [0,0,0,0,0,0,0,0,0,0,0,0]
    gamma = ''
    epsilon = ''
    for line in lines:
        x = list(line)
        for i, n in enumerate(x):
            if int(n)==0: zeros[i]+=1
            elif int(n)==1: ones[i]+=1
            else: print("No idea")
    print(zeros)
    print(ones)
    for i, n in enumerate(zeros):
        if zeros[i]>ones[i]:
            gamma = gamma+'0'
            epsilon = epsilon+'1'
        elif ones[i]>zeros[i]:
            gamma = gamma+'1'
            epsilon = epsilon+'0'
        else:
            print("Uh-oh")

g=(int(gamma, 2))
e=(int(epsilon,2))

print(g*e)
