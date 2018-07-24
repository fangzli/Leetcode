# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["aaa","aa","aaa"]
if not strs:
    print(0)
else:
    n = len(strs)
    prefix = strs[0]

    for i in range(1, n):

        m = len(strs[i])
        # print("i",i,m)
        if not prefix:
            break
        for j in range(m + 1):
            # print(j)
            if j >= m or j >= len(prefix) or prefix[j] != strs[i][j]:
                prefix = prefix[:j]
                # print("prefix",prefix)
                break

    print(prefix)