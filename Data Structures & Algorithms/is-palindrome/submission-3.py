class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i, j = 0, len(s) - 1
        while i < j:
            # check if char is alphanumeric
            if not s[i].isalnum():
                i += 1
                continue
            
            if not s[j].isalnum():
                j -= 1
                continue
            
            print(s[i].lower())
            print(s[j].lower())

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

