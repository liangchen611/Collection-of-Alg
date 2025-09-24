class Solution:
    def isValid(self, s: str) -> bool:
        signs = []
        valid = False
        for i in range(0,len(s)):
            sub_s = s[i]

            if len(signs)==0 and (sub_s==")" or sub_s=="}" or sub_s=="]"):
                return valid  

            if sub_s=="(" or sub_s=="{" or sub_s=="[":
                signs.append(sub_s)

            if sub_s==")" or sub_s=="}" or sub_s=="]":
                right = signs.pop()

                if sub_s==")" and right == "(":
                    continue

                if sub_s=="}" and right == "{":
                    continue
                
                if sub_s=="]" and right == "[":
                    continue

                else:
                    return valid
        
        if len(signs)==0:
            valid=True
            return valid
            
        elif len(signs)!=0:
            return valid