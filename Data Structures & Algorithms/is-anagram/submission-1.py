class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i=0
        f=0
        if(len(s)!=len(t)):
            return False
        while(i<len(t)):
            if t[i] in s:
                s=s.replace(t[i],'',1)
                i=i+1
                f=f+1
            else:
                i=i+1
        print(len(t))
        print(f)
        print(s)
        print(i)
        if f==len(t):
            return True
        else:
            return False
            
        