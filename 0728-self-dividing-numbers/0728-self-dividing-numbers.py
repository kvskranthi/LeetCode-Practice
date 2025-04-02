class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            i = str(i)
            k=int(i)
            if len(i)==1:
                ans.append(k)
            else:
                c=0
                for j in i:
                    j =int(j)
                    if j!=0 and k%j==0:
                        c=c+1
                if len(i)==c:
                    ans.append(k)
        return ans