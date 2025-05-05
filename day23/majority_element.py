#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=len(nums)/2
        set_nums=set(nums)
        for i in set_nums:
            if nums.count(i)>=count:
                return i
s=Solution()
res=s.majorityElement([3,2,3])   
print(res)    