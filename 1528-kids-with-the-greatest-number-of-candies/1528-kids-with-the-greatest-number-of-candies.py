class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans =[]
        s = max(candies)
        for i in candies:
            w = i+extraCandies
            if (w>=s):
                ans.append(True)
            else:
                ans.append(False)
        return ans