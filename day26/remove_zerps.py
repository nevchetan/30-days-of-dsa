#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=nums.count(0)
        while 0 in nums:
            nums.remove(0)
        nums.extend([0]*count)
        
       
s=Solution()
nums=[0,1,0,2,3]
ans=s.moveZeroes(nums)
print(nums)