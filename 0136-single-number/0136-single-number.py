from collections import defaultdict
class Solution(object):
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashed = defaultdict(int)
        for num in nums:
            hashed[num]+=1
        for key,value in hashed.items():
            if value == 1:
                return key

