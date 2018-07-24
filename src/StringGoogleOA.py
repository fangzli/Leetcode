S = "ab"
T = ""

def Sol(S, T):
    i = 0
    if not S:
        return False
    for char in T:
        while S[i] != char:
            i += 1
            if i >= len(S):
                return False
    return True

print(Sol(S,T))