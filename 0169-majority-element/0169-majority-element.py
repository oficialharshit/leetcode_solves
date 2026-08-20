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
        count1=0
        for i in range(len(arr)):
            if arr[i]==el:
                count1+=1
        if count1 > len(arr)/2:
            return el
        return -1