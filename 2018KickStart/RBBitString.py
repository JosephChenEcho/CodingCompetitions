#input value

inputsize = input()
i = 0
inputsize = int(inputsize)
inputN = [None]*inputsize
inputK = [None]*inputsize
inputP = [None]*inputsize
con = [None]*inputsize
while i < inputsize:
    x = input()
    firstline = x.split()
    inputN[i] = int(firstline[0])
    inputK[i] = int(firstline[1])
    inputP[i] = int(firstline[2])
    j = 0
    con[i] = [None]*inputK[i]
    while j < inputK[i]:
        con[i][j] = input().split()
        j += 1

    i += 1

#function
def followcon(start, end, count1, e):
    print("start = " + str(start) + ", end=" + str(end))
    tnum = e
    idx = 0
    cnt = 0
    while idx < start:
        tnum = int(tnum/2)
        idx += 1
    while idx <= end:
        cnt += tnum%2
        tnum = int(tnum/2)
        idx += 1
    print("e = "+str(e)+",cnt = " + str(cnt) + ",count1 = " + str(count1))
    return cnt == count1 

        
#do loop for input
i = 0
while i < inputsize:
    master = list(range(pow(2, inputN[i])))
    j = 0
    
    while j < len(con[i]):
        print("con =" + str(con[i]))
        for e in master:
            st = inputN[i] - int(con[i][j][1])
            en = inputN[i] - int(con[i][j][0])
                                 
            if(not followcon(st,en, int(con[i][j][2]),e)):
                master.remove(e)
        j += 1
    print(master)
    i += 1
