class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for i in s:
            if i in hash.values():
                stack.append(i)
            elif stack and hash[i] == stack[-1]:
                stack.pop()
            else: 
                return False
        if stack:
            return False
        return True