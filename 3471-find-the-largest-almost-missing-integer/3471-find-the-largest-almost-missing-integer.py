class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
        for i in range(len(nums)-k+1):
            window = nums[i:i+k]
            for x in set(window):
                count[x]=count.get(x,0)+1
        ans = -1
        for i in count:
            if count[i]==1:
                ans = max(ans,i)
        return ans