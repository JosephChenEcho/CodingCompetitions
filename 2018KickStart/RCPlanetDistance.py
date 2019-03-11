#input value

inputsize = input()
inputsize = int(inputsize)
i = 0
tube = [None]*inputsize
while i < inputsize:
    tsize = int(input())
    tube[i] = [None]*tsize
    j = 0
    while j < tsize:
        tube[i][j] = input()
        j += 1
    i += 1


#build matrix
def buildmatrix(msize, mtube):
    retm = [[0]*msize]*msize
    j = 0
    while j < msize:
        mi = int(mtube[j].split()[0]) - 1
        mj = int(mtube[j].split()[1]) - 1
        retm[mi][mj] = 1
        retm[mj][mi] = 1
        
        j += 1
    
    return retm

#do dfs
def dfs(ans, map):

#do loop in input
i = 0
while i < inputsize:
    map = buildmatrix(len(tube[i]), tube[i])
    ans = [0] * len(tube[i])
    
    i += 1
