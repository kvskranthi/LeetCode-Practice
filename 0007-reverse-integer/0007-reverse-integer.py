class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            a=-1*x
            b=str(a)[::-1]
            b=int(b)*-1
            if -2**31 <= b <= 2**31 - 1:
                return b
            else:
                return 0
        else:
            r=str(x)[::-1]
            if -2**31 <= int(r) <= 2**31 - 1:
                return int(r)
            else:
                return 0