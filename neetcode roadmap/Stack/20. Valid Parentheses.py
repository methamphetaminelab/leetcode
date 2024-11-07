class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {')': '(', '}': '{', ']': '['}

        for bracket in s:
            if bracket in bracketMap.values():
                stack.append(bracket)

            elif bracket in bracketMap.keys():
                if not stack or stack[-1] != bracketMap[bracket]:
                    return False
                
                stack.pop()

        return not stack