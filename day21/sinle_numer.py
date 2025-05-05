#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_nums=set(nums)
        for i in set_nums:
            if nums.count(i)==1:
                return i
                
            
            
        
       
                    
        
s=Solution()
res=s.singleNumber([1,2,1,2,4])
print(res)