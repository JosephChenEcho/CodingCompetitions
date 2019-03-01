#input value
print("hello world")
len = input()
print("len="+len)
i = 0
len = int(len)
num = [None]*len
while i < int(len):
    x = input()    
    num[i] = int(x)
    i = i+1
    print(i)



#function
def tailnum(len, tail):
    len = int(len)
    ret = int(tail)
    i = 0
    while i < len:
        ret = ret*10 + tail
        i = i + 1
    return ret

print(tailnum(5,0))
print(tailnum(3,8))
