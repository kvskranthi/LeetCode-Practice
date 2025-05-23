class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if n == 0:
                return True
        
            if flowerbed[i] == 0: 
                left_empty = (i == 0) or (flowerbed[i - 1] == 0) 
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0) 
                if left_empty and right_empty:  
                    flowerbed[i] = 1
                    n -= 1
        return n == 0     