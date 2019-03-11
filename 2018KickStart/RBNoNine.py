#input value

inputsize = input()
inputsize = int(inputsize)
i = 0
startnum = [None]*inputsize
endnum = [None]*inputsize
while i < inputsize:
    inputline = input().split()
    startnum[i] = inputline[0]
    endnum[i] = inputline[1]
    i += 1

#function
def countvalidnum(inumber):
    inumber = int(inumber)
    ret1 = 0
    while(inumber % 10 != 0):
        if(inumber % 9 != 0):
            ret1 += 1
        inumber -= 1
    if(inumber%9 != 0):
        ret1 += 1
    ret2 = 0
    base = 1
    #convertBase9count
    while(inumber != 0):
        ret2 = ret2 + base*(inumber%10)
        inumber = int(inumber/10)
        base *= 9
    #print(ret1+int(ret2*8/9))
    return ret1+int(ret2*8/9)

#do loop for input
i = 0
while i < inputsize:
    print("Case #"+str(i+1)+": " + str(countvalidnum(endnum[i])-countvalidnum(startnum[i])+1))
    
          
    i += 1
