class Solution:
    def countChars(self, str:str) -> dict:
        counts = [0] * 26
    
        for char in str:
            # Check if character is a valid lowercase letter
            if 'a' <= char <= 'z':
                index = ord(char) - ord('a')
                counts[index] += 1  
        return counts
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idx = 0
        ans = []
        list_map = {}
        for s in strs:
            count = tuple(self.countChars(s))
            if count in list_map:
                ans[list_map[count]].append(s)
            else:
                list_map[count] = idx
                ans.append([])
                ans[idx].append(s)
                idx += 1

        return ans