class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=[]
        for i in range(len(nums)):
            if nums[i] in n:
                return True
            else:
                n.append(nums[i])
        return False