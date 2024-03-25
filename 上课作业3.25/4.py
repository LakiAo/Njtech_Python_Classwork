def huiwen(n):
    if n == n[::-1]:
        return True

n = input()
hw = []

for i in range(1,int(n)+1):
    if huiwen(str(i)):
        hw.append(str(i))

print(','.join(hw))