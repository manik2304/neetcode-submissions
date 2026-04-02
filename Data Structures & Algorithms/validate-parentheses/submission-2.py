
class Solution:
    def isValid(self, s: str) -> bool:

        match = {')':'(','}':'{',']':'['}
        stack = []
        for bracket in s:
            if bracket in match: # only check for closing brackets

                if not stack or stack[-1]!=match[bracket]:
                    return False
                stack.pop()
            else: # push opening brackets
                stack.append(bracket)

        return len(stack)==0
        

        

       