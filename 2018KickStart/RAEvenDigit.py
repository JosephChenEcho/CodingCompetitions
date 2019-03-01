#input value

inputsize = input()
print("inputsize="+inputsize)
i = 0
inputsize = int(inputsize)
strnum = [None]*inputsize
while i < inputsize:
    x = input()    
    strnum[i] = str(x)
    i = i+1


#function
def addtail(head, tail, inputsize):
    tail = int(tail)
    inputsize = int(inputsize)
    i = 0
    ret = int(head)
    while i < inputsize:
        ret = ret * 10 + tail
        i = i + 1
    return ret


#do loop for input
i = 0
while i < inputsize:
    strn = strnum[i]
    j = 0
    ans = 0
    upperval = 0
    lowerval = 0
    while j < len(strn):
        a = int(strn[j])
        if(a%2 == 0):
            ans = ans * 10 + a
        else:
            if(a == 9):
                if (ans == 0):
                    upperval = addtail(1, 0, len(strn) + 1)
                    lowerval = addtail(ans, 8, len(strn))
                    break
                else:
                    lowerval = addtail(ans*10 + a - 1, 8, len(strn) - j - 1)
                    break
            else:
                upperval = addtail(ans*10 + a + 1, 0, len(strn) - j - 1)
                lowerval = addtail(ans*10 + a - 1, 8, len(strn) - j - 1)
                break
             
        j = j + 1
    if(j == len(strn)):
        print("Case #" + str(i+1) + ": "+ str(0))
    elif(upperval == 0):
        print("Case #" + str(i+1) + ": "+ str(int(strn) - lowerval))
    else:        
        print("Case #" + str(i+1) + ": "+ str(min(upperval - int(strn),int(strn) - lowerval)))
    i = i + 1
