class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        
        for left in range(len(nums)-1):
            
            for right in range(left+1,len(nums)):
                if nums[left]+nums[right]==target:
                    return([left,right])
        
        
        
        
       
        return()
        
        