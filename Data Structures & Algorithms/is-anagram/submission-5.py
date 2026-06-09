class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        for char in s:
            if (t.find(char) == -1):
                return False
            print(t.find(char))
            t = t.replace(t[t.find(char)], "", 1)
        
        return True