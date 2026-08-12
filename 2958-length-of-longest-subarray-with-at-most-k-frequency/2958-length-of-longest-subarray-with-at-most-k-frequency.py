class Solution(object):
    def maxSubarrayLength(self, nums, k):
        result = 0
        count = defaultdict(int)
        l = 0 # left pointer 
        for i in range(len(nums)): # this i will be the right pointer 
            count[nums[i]]+=1
            while count[nums[i]]>k:
                
                count[nums[l]]-=1
                l+=1 # move the left pointer
            result = max(result, i - l + 1) 
        return result
