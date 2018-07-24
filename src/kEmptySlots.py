class Solution:
    """
    @param flowers: the place where the flower will open in that day
    @param k:  an integer
    @return: in which day meet the requirements
    """

    def kEmptySlots(self, flowers, k):
        n = len(flowers)
        if n == 0 or k >= n - 1:
            return -1
        garden = [0] * (n + 1)
        for i in range(n):
            if self.isValid(flowers[i], k, n, garden):
                return i + 1
        return -1

    def isValid(self, x, k, n, garden):
        garden[x] = 1
        if x + k + 1 <= n and garden[x + k + 1] == 1:
            for i in range(x + 1, x + k + 1):
                if garden[i] == 1:
                    return False
            return True
        if x - k - 1 > 0 and garden[x - k - 1] == 1:
            for i in range(x - 1, x - k - 1, -1):
                if garden[i] == 1:
                    return False
            return True
        return False


M = Solution()
print(M.kEmptySlots([1,2,3,4], 1))