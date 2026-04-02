from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:

        match = defaultdict(str)
        match[')']='('
        match['}']='{'
        match[']']='['
        stack = []
        for bracket in s:
            if len(stack)>0 and stack[-1]==match[bracket]:
                stack.pop()
            else:
                stack.append(bracket)

        if len(stack)==0:
            return True
        else:
            return False
        

        

       