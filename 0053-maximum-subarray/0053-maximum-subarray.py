class Solution(object):
    def maxSubArray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = float('-inf')
        sum = 0
        for i in range(len(arr)):
            sum+=arr[i]
            if sum>maxi:
                maxi = max(maxi,sum)
            if sum<0:
                sum = 0
        return maxi
        