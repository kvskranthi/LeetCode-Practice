class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split()
        st=arr[::-1]
        return " ".join(st)