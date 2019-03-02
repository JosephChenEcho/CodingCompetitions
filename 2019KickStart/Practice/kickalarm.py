#input value

inputsize = input()
i = 0
inputsize = int(inputsize)
numarr = [None]*inputsize
while i < inputsize:
    numarr[i] =  input().split()
    i = i+1

#build A[]
def buildA(asize,cd,e1e2,f,init):
    retarr = [None]*asize
    retarr[0] = init % f
    i = 1
    while i < asize:
        retarr[i] = (retarr[i-1]*cd+e1e2)%f
        i = i + 1
    return retarr

#do loop for input
i = 0
while i < inputsize:
    k = int(numarr[i][1])
    aarr = buildA(int(numarr[i][0]),int(numarr[i][4]) + int(numarr[i][5]),int(numarr[i][6])+int(numarr[i][7]),int(numarr[i][8]),int(numarr[i][2])+int(numarr[i][3]))
    #debug
    print(aarr)
    j = 0
    power = 0
    while j < k:


        j = j + 1
    
    i = i + 1
    
