# 66
# Solution 1
digits = [9,9]
s = ""
result = []
for item in digits:
    s += str(item)
i = int(s)
i += 1

for item in str(i):
    result.append(int(item))

print(result)