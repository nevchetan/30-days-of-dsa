#In this we have to remove the element 
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         k = 0  # index to place non-val elements
         for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
         return k
sol=Solution()
nums=[3,2,2,3]
val=3
res=sol.removeElement(nums,val)
print(res)
