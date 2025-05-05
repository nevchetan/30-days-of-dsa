#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:]=nums2
        nums1.sort()
        print(nums1)
        

        

        
s=Solution()
res=s.merge([1,2,3,0,0],3,[4,3,5],3)
print(res)        