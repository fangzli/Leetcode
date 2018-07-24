# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         i = j = count = 0
#         while i < m and j < n:
#             if nums1[i] <= nums2[j]:
#                 i += 1
#             else:
#                 tmp = nums1[i]
#                 nums1[i] = nums2[j]
#                 nums1[m + count] = tmp
#                 count += 1
#                 i += 1
#                 j += 1
#         while j < n:
#             nums1[i + j] = nums2[j]
#             j += 1
#
#
#
#
#         print(nums1)
#         print i,j
#
# M = Solution()
# # M.merge([1,3,2,0,0,0],3,[2,5,6],3)
# M.merge([1,2,4,5,6,0],5,[3],1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            return None
        if not nums2:
            return nums1
        nums3 = [None] * len(nums1)
        i = j = 0
        leftDone = False
        rightDone = False
        max1 = max(nums1)
        max2 = max(nums2)
        max12 = max(max1, max2) + 1
        while i < m or j < n:
            print("i", i, "j", j, "num3", nums3, "leftDone?", leftDone, "rightDone?", rightDone)
            if leftDone:
                left = max12
            else:
                left = nums1[i]
            if rightDone:
                right = max12
            else:
                right = nums2[j]
            if left <= right and not leftDone:
                nums3[i + j] = nums1[i]
                i += 1
                if i >= m:
                    leftDone = True
            elif left > right and not rightDone:
                nums3[i + j] = nums2[j]
                j += 1
                if j >= n:
                    rightDone = True
            # elif leftDone:
            #     nums3[i + j] = nums2[j]
            #     j += 1
            # elif rightDone:
            #     nums3[i + j] = nums1[i]
            #     i += 1
            else:
                raise Exception("Should not be here")
        nums1 = nums3


M = Solution()

# M.merge([1, 2, 4, 5, 6, 0], 5, [3], 1)
nums1 = [1, 2, 3, 0, 0, 0]
M.merge(nums1, 3, [2, 5, 6], 3)
print(nums1)
print(float("inf"))
