class Solution(object):
    def maxArea(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0 
        left = 0
        right = len(arr)-1
        while left<right:
            hight = min(arr[left],arr[right])
            width = right - left 
            water = max(water,hight*width)
            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
                


        return water
            