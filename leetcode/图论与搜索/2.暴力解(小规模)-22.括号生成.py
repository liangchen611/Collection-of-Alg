class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = [[] for _ in range(0,n)]
        res[0]=["()"]
        count = n
        current = ""
        
        if n==1:
            return res[0]
        elif n>1:
            for i in range(1,n):
                stack = res[i-1]
                for j in range(0,len(stack)):
                    elem = stack[j]
                    for k in range(0,len(elem)):
                        current = elem[:k]+"()"+elem[k:]
                        if current not in res[i]:
                            res[i].append(current)
        return(res[n-1])
 