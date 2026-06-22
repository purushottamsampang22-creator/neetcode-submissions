class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss=[]
        tt=[]
        if len(s)==len(t):
            for i in range(len(s)):
                ss.append(s[i])
                tt.append(t[i])
        else:
            return False
        for i in range(len(s)):
            if ss[i] in tt:
                tt.remove(s[i])
            else:
                return False
        return True   
                
        