class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                operations += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1
        return operations