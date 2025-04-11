class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=["+","-","/","*"]
        s=[]
        for token in tokens:
            if token in a:
                o2=s.pop()
                o1=s.pop()
                res=0
                if token=="+":
                    res=int(o1)+int(o2)
                elif token=="-":
                    res=int(o1)-int(o2)
                elif token=="*":
                    res=int(o1)*int(o2)
                else:
                    res=int(o1)/int(o2)
                s.append(res) 
            else:
                s.append(token)    
        return int(s[0]) 