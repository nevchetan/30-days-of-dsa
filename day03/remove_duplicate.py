#the question is to remove a duplicate element from the array without using a new array we need to replace it in place as we dont have extra memory
#problem link- https://leetcode.com/problems/remove-duplicates-from-sorted-array
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        j=1
        for i in range(1,n):
            if nums[i]!= nums[i-1]:
                 nums[j]=nums[i]
                 j+=1

        return j
      
sol=Solution()
nums=[0,0,1,1,1,2,3,3,4]
res=sol.removeDuplicates(nums)
print(res)