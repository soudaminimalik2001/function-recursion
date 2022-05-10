#o/p=1,2,4,8,16,32,64,128,256
def num(a):
    if a==1:
        return 1
    else:
        return 2 * num(a-1)
i=1
while i<10:
    print(num(i))
    i+=1
    