class Solution(object):
    def maxProfit(self, arr):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = arr[0]
        maxi = 0
        for i in range(1,len(arr)):
            maxi = max(maxi,arr[i]-mini)
            mini = min(mini,arr[i])
        return maxi

            
        

        