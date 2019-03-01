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
def addtail(tail, len):
    tail = int(tail)
    len = int(len)
    i = 0
    ret = tail
    while i < len - 1:
        ret = ret * 10 + tail
        i = i + 1
    return ret

print(addtail(0,3))
print(addtail(8,4))
