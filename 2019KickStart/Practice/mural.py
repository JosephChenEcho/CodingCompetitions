#input value
inputsize = input()
i = 0
inputsize = int(inputsize)
muralsize = [0]*inputsize
muralscore = [None]*inputsize
i=0
while i < inputsize:
    muralsize[i] = int(input())
    muralscore[i] = str(input())
    i = i + 1

def maxsubsum(numarr, numsize):
    ret  = 0
    i = 0
    sumsub = 0
    while i < numsize:
        sumsub += int(numarr[i])
        i = i + 1
    j = 0
    ret = sumsub
    while i < len(numarr):
        sumsub = sumsub - int(numarr[j]) + int(numarr[i])
        ret = max(ret,sumsub)
        j = j + 1
        i = i + 1
    return ret


#do loop for input
i = 0
while i < inputsize:
    arrsize = int((muralsize[i]+1)/2)
    print("Case #" + str(i+1) + ": " + str(maxsubsum(muralscore[i], arrsize)))
    i = i+1
