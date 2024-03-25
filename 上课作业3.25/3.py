n = int(input())
s = 0
for i in range(10**(n-1),10**n):
    for j in range(len(str(i))):
        s += int(str(i)[j])**n
    if i == s:
        print(i,end=" ")
    s=0