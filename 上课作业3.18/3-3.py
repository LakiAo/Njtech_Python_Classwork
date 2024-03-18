name,group = [],[]
for i in range(4):
    a = input()
    name.append(a)
for i in range(4):
    group.append(name[i][-1])
print("".join(group))