nums = [4,1,2,1,2]
# Solution 1
# def func containsDuplicate(nums):
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print("Contains Duplicate")
            break



# Solution 2
# return len(nums) > len(set(nums))


# nums.remove(2)

# print(sorted(nums))



