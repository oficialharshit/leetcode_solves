class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        result = 0
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]]+=1
            while count[s[i]]>2:
                count[s[left]]-=1
                left+=1
            result = max(result,i-left+1)
        return result


        