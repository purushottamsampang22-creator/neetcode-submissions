class Solution:
    def hammingWeight(self, n: int) -> int:
        if n==0:
            return(0)
        f=1
        while(n>1):
            if n%2==1:
                f=f+1
                n=n-1
                n=n/2
            else:
                n=n/2
        return(f)