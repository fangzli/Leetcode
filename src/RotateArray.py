def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums2 = [None] * len(nums)
    for i in range(len(nums)):
        nums2[(i + k) % len(nums)] = nums[i] # this make sure it works even if k > n

    return nums2
    # for i in range(len(nums)):
    #    nums[i] = nums2[i]


# print(rotate([1,2,3,4,5,6,7], 3))

def reverse(nums, start, end):
    # reverse an array
    # if you want to reverse the whole array, start = 0, end = length - 1
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start+=1
        end-=1
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(reverse(nums,k,len(nums)-1))

"""
nums = nums[::-1]
nums = nums[0:k][::-1] + nums[k:len(nums)][::-1]
print(nums) 
"""
