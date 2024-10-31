class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ''
        for str in strs:
            s += f'{len(str)}#{str}'
        print(s)
        return s
    
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            lenght = int(s[i:j])
            i = j + 1
            j = i + lenght
            strs.append(s[i:j])
            i = j

        return strs