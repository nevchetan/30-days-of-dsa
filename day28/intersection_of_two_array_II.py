#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


from collections import Counter
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1=Counter(nums1)
        count2=Counter(nums2)
        res=[]
        for i in count1:
            if i in count2:
                res.extend([i]*min(count1[i],count2[i]))
        return res

s=Solution()
ans=s.intersect([1,2,2,1],[2,2])
print(ans)