class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pas = 0
        thash = set()
        if len(s) == len(t):
            for i in t:
                thash.add(i)
            for i in thash:
                if t.count(i) == s.count(i):
                    print(pas, i, t.count(i), s.count(i))
                    pas += t.count(i)
                else:
                    break
            if pas == len(s):
                return True
            else:
                return False
        else:
            return False