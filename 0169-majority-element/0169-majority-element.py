class Solution(object):
    def majorityElement(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        el = 0 
        for i in range(len(arr)):
            if count == 0:
                count = 1
                el = arr[i]
            elif arr[i]==el:
                count+=1
            else:
                count-=1
        return el