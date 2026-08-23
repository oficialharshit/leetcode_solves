class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxi = -1
        ans = []
        for i in range(len(arr)-1,-1,-1):
            ans.append(maxi)
            maxi = max(arr[i],maxi)
        
        return ans[::-1]
                