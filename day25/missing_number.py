#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums=sum(nums)
        sum_range=sum(range(len(nums)+1))
        return sum_range-sum_nums
        
      
s=Solution()
ans=s.missingNumber([1,0,3])
print(ans)