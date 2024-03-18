def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "第一象限"
    elif x < 0 and y > 0:
        return "第二象限"
    elif x < 0 and y < 0:
        return "第三象限"
    elif x > 0 and y < 0:
        return "第四象限"
    elif x == 0 and y != 0:
        return "位于y轴上"
    elif y == 0 and x != 0:
        return "位于x轴上"
    else:
        return "坐标原点"

x = eval(input())
y = eval(input())

print(find_quadrant(x, y))

