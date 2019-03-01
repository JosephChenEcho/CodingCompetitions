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
