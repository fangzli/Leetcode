class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}
        for l in s:
            if l in dict1:
                dict1[l] += 1
            else:
                dict1[l] = 1
        for l in t:
            if l in dict2:
                dict2[l] += 1
            else:
                dict2[l] = 1
        return dict1 == dict2