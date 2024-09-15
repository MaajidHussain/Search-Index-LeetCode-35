class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] > target or nums[i]==target:
                return i
        return len(nums)
            
                
solution=Solution()
nums = [1,3,5,6]
target = 2
result=solution.searchInsert(nums,target)
print(result)