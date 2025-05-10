#Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        t_nums=list(set(nums))
        t_nums.sort()
        if len(t_nums)<=2:
            return max(t_nums)
        else:
            return t_nums[-3]

s=Solution()
ans=s.thirdMax([1,2,2,3,5,5])
print(ans)