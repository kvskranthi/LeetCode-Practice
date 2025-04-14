class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[]
        m=0
        l.append(m)
        for g in gain:
            if g<0:
                g=g*-1
                m=m-g
                l.append(m)
            else:
                m=m+g
                l.append(m)
        print(l)
        return max(l)

        