target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
tm = [None] * len(position)

for i in range(len(position)):
    tm[i] = (target - position[i])/speed[i]
tmax = max(tm)

count = 0
arr = [None] * len(position)

for i in range(len(position)):
    arr[i] = i

for t in range(int(tmax)):
    for i in range(len(position) - 1):
        for j in range(i + 1, len(position)):
            if (position[i] + speed[i]*t == position[j] + speed[j]*t) and (position[i] + speed[i]*t <= target) and (position[j] + speed[j]*t <= target):
                print(i,j)
                count += 1
# Not finished!


#print(tmax)
print count