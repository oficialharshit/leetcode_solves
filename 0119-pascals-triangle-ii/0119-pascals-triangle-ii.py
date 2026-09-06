class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        ans = [1]
        a = 1
        for i in range(1,n+1):
            a = a * (n-i+1)
            
            a = a/i
            ans.append(a)
        return ans
        