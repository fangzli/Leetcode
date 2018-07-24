class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # arr = []
        # for i,v in enumerate(list(s)):
        #     if v not in arr:
        #         arr.append(v)
        #     else:
        #         arr.remove(v)
        # return arr[0]
        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        for i,v in enumerate(s):
            if dict[v] == 1:
                return i
        return -1