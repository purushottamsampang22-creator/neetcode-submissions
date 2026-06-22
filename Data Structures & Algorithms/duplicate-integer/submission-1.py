class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=[]
        for i in range(len(nums)):
            if nums[i] in num:
                return True
            else:
                num.append(nums[i])
        return False
        