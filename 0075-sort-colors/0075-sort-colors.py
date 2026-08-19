class Solution(object):
    def sortColors(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in range(len(arr)):
            if arr[i]==0:
                count[0]+=1
            elif arr[i]==1:
                count[1]+=1
            else :
                count[2]+=1
        index = 0
        for i in range(count[0]):
            arr[index]=0
            index+=1
        for i in range(count[1]):
            arr[index]=1
            index+=1
        for i in range(count[2]):
            arr[index]=2
            index+=1