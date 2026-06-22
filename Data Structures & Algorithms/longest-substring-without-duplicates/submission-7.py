class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return(1)
        a=[]
        ans=0
        for i in s:
            if i in a:
                if ans<len(a):
                    ans=len(a)
                    p=0
                    
                    j=0
                    for j in range(len(a)):
                        if i==a[j]:
                            p=j
                            break
                    a=a[p+1:]
                    a.append(i)
                else:
                    p=0
                    j=0
                    for j in range(len(a)):
                        if i==a[j]:
                            p=j
                            break
                    a=a[p+1:]
                    a.append(i)
            else:
                a.append(i)
            
        if len(a)>ans:
            ans=len(a)
        return(ans)

        