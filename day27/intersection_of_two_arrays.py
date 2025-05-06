#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums1:
            if i in nums2:
                res.append(i)
        return res
 
 
s=Solution()
ans=s.intersection([1,2,1,2],[2,3])
print(ans)       