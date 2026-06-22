class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        h=0
        ans=[]
       
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
                if d[nums[i]]>h:
                    h=d[nums[i]]

            else:
                d[nums[i]]=1
                if d[nums[i]]>h:
                    h=d[nums[i]]
        
        while(k>0):
            for i in d:
                if d[i]==h:
                    ans.append(i)
                    k=k-1
            h=h-1
        return(ans)
                
                
        
        