class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=[]
        for i in range(len(s)):
            if s[i]>='a' and s[i]<='z':
                ans.append(s[i])
            elif s[i]>='A' and s[i]<='Z':
                
                ans.append(s[i].lower())
            elif s[i].isdigit():
                ans.append(s[i])
        print(ans)
        if ans==ans[::-1]:
            return(True)
        else:
            return(False)
        