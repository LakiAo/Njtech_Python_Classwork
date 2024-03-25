a, b = (eval(input()) for _ in range(2))
print(max(i for i in range(1, min(a, b)+1) if a % i == 0 and b % i == 0))