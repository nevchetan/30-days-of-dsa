#to find the closest number to zero in a given array

from typing import List
class Solution:
    def findClosestNumber(self,nums:List[int]) -> int:
        closest=nums[0]
        for num in nums[1:]:
            if abs(num)<abs(closest) or (abs(num)==abs(closest) and num>closest):
                closest=num
        return closest
    

s=Solution()
nums=[-1,2,3,1]
res=s.findClosestNumber(nums)
print(res)


