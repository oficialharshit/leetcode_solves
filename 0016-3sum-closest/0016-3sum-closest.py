class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                # If current sum is closer to target
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Exact answer
                if current == target:
                    return current

                # Move pointers
                if current < target:
                    left += 1
                else:
                    right -= 1

        return closest
        