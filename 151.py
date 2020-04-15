class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split(" ")
        l1 = l1[::-1]
        l1 = [x for x in l1 if x not in ["", " "]]
        print(l1)
        r = " ".join(l1)
        r = r.strip()
        return r
