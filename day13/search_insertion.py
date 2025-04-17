class Solution:
    def searchInsert(self,nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left

sol=Solution()
nums=[1,3,4,5,6]
target=2
res=sol.searchInsert(nums,target)
print(res)