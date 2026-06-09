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
            else:
                if not stack or hash[i] != stack.pop():
                    return False
        if stack:
            return False
        return True
