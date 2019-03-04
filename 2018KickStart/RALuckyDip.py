#input value

inputsize = input()
inputsize = int(inputsize)
i = 0
bagsize = [None]*inputsize
rediplimit = [None]*inputsize
itemvalue = [None]*inputsize

while i < inputsize:
    firstline =  input().split()
    bagsize[i] = int(firstline[0])
    rediplimit[i] = int(firstline[1])
    itemvalue[i] = input().split()
    i = i + 1

#funciont
def getnewE(prevE, bsize, ivalue):
    j = 0
    newE = 0
    while j < bsize:
        newE += max(prevE, int(ivalue[j]))
        j = j + 1
    newE = newE/bsize
    return newE

#todo
#optiomsize binary search for edge number

#do loop for input

i = 0
while i < inputsize:
    initE = 0
    itemi = 0
    redip = 0
    while itemi < bagsize[i]:
        initE += int(itemvalue[i][itemi])
        itemi = itemi + 1
    initE = initE/bagsize[i]
    nextE = initE
    while redip < rediplimit[i]:
        nextE = getnewE(initE, bagsize[i], itemvalue[i])
        redip = redip + 1
        initE = nextE
    print("Case #"+str(i+1)+": "+ str(nextE))
    i = i + 1

