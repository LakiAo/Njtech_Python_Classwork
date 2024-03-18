up = down = 1
for i in range(365):
    down *= 0.99
    up *= 1.01
print("天天向上：", up)
print("天天向下：", down)