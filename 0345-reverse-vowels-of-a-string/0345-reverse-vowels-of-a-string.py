class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=[]
        for i in s:
            arr.append(i)
        d=['a','e','i','o','u','A','E','I','O','U']
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i] in d and arr[j] in d:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j=j-1
            elif arr[i] not in d:
                i+=1
            elif arr[j] not in d:
                j=j-1
        a = ''.join(arr)
        return a
