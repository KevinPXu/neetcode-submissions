class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            length = len(s)
            encoded_str += str(length) + "#" + s
        return encoded_str


    def decode(self, s: str) -> List[str]:
        idx = 0
        decoded = []
        while idx < len(s):
            str_len = ""
            while s[idx] != "#":
                str_len += s[idx]
                idx += 1
            idx += 1
            decoded.append(s[idx: idx + int(str_len)])
            idx += int(str_len) 
        return decoded