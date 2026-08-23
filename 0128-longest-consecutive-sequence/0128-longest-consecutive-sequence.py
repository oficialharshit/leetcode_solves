class Solution(object):
    def longestConsecutive(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(arr)==0:
            return 0
        bl = set(arr)
        leng = 1
        for num in bl:
            if num-1 not in bl:
                cnt = 1
                x = num
                while x+1 in bl:
                    x+=1
                    cnt+=1
                leng = max(leng,cnt)
        return leng
