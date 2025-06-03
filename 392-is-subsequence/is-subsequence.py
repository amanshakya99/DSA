class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
         return True
        correct=len(s)
        start =0
        for letter in t:
            if s[start] == letter:
                start+=1
            if start == correct:
                return True

        return False

        
