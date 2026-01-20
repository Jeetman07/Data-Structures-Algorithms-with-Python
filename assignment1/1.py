a = input("")
newar = []
for i in range(len(a)):
    pos = 0
    while pos < len(newar) and newar[pos] <a[i]:
        pos += 1
    newar.insert(pos,a[i])
newar = "".join(newar)
print(newar)