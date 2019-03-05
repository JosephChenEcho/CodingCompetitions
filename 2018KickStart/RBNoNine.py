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
    retval = 0
    j = 0
    while j < len(inumber):
        retval *= 9
        retval += int(inumber[j]) % 9
        j += 1
    
    #print(int(retval/9))
    #print(retval%9)
    retval -=  int(retval/9)
    return retval

#do loop for input
i = 0
while i < inputsize:
    print(countvalidnum(startnum[i]))
    print(countvalidnum(endnum[i]))
          
    i += 1
