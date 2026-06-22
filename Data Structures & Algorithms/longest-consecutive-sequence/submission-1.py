class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return(0)
        l=nums[0]
        m=nums[0]
        ans=0
        for i in range(len(nums)):
            if nums[i]>m:
                m=nums[i]
            elif nums[i]<l:
                l=nums[i]
        print(l,m)
        t=0
        for j in range(l,m+2,1):
            
            if j in nums:
                t=t+1
                print(t)
            else:
                if t>ans:
                    print(t)
                    ans=t
                    t=0
                else:
                    t=0
        
        return(ans)


            

        