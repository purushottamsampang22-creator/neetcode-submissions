class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=sorted(stones)
        print(s)
        l=len(s)-1
        while(len(s)>1):
            s[l-1]=s[l]-s[l-1]
            del s[l]
            l=l-1
            s=sorted(s)
            
        return(s[l])

