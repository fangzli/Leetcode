nums = [1,0,1,2,3]
# 283 Move Zeros
key = 0
for i in range(len(nums)):
    if (nums[i] != 0) & (key != i):
        nums[key] = nums[i]
        nums[i] = 0
        key += 1
    elif (nums[i] != 0) & (key == i):
        key += 1

print(nums)