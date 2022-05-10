#o/p=1, 4, 7, 10, 13, 16 ...
def num(a):
    if a==1:
        return 1
    else:
        return num(a)
i=1
while i<20:
    print(num(i))
    i+=3
    