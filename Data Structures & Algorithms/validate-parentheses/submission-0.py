class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack or hash[i] != stack.pop():
                    return False
        if stack:
            return False
        return True
