class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            num = -int(str(x)[len(str(x)):0:-1])
        else:
            num = int(str(x)[::-1])

        if num > 2 ** 31 - 1 or num < -2 ** 31:
            return 0
        else:
            return num