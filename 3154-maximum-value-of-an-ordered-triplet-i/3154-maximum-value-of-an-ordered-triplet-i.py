class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    s= (nums[i] - nums[j]) * nums[k]
                    if s>ans:
                        ans=s
        if ans<= 0:
            return 0
        else:
            return ans