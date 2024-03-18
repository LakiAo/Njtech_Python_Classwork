a = eval(input())
if a < 0:
    y = 0
elif 0 <= a < 5:
    y = a
elif 5 <= a < 10:
    y = 3*a - 5
elif 10 <= a < 20:
    y = 0.5*a - 2
elif a >= 20:
    y = 0
print(y)
