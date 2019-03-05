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

#calculate power
def calpower(para, Aarray):
    Asize = len(Aarray)
    returnpower = 0
    alen = 1
    print(para)
    while alen <= Asize:
        start = 0
        while start + alen <= Asize :
            idx = 0
            while idx < alen:
                returnpower += Aarray[idx+start]*para[idx]
                idx = idx + 1
#                print("idx=" + str(idx) + "start="+str(start)+"alen="+str(alen)+"Asize="+str(Asize))
            start = start + 1
            #print("idx=" + str(idx) + "start="+str(start)+"alen="+str(alen)+"Asize="+str(Asize))

        alen = alen + 1
    return returnpower
#do loop for input



i = 0
while i < inputsize:
    k = int(numarr[i][1])
    aarr = buildA(int(numarr[i][0]),int(numarr[i][4]) + int(numarr[i][5]),int(numarr[i][6])+int(numarr[i][7]),int(numarr[i][8]),int(numarr[i][2])+int(numarr[i][3]))
    #debug
    print(aarr)
    j = 0
    power = 0
    para = [1]*len(aarr)
    totalpower = 0
    while j < k:
        m = 1
        while m <= len(para):
            para[m-1] *= m%1000000007 
            m += 1
        #print(calpower(para,aarr))
        totalpower += calpower(para,aarr)
        j = j + 1
    print("Case #"+str(i+1)+": "+ str(totalpower%1000000007))
    i = i + 1
    
