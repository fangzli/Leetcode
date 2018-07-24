n = 6
oldStr = '1'
for _ in range(n - 1):
    tmp = ''
    count = 1
    for i in range(1, len(oldStr) + 1):
        if i < len(oldStr) and oldStr[i] == oldStr[i - 1]:
            count += 1
        else:
            tmp += str(count) + oldStr[i - 1]
            count = 1
    oldStr = tmp

print(oldStr)